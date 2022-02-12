import struct
import abc
from typing import List, Tuple, Dict, Callable
import uuid
from types import SimpleNamespace
from collections import UserList
# from stat import *  # File type checking
from io import BytesIO


class BlockBytesIO(BytesIO):

    def __init__(self, block_size: int, initial_bytes=None):
        self.block_size = block_size
        super(BlockBytesIO, self).__init__(initial_bytes=initial_bytes)

    def read_in_block(self, block_id, in_block_offset=0, size=-1):
        self.seek(block_id * self.block_size)
        self.seek(in_block_offset, 1)
        size = self.block_size - size - 1 if size in (-1, None) else size
        if size < 0:
            raise ValueError
        return self.read(size)

    def write_in_block(self, block_id, buffer, in_block_offset=0):
        self.seek(block_id * self.block_size)
        self.seek(in_block_offset, 1)
        return self.write(buffer)


class BlockArray:

    def __init__(self, data: bytearray, bs=1024):
        self.data = memoryview(data)
        self.blocksize = bs
        self.shape = (self.data.nbytes // self.blocksize, self.blocksize)

    def data_index2block_index(self, item):
        if isinstance(item, slice):
            item = item.start, item.stop, item.step
            item = slice(*(i * self.blocksize if i is not None else i for i in item))
        else:
            item = item * self.blocksize
            try:
                self.data[item]
            except IndexError:
                raise
            item = slice(item, item + self.blocksize)
        return item

    def __getitem__(self, item):
        item = self.data_index2block_index(item)
        return self.data[item]

    def __setitem__(self, key, value):
        key = self.data_index2block_index(key)
        self.data[key] = value

    def __getattr__(self, item):
        return getattr(self.data, item)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.shape}'


class Bitmap:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def get_bit_location(num):
        bit_num = num % 8
        byte_num = (num - bit_num) // 8
        return byte_num, bit_num

    @staticmethod
    def get_bit_offset(bit_num):
        return bit_num

    def set_bit(self, n):
        byte_num, bit_num = self.get_bit_location(n)
        byte = self.data[byte_num]
        byte |= 1 << self.get_bit_offset(bit_num)
        self.data[byte_num] = byte

    def clear_bit(self, n):
        byte_num, bit_num = self.get_bit_location(n)
        byte = self.data[byte_num]
        byte &= ~(1 << self.get_bit_offset(bit_num))
        self.data[byte_num] = byte

    def get_bit(self, n):
        byte_num, bit_num = self.get_bit_location(n)
        bit = self.data[byte_num] & (1 << self.get_bit_offset(bit_num))
        return int(bool(bit))

    def __iter__(self):
        return (self.get_bit(i) for i in range(len(self.data) * 8))


class MySimpleNamespace(SimpleNamespace):

    def __init__(self, **kwargs):
        self._fields = tuple(kwargs)
        super().__init__(**kwargs)

    def __repr__(self):
        namespace = {i: self.__dict__[i] for i in self._fields}
        namespace_repr = ', '.join(f'{k}={v}' for k, v in namespace.items())
        return f'{self.__class__.__name__}({namespace_repr})'

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        return (getattr(self, i) for i in self._fields)


class FileSystemDataStructureModuleMeta(abc.ABCMeta):

    def __new__(mcs, name, bases, attrs):
        try:
            description = attrs['description']
        except KeyError as e:
            if MySimpleNamespace not in bases:
                class_name = e.__traceback__.tb_frame.f_locals['name']
                raise TypeError(f"{class_name} class must provide description attribute")
            return super().__new__(mcs, name, bases, attrs)
        structure = struct.Struct(''.join(i[0] for i in description))
        attrs['structure'] = structure
        attrs['size'] = structure.size
        return super().__new__(mcs, name, bases, attrs)


class FileSystemDataStructureModule(MySimpleNamespace, metaclass=FileSystemDataStructureModuleMeta):
    description: List[Tuple[str, str]]
    size: int
    structure: struct.Struct
    unpack_hooks: Dict[str, Callable] = {}
    pack_hooks: Dict[str, Callable] = {}

    def __init__(self, buffer=None, **kwargs):
        if buffer is not None:
            try:
                memoryview(buffer)  # check if an object supports the buffer protocol
            except TypeError as e:
                raise TypeError(e.args[0].replace('memoryview', self.__name__))
            data_structure_vars = self.unpack_variables(self.__class__.description, buffer)
            kwargs = data_structure_vars
        # must_args = {b: a for a, b in self.__class__.description}
        # left_args = must_args.keys() - kwargs.keys()
        # if left_args:
        #     raise TypeError(f'{self.__class__} missing {len(left_args)} required arguments: '
        #                     f'{str(left_args)[1:-1]}')
        super().__init__(**kwargs)
        self.unpack_hooks_apply()

    def unpack_hooks_apply(self):
        default_hook = (lambda x: x[0] if len(x) == 1 else x)
        for i in self._fields:
            value = getattr(self, i)
            hook = self.unpack_hooks.get(i, default_hook)
            new_value = hook(value)
            setattr(self, i, new_value)

    @staticmethod
    def unpack_variables(description, buffer):
        structure = struct.Struct(''.join(i[0] for i in description))
        unpacked = structure.unpack(buffer)
        ind = 0
        variables = {}
        for fmt, var_name in description:
            fmt_len = fmt[:-1]
            fmt_len = int(fmt_len) if fmt_len else 1
            value = unpacked[ind:ind + fmt_len]
            variables[var_name] = value
            ind += fmt_len
        return variables

    def pack_hooks_apply(self):
        def default_hook(x):
            try:
                x[0]
            except TypeError:
                x = x,
            return x

        for i in self._fields:
            value = getattr(self, i)
            hook = self.pack_hooks.get(i, default_hook)
            new_value = hook(value)
            setattr(self, i, new_value)

    def pack_variables(self):
        """In one iterable"""
        variables = ()
        self.pack_hooks_apply()
        for i in self:
            variables += i
        return variables

    def __bytes__(self):
        variables = self.pack_variables()
        return self.structure.pack(*variables)

    @abc.abstractmethod
    def to_file(self, *args, **kwargs):
        """Implements writing bytes to file"""

    @classmethod
    @abc.abstractmethod
    def from_file(cls, *args, **kwargs):
        """Implements fetch bytes for this structure from file"""


class SuperBlock(FileSystemDataStructureModule):
    # https://github.com/tytso/e2fsprogs/blob/master/lib/ext2fs/ext2_fs.h#L653
    description = [
        ('I', 's_inodes_count'),  # Inodes count TODO
        ('I', 's_blocks_count'),  # Blocks count TODO
        ('I', 's_r_blocks_count'),  # Reserved blocks count TODO
        ('I', 's_free_blocks_count'),  # Free blocks count
        ('I', 's_free_inodes_count'),  # Free inodes count
        ('I', 's_first_data_block'),  # First Data Block TODO
        ('I', 's_log_block_size'),  # Block size (log2 (block size) - 10) TODO
        ('i', 's_log_frag_size'),  # Fragment size (log2 (fragment size) - 10) TODO
        ('I', 's_blocks_per_group'),  # Blocks per group TODO
        ('I', 's_frags_per_group'),  # Fragments per group TODO
        ('I', 's_inodes_per_group'),  # Inodes per group TODO
        ('I', 's_mtime'),  # Mount time
        ('I', 's_wtime'),  # Write time
        ('H', 's_mnt_count'),  # Mount count
        ('h', 's_max_mnt_count'),  # Maximal mount count
        ('H', 's_magic'),  # Magic signature
        ('H', 's_state'),  # File system state
        ('H', 's_errors'),  # Behaviour when detecting errors
        ('H', 's_minor_rev_level'),  # minor revision level
        ('I', 's_lastcheck'),  # time of last check
        ('I', 's_checkinterval'),  # max. time between checks
        ('I', 's_creator_os'),  # OS
        ('I', 's_rev_level'),  # Revision level
        ('H', 's_def_resuid'),  # Default uid for reserved blocks
        ('H', 's_def_resgid'),  # Default gid for reserved blocks
        # These fields are for EXT2_DYNAMIC_REV superblocks only.
        # Note: the difference between the compatible feature set and
        # the incompatible feature set is that if there is a bit set
        # in the incompatible feature set that the kernel doesn't
        # know about, it should refuse to mount the filesystem.
        # e2fsck's requirements are more strict), if it doesn't know
        # about a feature in either the compatible or incompatible
        # feature set, it must abort and not try to meddle with
        # things it doesn't understand...
        ('I', 's_first_ino'),  # First non-reserved inode
        ('H', 's_inode_size'),  # size of inode structure
        ('H', 's_block_group_nr'),  # block group # of this superblock
        ('I', 's_feature_compat'),  # compatible feature set
        ('I', 's_feature_incompat'),  # incompatible feature set
        ('I', 's_feature_ro_compat'),  # readonly-compatible feature set
        ('16B', 's_uuid'),  # 128-bit uuid for volume
        ('16c', 's_volume_name'),  # volume name
        ('64c', 's_last_mounted'),  # directory where last mounted
        ('I', 's_algorithm_usage_bitmap'),  # For compression
        # Performance hints.  Directory preallocation should only
        # happen if the EXT2_COMPAT_PREALLOC flag is on.
        ('B', 's_prealloc_blocks'),  # Nr of blocks to try to preallocate
        ('B', 's_prealloc_dir_blocks'),  # Nr to preallocate for dirs
        ('H', 's_padding1'),
        ('204I', 's_reserved'),  # Padding to the end of the block
    ]

    unpack_hooks = {'s_uuid': lambda x: uuid.UUID(int=int(''.join(hex(i)[2:] for i in x), 16))}
    pack_hooks = {'s_uuid': lambda x: struct.unpack('16B', x.bytes)}

    def to_file(self, fd):
        fd.seek(1024)
        fd.write(bytes(self))

    @classmethod
    def from_file(cls, fd):
        fd.seek(1024)
        sb_raw = fd.read(cls.size)
        return cls(sb_raw)


class GroupDesc(FileSystemDataStructureModule):
    description = [
        ('I', 'bg_block_bitmap'),  # Blocks bitmap block
        ('I', 'bg_inode_bitmap'),  # Inodes bitmap block
        ('I', 'bg_inode_table'),  # Inodes table block
        ('H', 'bg_free_blocks_count'),  # Free blocks count
        ('H', 'bg_free_inodes_count'),  # Free inodes count
        ('H', 'bg_used_dirs_count'),  # Directories count
        ('H', 'bg_pad'),
        ('3I', 'bg_reserved'),
    ]

    def to_file(self, fd, group_desc_id, block_size=1024):
        fd.seek(1024 + block_size + self.size * (group_desc_id - 1))
        fd.write(bytes(self))

    @classmethod
    def from_file(cls, fd, group_desc_id, block_size=1024):
        fd.seek(1024 + block_size + cls.size * (group_desc_id - 1))
        group_desc_raw = fd.read(cls.size)
        return cls(group_desc_raw)


class Inode(FileSystemDataStructureModule):
    description = [
        ('H', 'i_mode'),  # File mode
        ('H', 'i_uid'),  # Low 16 bits of Owner Uid
        ('I', 'i_size'),  # Size in bytes
        ('I', 'i_atime'),  # Access time
        ('I', 'i_ctime'),  # Creation time
        ('I', 'i_mtime'),  # Modification time
        ('I', 'i_dtime'),  # Deletion Time
        ('H', 'i_gid'),  # Low 16 bits of Group Id
        ('H', 'i_links_count'),  # Links count
        ('I', 'i_blocks'),  # Blocks count
        ('I', 'i_flags'),  # File flags
        ('I', 'osd1'),  # OS dependent 1
        ('15I', 'i_block'),  # Pointers to blocks
        ('I', 'i_generation'),  # File version (for NFS)
        ('I', 'i_file_acl'),  # File ACL
        ('I', 'i_dir_acl'),  # Directory ACL
        ('I', 'i_faddr'),  # Fragment address
        ('B', 'l_i_frag'),  # Fragment number
        ('B', 'l_i_fsize'),  # Fragment size
        ('H', 'i_pad1'),
        ('H', 'l_i_uid_high'),  # these 2 fields
        ('H', 'l_i_gid_high'),  # were reserved2[0]
        ('I', 'l_i_reserved2'),
    ]

    def to_file(self, fd, inode_table_id, inode_id, block_size=1024):
        fd.seek(block_size * inode_table_id)
        fd.seek(self.size * (inode_id - 1), 1)
        fd.write(bytes(self))

    @classmethod
    def from_file(cls, fd, inode_table_id, inode_id, block_size=1024):
        fd.seek(block_size * inode_table_id)
        fd.seek(cls.size * (inode_id - 1), 1)
        inode_raw = fd.read(cls.size)
        return cls(inode_raw)


class DirectoryEntry(FileSystemDataStructureModule):
    description = [
        ('I', 'inode'),  # Inode number
        ('H', 'rec_len'),  # Directory entry length
        ('B', 'name_len'),  # Name length
        ('B', 'file_type'),
        ('255c', 'name'),  # File name
    ]

    def __init__(self, buffer=None, **kwargs):
        super().__init__(buffer, **kwargs)
        # Change name structure
        self.solve_name_directory()
        name_ind = [i[1] for i in self.description].index('name')
        self.description = self.description[:]
        self.description[name_ind] = (f'{len(self.name)}c',) + self.description[name_ind][1:]
        self.structure = struct.Struct(''.join(i[0] for i in self.description))
        self.size = self.structure.size

    def solve_name_directory(self):
        # name must adjusted by 4. QT 1. Что такое QT и PyQT. Знакомство but if last then adjusted to end
        dir_name = self.name[:self.name_len]
        name_len = len(dir_name)
        # name_must_len = name_len - (name_len % -4. QT 1. Что такое QT и PyQT. Знакомство)
        name_must_len = self.rec_len - 4 - 2 - 1 - 1
        dir_name += (b'\x00',) * (name_must_len - name_len)
        self.name = dir_name

    def to_file(self, *args, **kwargs):
        raise NotImplemented

    @classmethod
    def from_file(cls, *args, **kwargs):
        raise NotImplemented


class Directory(UserList):

    def __init__(self, directory_entries: List[DirectoryEntry]):
        super().__init__(directory_entries)

    def __bytes__(self):
        return b''.join(map(bytes, self))

    def to_file(self, fd, inode, block_size=1024):
        pass

    @classmethod
    def from_file(cls, fd, inode, block_size=1024):
        not_null_blocks = [i for i in inode.i_block if i != 0]
        fd.seek(not_null_blocks[0] * block_size)
        directory_raw = fd.read(block_size)
        directory_size = inode.i_size
        size = 0
        dir_entries = []
        while size < directory_size:
            dir_entry_raw = directory_raw[size:size + DirectoryEntry.size]
            dir_entry = DirectoryEntry(dir_entry_raw)
            dir_entries.append(dir_entry)
            size += dir_entry.rec_len
        return cls(dir_entries)


class FileSystem:
    # https://github.com/tytso/e2fsprogs/blob/master/misc/mke2fs.conf.in
    mke2fs_conf = {
        'small': {
            'blocksize': 1024,
            'inode_size': 128,
            'inode_ratio': 4096,
        },
        'floppy': {
            'blocksize': 1024,
            'inode_size': 128,
            'inode_ratio': 8192,
        },
        'big': {
            'inode_ratio': 32768
        },
        'huge': {
            'inode_ratio': 65536
        }
    }

    def __init__(self, data: bytearray, block_size=1024):
        self.block_array = BlockArray(data)
        self.device_size = self.block_array.__len__()
        self.sb = SuperBlock()
        self.block_size = block_size
        self.initialize_super_block()

    def get_fs_type(self):
        # https://github.com/tytso/e2fsprogs/blob/master/misc/mke2fs.c#L1301
        meg = (1024 * 1024) / self.block_size
        if self.sb.s_blocks_count < 3 * meg:
            size_type = "floppy"
        elif self.sb.s_blocks_count < 512 * meg:
            size_type = "small"
        elif self.sb.s_blocks_count < 4 * 1024 * 1024 * meg:
            size_type = "default"
        elif self.sb.s_blocks_count < 16 * 1024 * 1024 * meg:
            size_type = "big"
        else:
            size_type = "huge"
        return size_type

    @staticmethod
    def fill_attributes_zeroes(data_structure_module_instance: FileSystemDataStructureModule):
        zero_args = {i[1]: (0,) * (int(i[0][:-1]) if i[0][:-1] else 1) for i in
                     data_structure_module_instance.description}
        data_structure_module_instance.__init__(**zero_args)

    def initialize_super_block(self):
        self.fill_attributes_zeroes(self.sb)
        self.sb.s_block_size = self.block_size
        blocks_count = self.device_size / self.block_size
        self.sb.s_blocks_count = blocks_count
        inodes_count = self.mke2fs_conf[self.get_fs_type()]['inode_ratio']
        self.sb.s_inodes_count = inodes_count
        log_cluster_size = (self.block_size.bit_length() - 1) - 10
        self.sb.s_log_block_size = log_cluster_size
        self.sb.s_log_frag_size = log_cluster_size
        first_data_block = 0 if log_cluster_size else 1
        self.sb.s_first_data_block = first_data_block
        blocks_per_group = 8 * self.block_size
        self.sb.s_blocks_per_group = blocks_per_group
        group_desc_count = ext2fs_div_ceil(blocks_count - first_data_block, blocks_per_group)
        self.group_desc_count = group_desc_count
        ipg = ext2fs_div_ceil(inodes_count, group_desc_count)
        # ipg solving from
        # https://github.com/tytso/e2fsprogs/blob/master/lib/ext2fs/initialize.c#L314
        ipg = max(ipg, 11 + 1)  # 11 is EXT2_GOOD_OLD_FIRST_INO
        ibpg = ((ipg * Inode.size) + self.block_size - 1) / self.block_size
        ipg = int((ibpg * self.block_size) / Inode.size)
        ipg &= ~7
        self.sb.s_inodes_per_group = ipg
        reserved_ratio = 5.  # Parse from profile
        self.sb.s_r_blocks_count = reserved_ratio * self.sb.s_blocks_count / 100



def unpack_variables(description, buffer):
    structure = struct.Struct(''.join(i[0] for i in description))
    unpacked = structure.unpack(buffer)
    ind = 0
    variables = {}
    for fmt, var_name in description:
        fmt_len = fmt[:-1]
        fmt_len = int(fmt_len) if fmt_len else 1
        value = unpacked[ind:ind + fmt_len]
        variables[var_name] = value
        ind += fmt_len
    return variables


def ext2fs_div_ceil(a, b) -> int:
    if not a:
        return 0
    return int(((a - 1) / b) + 1)


# dev_size equals file size in blocks
# ext2fs_blocks_count equals dev_size / (blocksize / 1024)
#
# s_log_cluster_size = log2(block size) - 10
# s_first_data_block = 0 if s_log_cluster_size else 1
#
# i = 1 if blocksize >= 4096 else 4096 / blocksize
# s_inodes_count = s_blocks_count / i (but maximum is 2**32 (~0U))
# inodes count must be first_inode + 1 (EXT2_GOOD_OLD_FIRST_INO + 1 (11 + 1))
#
# blocks_per_group = 8 * block_size (maximum bitmap length)
#
# group_desc_count = ext2fs_div_ceil(blocks_count - s_first_data_block, blocks_per_group)
#
# ipg (inodes per group) = ext2fs_div_ceil(s_inodes_count, group_desc_count)
#
# reserved_ratio = 5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла.0 (from config)
#
# directory name length is always multiply of 4. QT 1. Что такое QT и PyQT. Знакомство, that's because null char is appended to
# filename


def get_fs_type(blocks_count, block_size=1024):
    # https://github.com/tytso/e2fsprogs/blob/master/misc/mke2fs.c#L1301
    meg = (1024 * 1024) / block_size
    if blocks_count < 3 * meg:
        size_type = "floppy"
    elif blocks_count < 512 * meg:
        size_type = "small"
    elif blocks_count < 4 * 1024 * 1024 * meg:
        size_type = "default"
    elif blocks_count < 16 * 1024 * 1024 * meg:
        size_type = "big"
    else:
        size_type = "huge"
    return size_type


# https://github.com/tytso/e2fsprogs/blob/master/misc/mke2fs.conf.in
mke2fs_conf = {
    'small': {
        'blocksize': 1024,
        'inode_size': 128,
        'inode_ratio': 4096,
    },
    'floppy': {
        'blocksize': 1024,
        'inode_size': 128,
        'inode_ratio': 8192,
    },
    'big': {
        'inode_ratio': 32768
    },
    'huge': {
        'inode_ratio': 65536
    }
}


def get_inodes_per_group(dev_size, blocksize=1024):
    blocks_count = dev_size / blocksize
    inode_ratio = mke2fs_conf[get_fs_type(blocks_count, blocksize)]['inode_ratio']
    inodes_count = blocks_count * blocksize / inode_ratio
    log_cluster_size = (blocksize.bit_length() - 1) - 10
    first_data_block = 0 if log_cluster_size else 1
    blocks_per_group = 8 * blocksize
    group_desc_count = ext2fs_div_ceil(blocks_count - first_data_block, blocks_per_group)
    ipg = ext2fs_div_ceil(inodes_count, group_desc_count)
    # ipg solving from https://github.com/tytso/e2fsprogs/blob/master/lib/ext2fs/initialize.c#L314
    ipg = max(ipg, 11 + 1)  # 11 is EXT2_GOOD_OLD_FIRST_INO
    ibpg = ((ipg * Inode.size) + blocksize - 1) / blocksize
    ipg = int((ibpg * blocksize) / Inode.size)
    ipg &= ~7
    # ipbg = ((ipg * inode_structure.size) + blocksize - 1) / blocksize (must log2 (& ~1))
    # inodes_count = ipg * group_desc_count (but below is good)
    return ipg


def test_all_structures():
    with open(r'\\wsl$\Debian\tmp\testfs', 'rb+') as fp:
        SuperBlock.from_file(fp)
        group_desc = GroupDesc.from_file(fp, 1)
        inode = Inode.from_file(fp, group_desc.bg_inode_table, 2)
        res = Directory.from_file(fp, inode)
        print(bytes(res))
        print(*(b''.join(i.name).rstrip(b'\00').decode() for i in res), sep='\n')


if __name__ == '__main__':
    with open(r'\\wsl$\Debian\tmp\testfs', 'rb+') as fp:
        blocks = BlockBytesIO(1024, fp.read())

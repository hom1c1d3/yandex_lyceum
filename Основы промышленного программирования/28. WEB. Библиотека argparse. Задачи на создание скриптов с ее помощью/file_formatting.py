import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        fd = open(file_name, 'r', encoding='utf8')
    except Exception as e:
        return e
    text_block = ''
    line = ''
    line_len = 0
    block_height = 0
    is_line_formatted = False
    while True:
        i = fd.read(1)
        if i == '':
            text_block += line
            break
        if i == '\n' and is_line_formatted:
            is_line_formatted = False
            continue
        is_line_formatted = False
        line += i
        line_len += 1
        if i == '\n' or line_len == frame_width:
            if i != '\n':
                line += '\n'
                is_line_formatted = True
            text_block += line
            line = ''
            line_len = 0
            block_height += 1
        if block_height == frame_height:
            break
    fd.close()
    return text_block.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int)
    parser.add_argument('--frame-width', type=int)
    parser.add_argument('filename')
    args = parser.parse_args()
    formatted_block = format_text_block(args.frame_height, args.frame_width, args.filename)
    print(formatted_block)


if __name__ == '__main__':
    main()

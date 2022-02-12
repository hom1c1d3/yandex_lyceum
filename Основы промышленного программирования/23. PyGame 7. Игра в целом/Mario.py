import os
import sys
import pygame

pygame.init()
pygame.key.set_repeat(200, 70)
FPS = 50
WIDTH = 500
HEIGHT = 500
STEP = 10
clock = pygame.time.Clock()
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()



def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    intro_text = ["Заставка",
                  "",
                  "Правила игры",
                  "Если в правилах несколько строк",
                  "приходится выводить их построчно"]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 60
    for line in intro_text:
        string_render = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_render.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = 10
        screen.blit(string_render, intro_rect)
        text_coord += intro_rect.height + 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)




def load_level(filename):
    filename = filename
    try:
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
    except Exception:
        print(f'файл с именем {filename} не найден')
        exit()
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               title_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15,
                                               title_height * pos_y + 5)
        self.move_cam = 0
        self.x = self.rect.x // tile_width
        self.y = self.rect.y // title_height

    def move(self, step):
        global map_
        try:
            if step == 1:
                if map_[self.y][self.x - 1] != '#':
                    self.move_cam = 1
                    self.rect.x -= tile_width
                    for sprite in all_sprites:
                        if sprite.rect.x == w - 50:
                            sprite.rect.x = -50
                    for i in range(len(map_)):
                        map_[i] = map_[i][-1] + map_[i][:-1]
                        map_[i] = map_[i].replace('@', '.')
                    map_[self.y] = map_[self.y][:self.x] + '@' + map_[self.y][self.x + 1:]
            if step == 2:
                if map_[self.y][self.x + 1] != '#':
                    self.move_cam = 1
                    self.rect.x += tile_width
                    for sprite in all_sprites:
                        if sprite.rect.x == 0:
                            sprite.rect.x = w
                    for i in range(len(map_)):
                        map_[i] = map_[i][1:] + map_[i][0]
                        map_[i] = map_[i].replace('@', '.')
                    map_[self.y] = map_[self.y][:self.x] + '@' + map_[self.y][self.x + 1:]
            if step == 3:
                if map_[self.y - 1][self.x] != '#':
                    self.move_cam = 1
                    self.rect.y -= title_height
                    for sprite in all_sprites:
                        if sprite.rect.y == h - 50:
                            sprite.rect.y = - 50
                    map_ = [map_[-1]] + map_[:-1]
                    for i in range(len(map_)):
                        map_[i] = map_[i].replace('@', '.')
                    map_[self.y] = map_[self.y][:self.x] + '@' + map_[self.y][self.x + 1:]
            if step == 4:
                if map_[self.y + 1][self.x] != '#':
                    self.move_cam = 1
                    self.rect.y += title_height
                    for sprite in all_sprites:
                        if sprite.rect.y == 0:
                            sprite.rect.y = h
                    map_ = map_[1:] + [map_[0]]
                    for i in range(len(map_)):
                        map_[i] = map_[i].replace('@', '.')
                    map_[self.y] = map_[self.y][:self.x] + '@' + map_[self.y][self.x + 1:]
        except Exception as e:
            pass


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            if level[y][x] == '#':
                Tile('wall', x, y)
            if level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


level = input('Введите имя файла с уровнем: ')
map_ = load_level('data/' + level)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')
tile_width = title_height = 50
player, level_x, level_y = generate_level(load_level('data/' + level))
start_screen()
w, h = len(map_) * tile_width, len(map_[0]) * title_height


# Главный Игровой цикл
running = True
while running:
    player.move_cam = 0
    WIDTH, HEIGHT = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(1)
            if event.key == pygame.K_RIGHT:
                player.move(2)
            if event.key == pygame.K_UP:
                player.move(3)
            if event.key == pygame.K_DOWN:
                player.move(4)
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    player, level_x, level_y = generate_level(map_)
    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
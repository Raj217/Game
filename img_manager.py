import pygame
import os
import game

def load_bgs(width, height):
    bgs = [pygame.transform.scale(pygame.image.load(os.path.join(f'assets/background/Backgrounds/game_background_{i}.png')), (width, height)) for i in range(1, 5)]
    bw_bgs = [pygame.transform.scale(pygame.image.load(os.path.join(f'assets/background/Backgrounds/game_background_{i}_BW.png')), (width, height)) for i in range(1, 5)]
    return bgs + bw_bgs

def load_tileset(width, height):
    tiles = pygame.transform.scale(pygame.image.load(os.path.join('assets/background/Tilesets/platform.png')), (width, height))
    return tiles

def load_menu(width, height):
    return pygame.transform.scale(pygame.image.load(os.path.join('assets/Menu/Menu/menu.png')), (width, height))

def load_info_menu(width, height):
    return [pygame.transform.scale(pygame.image.load(os.path.join(f'assets/Info/info1.png')), (width, height))]

def load_buttons():
    button_restart = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-restart_game.png'))
    button_exit_menu = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-exit_menu.png'))
    button_info = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-info.png'))
    button_open_menu = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-open_menu.png'))
    button_paused = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-paused.png'))
    button_play = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-play.png'))
    button_save = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-save.png'))
    button_selected = pygame.image.load(os.path.join(f'assets/Menu/Buttons/button-selected.png'))

    return button_restart, button_exit_menu, button_info, button_open_menu, button_paused, button_play, button_save, button_selected

def load_hero1():
    attack = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Knight/Attack/attack{i}.png')) for i in range(4)]
    attack_extra = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Knight/Attack_Extra/attack_extra{i}.png')) for i in range(1, 9)]
    bw = pygame.image.load(os.path.join('assets/heroes/Type1/Knight/BW/knight.png'))
    death = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Knight/Death/death{i}.png')) for i in range(1, 11)]
    hurt = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Knight/Hurt/hurt{i}.png')) for i in range(1, 5)]
    idle = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Knight/Idle/idle{i}.png')) for i in range(1, 13)]
    jump = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Knight/Jump/jump{i}.png')) for i in range(1, 8)]
    run = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Knight/Run/run{i}.png')) for i in range(1, 9)]
    stand = [pygame.image.load(os.path.join('assets/heroes/Type1/Knight/Stand/stand.png'))]
    coloured_img = pygame.image.load(os.path.join('assets/heroes/Type1/Knight/knight.png'))
    return attack, attack_extra, bw, death, hurt, idle, jump, run, stand, coloured_img

def load_hero2():
    attack = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Attack/attack{i}.png')) for i in range(1, 8)]
    attack_extra = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Attack_Extra/attack_extra{i}.png')) for i in range(6)]
    bw = pygame.image.load(os.path.join('assets/heroes/Type1/Mage/BW/mage.png'))
    death = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Death/death{i}.png')) for i in range(1, 11)]
    fire = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Fire/fire{i}.png')) for i in range(1, 10)]
    fire_extra = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Fire_Extra/fire_extra{i}.png')) for i in range(1, 10)]
    hurt = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Hurt/hurt{i}.png')) for i in range(1, 5)]
    idle = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Idle/idle{i}.png')) for i in range(1, 15)]
    jump = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Jump/jump{i}.png')) for i in range(1, 8)]
    run = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Mage/Run/run{i}.png')) for i in range(1, 9)]
    stand = [pygame.image.load(os.path.join('assets/heroes/Type1/Mage/Stand/stand.png'))]
    coloured_img = pygame.image.load(os.path.join('assets/heroes/Type1/Mage/mage.png'))
    return attack, attack_extra, bw, death, fire, fire_extra,  hurt, idle, jump, run,  stand, coloured_img

def load_hero3():
    attack = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Rogue/Attack/attack{i}.png')) for i in range(1, 8)]
    attack_extra = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Rogue/Attack_Extra/attack_extra{i}.png')) for i in range(1, 12)]
    bw = pygame.image.load(os.path.join('assets/heroes/Type1/Rogue/BW/rogue.png'))
    death = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Rogue/Death/death{i}.png')) for i in range(1, 11)]
    hurt = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Rogue/Hurt/hurt{i}.png')) for i in range(1, 5)]
    idle = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Rogue/Idle/idle{i}.png')) for i in range(1, 18)]
    jump = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Rogue/Jump/jump{i}.png')) for i in range(1, 8)]
    run = [pygame.image.load(os.path.join(f'assets/heroes/Type1/Rogue/Run/run{i}.png')) for i in range(1, 9)]
    stand = [pygame.image.load(os.path.join('assets/heroes/Type1/Rogue/Stand/stand.png'))]
    coloured_img = pygame.image.load(os.path.join('assets/heroes/Type1/Rogue/rogue.png'))
    return attack, attack_extra, bw, death, hurt, idle, jump, run, stand, coloured_img


def load_health_coins(width, height):
    imgs = [pygame.transform.scale(pygame.image.load(os.path.join(f'assets/Coins/health/health_{i}.png')), (width, height)) for i in range(5)]
    if game.DEVELOPER == 'Rajdristant Ghose':
        return imgs
    else:
        raise Exception

def load_money_coins(width, height):
    imgs = [pygame.transform.scale(pygame.image.load(os.path.join(f'assets/Coins/money/money_{i}.png')), (width, height)) for i in range(5)]
    return imgs

def load_special_attack_coins(width, height):
    imgs = [pygame.transform.scale(pygame.image.load(os.path.join(f'assets/Coins/special_attack/special_attack_{i}.png')), (width, height)) for i in range(5)]
    return imgs

def load_enemy1(width, height):
    attack = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/1/1_enemies_1_attack_0{i}.png')), (width, height)), True, False) for i in range(20)]
    die = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/1/1_enemies_1_die_0{i}.png')), (width, height)), True, False) for i in range(20)]
    hurt = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/1/1_enemies_1_hurt_0{i}.png')), (width, height)), True, False) for i in range(20)]
    walk = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/1/1_enemies_1_walk_0{i}.png')), (width, height)), True, False) for i in range(20)]

    return attack, die, hurt, walk

def load_enemy2(width, height):
    attack = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/5/5_enemies_1_attack_0{i}.png')), (width, height)), True, False) for i in range(20)]
    die = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/5/5_enemies_1_die_0{i}.png')), (width, height)), True, False) for i in range(20)]
    hurt = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/5/5_enemies_1_hurt_0{i}.png')), (width, height)), True, False) for i in range(20)]
    walk = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/5/5_enemies_1_walk_0{i}.png')), (width, height)), True, False) for i in range(20)]

    return attack, die, hurt, walk

def load_enemy5(width, height):
    attack = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/6/6_enemies_1_attack_0{i}.png')), (width, height)), True, False) for i in range(20)]
    die = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/6/6_enemies_1_die_0{i}.png')), (width, height)), True, False) for i in range(20)]
    hurt = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/6/6_enemies_1_hurt_0{i}.png')), (width, height)), True, False) for i in range(20)]
    walk = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/6/6_enemies_1_walk_0{i}.png')), (width, height)), True, False) for i in range(20)]

    return attack, die, hurt, walk

def load_enemy6(width, height):
    attack = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/7/7_enemies_1_attack_0{i}.png')), (width, height)), True, False) for i in range(20)]
    die = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/7/7_enemies_1_die_0{i}.png')), (width, height)), True, False) for i in range(20)]
    hurt = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/7/7_enemies_1_hurt_0{i}.png')), (width, height)), True, False) for i in range(20)]
    walk = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/7/7_enemies_1_walk_0{i}.png')), (width, height)), True, False) for i in range(20)]

    return attack, die, hurt, walk

def load_enemy4(width, height):
    attack = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/9/9_enemies_1_attack_0{i}.png')), (width, height)), True, False) for i in range(20)]
    die = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/9/9_enemies_1_die_0{i}.png')), (width, height)), True, False) for i in range(20)]
    hurt = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/9/9_enemies_1_hurt_0{i}.png')), (width, height)), True, False) for i in range(20)]
    walk = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/9/9_enemies_1_walk_0{i}.png')), (width, height)), True, False) for i in range(20)]

    return attack, die, hurt, walk

def load_enemy3(width, height):
    attack = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/10/10_enemies_1_attack_0{i}.png')), (width, height)), True, False) for i in range(20)]
    die = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/10/10_enemies_1_die_0{i}.png')), (width, height)), True, False) for i in range(20)]
    hurt = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/10/10_enemies_1_hurt_0{i}.png')), (width, height)), True, False) for i in range(20)]
    walk = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(f'assets/enemies/10/10_enemies_1_walk_0{i}.png')), (width, height)), True, False) for i in range(20)]

    return attack, die, hurt, walk

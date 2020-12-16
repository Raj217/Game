import pygame
import img_manager
import random
import pandas as pd
from tkinter import messagebox
import tkinter


"""
Die Problem of knight
"""
class Game:
    def __init__(self):
        # ----------------- Info WIN -------------------
        self.root = tkinter.Tk()
        self.root.geometry("1x1")
        self.root.withdraw()

        # ----------------- Main WIN -------------------
        self.width = 970
        self.height = int(self.width // 1.709)  # 1.709 is the aspect ratio
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Heroic Heist')
        self.clock = pygame.time.Clock()

        # ----------------- Backgrounds -------------------
        self.bg1, self.bg2, self.bg3, self.bg4, self.bg1_bw, self.bg2_bw, self.bg3_bw, self.bg4_bw = img_manager.load_bgs(self.width, self.height)

        self.bg_coloured = [self.bg1, self.bg2, self.bg3, self.bg4]
        self.bg_bw = [self.bg1_bw, self.bg2_bw, self.bg3_bw, self.bg4_bw]

        self.curr_bg = 0
        self.menu = False
        self.menu_info = False

        # ----------------- Menu -------------------
        self.menu_img = img_manager.load_menu(830, 450)

        # ----------------- Info Menu -------------------
        self.info = img_manager.load_info_menu(self.width, self.height)

        # ----------------- Platform -------------------
        self.platform1 = img_manager.load_tileset(self.width, int(self.height // 4))
        self.platform2 = img_manager.load_tileset(self.width, int(self.height // 4))
        self.platform_height = 60
        self.platform1_x = 0

        # ----------------- Buttons -----------------
        self.buttons = img_manager.load_buttons()
        self.button_restart_game, self.button_exit_menu, self.button_info, self.button_open_menu, self.button_paused, self.button_play, self.button_save, self.button_selected = self.buttons

        self.width_button_info = 35
        self.width_button_restart = 47
        self.width_button_open_menu = 48
        self.width_button_paused = 38
        self.width_button_save = 38
        self.width_button_selected = 32
        self.width_button_exit_menu = 53

        self.button_info = pygame.transform.scale(self.button_info, (self.width_button_info, int(self.width_button_info*(160/142))))
        self.button_restart_game = pygame.transform.scale(self.button_restart_game, (self.width_button_restart, int(self.width_button_restart*(160/142))))
        self.button_open_menu = pygame.transform.scale(self.button_open_menu, (self.width_button_open_menu, int(self.width_button_open_menu * (160 / 142))))
        self.button_paused = pygame.transform.scale(self.button_paused, (self.width_button_paused, int(self.width_button_paused * (160 / 142))))
        self.button_save = pygame.transform.scale(self.button_save, (self.width_button_save, int(self.width_button_save * (160 / 142))))
        self.button_selected = pygame.transform.scale(self.button_selected, (self.width_button_selected, int(self.width_button_selected*(160/142))))
        self.button_exit_menu = pygame.transform.scale(self.button_exit_menu, (self.width_button_exit_menu, int(self.width_button_exit_menu*(130/142))))

        # ------------------- Read Today -------------------
        # self.game_info
        self.read_data()

        # ------------------- Hero Info -------------------
        self.hero_money_pts = int(self.game_info.loc['coins'])
        self.hero_health_pts = int(self.game_info.loc['health'])
        self.hero_special_attack_pts = int(self.game_info.loc['special_attack'])
        self.herot1_height = 160
        self.hero_anim_count = 0
        self.herot1_anim_slower = 3
        self.hero_anim_slower_const = self.herot1_anim_slower
        self.var_hero_run = False       # platform running
        self.hero_change_dirn = False
        self.hero_x = 100
        self.hero_y_var = self.height - self.herot1_height
        self.hero_speed = 4
        self.hero_run_bool = False      # actual hero running
        self.hero_jump = False
        self.hero_jump_up_speed = 12
        self.hero_jump_down_speed = self.hero_jump_up_speed//2
        self.hero_attack = False
        self.hero_special_attack = False
        self.curr_hero = 0
        self.hero_lvl = int(self.game_info.loc['hero_level'])
        self.hero_enemy_encounter = False
        self.hero_health = int(self.game_info.loc['hero_health'])
        self.hero_attack_val = 5 + 5*(self.hero_lvl//15) + self.curr_hero*4
        self.hero_special_attack_val = 2*self.hero_attack_val
        self.hero_enemy_attack_bool = False
        self.fire_x = self.hero_x + 10
        self.fire_speed = 10


        # ------------------- Hero Images -----------------
        self.h1t1 = img_manager.load_hero1()
        self.h1t1_attack, self.h1t1_attack_extra, self.h1t1_bw, self.h1t1_death, self.h1t1_hurt, self.h1t1_idle, self.h1t1_jump, self.h1t1_run, self.h1t1_stand, self.h1t1_coloured_img = self.h1t1

        self.h2t1 = img_manager.load_hero2()
        self.h2t1_attack, self.h2t1_attack_extra, self.h2t1_bw, self.h2t1_death, self.h2t1_fire, self.h2t1_fire_extra, self.h2t1_hurt, self.h2t1_idle, self.h2t1_jump, self.h2t1_run, self.h2t1_stand, self.h2t1_coloured_img = self.h2t1

        self.h3t1 = img_manager.load_hero3()
        self.h3t1_attack, self.h3t1_attack_extra, self.h3t1_bw, self.h3t1_death, self.h3t1_hurt, self.h3t1_idle, self.h3t1_jump, self.h3t1_run, self.h3t1_stand, self.h3t1_coloured_img = self.h3t1

        self.hero_coloured_imgs = [self.h1t1_coloured_img, self.h2t1_coloured_img, self.h3t1_coloured_img]
        self.hero_bw_img = [self.h1t1_bw, self.h2t1_bw, self.h3t1_bw]

        # ------------------- Game States -------------------
        self.start_game = False

        # ------------------- Coins -------------------
        coin_width = 35
        coin_height = 35
        self.special_attack_coins = img_manager.load_special_attack_coins(coin_width, coin_height)
        self.money_coins = img_manager.load_money_coins(coin_width, coin_height)
        self.health_coins = img_manager.load_health_coins(coin_width, coin_height)


        # ------------------- Coin Info -------------------
        self.coin_anim_count = 0
        self.coin_anim_slower = 20
        self.coin_max_in_1_screen_ = random.choice([3]*30 + [4]*25 + [5]*10)
        self.coins = []
        self.coin_y = []
        self.coin_x = []
        self.coin_min_dist = 50

        # ------------------- Enemy Images -------------------
        enemy1 = img_manager.load_enemy1(68, 58)
        self.enemy1_attack, self.enemy1_die, self.enemy1_hurt, self.enemy1_walk = enemy1

        enemy2 = img_manager.load_enemy2(88, 78)
        self.enemy2_attack, self.enemy2_die, self.enemy2_hurt, self.enemy2_walk = enemy2

        enemy3 = img_manager.load_enemy3(88, 78)
        self.enemy3_attack, self.enemy3_die, self.enemy3_hurt, self.enemy3_walk = enemy3

        enemy4 = img_manager.load_enemy4(88, 78)
        self.enemy4_attack, self.enemy4_die, self.enemy4_hurt, self.enemy4_walk = enemy4

        enemy5 = img_manager.load_enemy5(98, 88)
        self.enemy5_attack, self.enemy5_die, self.enemy5_hurt, self.enemy5_walk = enemy5

        enemy6 = img_manager.load_enemy6(98, 88)
        self.enemy6_attack, self.enemy6_die, self.enemy6_hurt, self.enemy6_walk = enemy6


        # ------------------- Enemy Info -------------------
        self.enemies_walk = []
        self.enemies_attack = []
        self.enemies_die = []
        self.enemies_hurt = []
        self.enemy_anim_counts = []
        self.enemy_y = []
        self.enemy_x = []
        self.enemy_attack_strength = []
        self.enemy_idle = []
        self.enemy_health = []
        self.enemy_speed = 1
        self.enemy_max_in_1_screen_ = random.choice([2]*40+[1]*190+[3]*5)
        self.enemy_min_dist = 80
        self.enemy_choices = [self.enemy1_walk]
        self.enemy_walk_bool = []
        self.enemy_pause = False
        self.enemies_killed = int(self.game_info.loc['enemies_killed'])
        self.enemy_health_multiplier = 45


    def read_data(self):
        game_info = {}
        with open('dataset/data.csv', 'r') as open_file:
            data = [i.strip('\n').split(',') for i in open_file.readlines()]
        for datum in data:
            game_info[datum[0]] = datum[1]

        self.game_info = pd.DataFrame(data=game_info.values(), index=game_info.keys())


    def run(self):
        crashed = False
        pygame.key.set_repeat(10, 10)

        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos_x_left = self.width//2-120
                    pos_x_right = self.width//2-120 + 238
                    pos_y_up = self.height//4
                    pos_y_bottom = self.height//4+266

                    if pos_x_left < pos[0] < pos_x_right and pos_y_up < pos[1] < pos_y_bottom and not self.start_game:
                        self.start_game = True
                        self.hero_anim_count = 0

                    elif self.width-55 < pos[0] < self.width-55+self.width_button_open_menu and 6 < pos[1] < 6+int(self.width_button_open_menu*(160/142)) and self.start_game and not self.menu_info:
                        self.menu = True
                        self.met_button_open_menu()

                    elif self.width-95 < pos[0] < self.width-95+self.width_button_info and 10 < pos[1] < 10+int(self.width_button_info*(160/142)) and self.start_game:
                        self.menu_info = True
                        self.met_button_info()


                    elif self.width - 142 < pos[0] < self.width-142+self.width_button_restart and 6 < pos[1] < 6+int(self.width_button_restart*(160/142)) and self.start_game:
                        val = messagebox.askyesno('Restart', 'Delete all data and Restart game?')
                        if val:
                            self.met_button_restart()
                        else:
                            messagebox.showinfo('Error', 'Process withdrawn')

                    elif self.width - 187 < pos[0] < self.width-187+self.width_button_save and 10 < pos[1] < 10+int(self.width_button_save*(160/142)) and self.start_game:
                        self.met_button_save()
                        messagebox.showinfo('Save', 'Game Saved Successfully')

                    elif self.width - 232 < pos[0] < self.width-232+self.width_button_paused and 10 < pos[1] < 10+int(self.width_button_paused*(160/142)) and self.start_game:
                        self.met_button_paused()

                    elif self.width-150 < pos[0] < self.width-150+self.width_button_exit_menu and 100 < pos[1] < 100+int(self.width_button_exit_menu*(130/142)) and self.menu:
                        self.menu = False

                    elif self.width-60 < pos[0] < self.width-60+self.width_button_info and 25 < pos[1] < 25+int(self.width_button_info*(160/142)) and self.menu_info:
                        self.menu_info = False

                    elif self.menu and 150 < pos[0] < 150+128 and 238-128 < pos[1] < 238:
                        if self.check_purchase_validity(0, 'hero'):
                            self.curr_hero = 0

                    elif self.menu and 250 < pos[0] < 250+128 and 238-128 < pos[1] < 238:
                        if self.check_purchase_validity(1, 'hero'):
                            self.curr_hero = 1
                        else:
                            if self.check_buy(1, 'hero'):
                                val = messagebox.askyesno("Purchase", "Confirm Purchase?")
                                if val is True:
                                    self.game_info.loc['hero_purchased'] += '1'
                                    self.hero_money_pts -= 150
                                    messagebox.showinfo('Purchased', 'Mage PURCHASED!')
                                else:
                                    messagebox.showinfo('Purchased', 'Mage purchase cancelled!')
                            else:
                                messagebox.showerror("Error", "Not Enough Money")

                    elif self.menu and 350 < pos[0] < 350+128 and 238-128 < pos[1] < 238:
                        if self.check_purchase_validity(2, 'hero'):
                            self.curr_hero = 2
                        else:
                            if self.check_buy(2, 'hero'):
                                val = messagebox.askyesno("Purchase", "Confirm Purchase?")
                                if val is True:
                                    self.game_info.loc['hero_purchased'] += '2'
                                    self.hero_money_pts -= 300
                                    messagebox.showinfo('Purchased', 'Rogue PURCHASED!')
                                else:
                                    messagebox.showinfo('Purchased', 'Rogue purchase cancelled!')
                            else:
                                messagebox.showerror("Error", "Not Enough Money")

                    elif self.menu and 180 < pos[0] < 180+170 and 360 < pos[1] < 360+90:
                        if self.check_purchase_validity(0, 'bg'):
                            self.curr_bg = 0

                    elif self.menu and 350 < pos[0] < 350+170 and 360 < pos[1] < 360+90:
                        if self.check_purchase_validity(1, 'bg'):
                            self.curr_bg = 1
                        else:
                            if self.check_buy(1, 'bg'):
                                val = messagebox.askyesno("Purchase", "Confirm Purchase?")
                                if val is True:
                                    self.game_info.loc['bg_purchased'] += '1'
                                    self.hero_money_pts -= 50
                                    messagebox.showinfo('Purchased', 'Mountains(2) PURCHASED!')
                                else:
                                    messagebox.showinfo('Purchased', 'Mountains(2) purchase cancelled!')
                            else:
                                messagebox.showerror("Error", "Not Enough Money")

                    elif self.menu and 520 < pos[0] < 520+170 and 360 < pos[1] < 360+90:
                        if self.check_purchase_validity(2, 'bg'):
                            self.curr_bg = 2
                        else:
                            if self.check_buy(2, 'bg'):
                                val = messagebox.askyesno("Purchase", "Confirm Purchase?")
                                if val is True:
                                    self.game_info.loc['bg_purchased'] += '2'
                                    self.hero_money_pts -= 100
                                    messagebox.showinfo('Purchased', 'Forest(Night) PURCHASED!')
                                else:
                                    messagebox.showinfo('Purchased', 'Forest(Night) purchase cancelled!')
                            else:
                                messagebox.showerror("Error", "Not Enough Money")

                    elif self.menu and 690 < pos[0] < 690+170 and 360 < pos[1] < 360+90:
                        if self.check_purchase_validity(3, 'bg'):
                            self.curr_bg = 3
                        else:
                            if self.check_buy(1, 'bg'):
                                val = messagebox.askyesno("Purchase", "Confirm Purchase?")
                                if val is True:
                                    self.game_info.loc['bg_purchased'] += '3'
                                    self.hero_money_pts -= 150
                                    messagebox.showinfo('Purchased', 'Mountains(3) PURCHASED!')
                                else:
                                    messagebox.showinfo('Purchased', 'Mountains(3) purchase cancelled!')
                            else:
                                messagebox.showerror("Error", "Not Enough Money")


                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_d] and not self.hero_jump and not self.hero_enemy_encounter:
                        self.var_hero_run = True
                        if self.hero_change_dirn:
                            self.hero_change_dirn = False
                        if self.hero_x < 100:
                            self.hero_run_bool = True
                            self.hero_x += self.hero_speed
                        else:
                            self.hero_run_bool = False
                    elif key[pygame.K_a] and not self.hero_jump:
                        self.var_hero_run = True
                        self.hero_change_dirn = True
                        if -30 <= self.hero_x <= 100:
                            self.hero_run_bool = True
                            self.hero_x -= self.hero_speed
                    elif key[pygame.K_SPACE]:
                        if not self.hero_jump:
                            self.hero_anim_count = 0
                            self.hero_jump = True
                    elif key[pygame.K_e]:
                        if not self.hero_attack and not self.hero_special_attack and not self.hero_jump:
                            self.hero_attack = True
                            self.hero_anim_count = 0
                    elif key[pygame.K_q]:
                        if not self.hero_attack and not self.hero_special_attack and self.hero_special_attack_pts > 0 and not self.hero_jump:
                            self.hero_special_attack_pts -= 1
                            self.hero_special_attack = True
                            self.hero_anim_count = 0


                elif event.type == pygame.KEYUP:
                    self.var_hero_run = False
                    self.hero_run_bool = False



            self.draw()
        pygame.quit()

    def draw(self):
        if self.menu_info:
            self.met_button_info()
        elif self.menu:
            self.met_button_open_menu()
        else:
            self.draw_background()
            self.draw_platform()
            if not self.start_game:
                self.draw_start_game()
            else:

                self.met_buttons()
                self.display_coins()
                self.hero1_actions()
                self.spawn_coins()
                self.collide_hero_coin()
                self.spawn_enemies()
                self.hero_info()

        self.clock.tick(30)
        pygame.display.update()

    def draw_background(self):
        if self.curr_bg == 0:
            bg = self.bg1
        elif self.curr_bg == 1:
            bg = self.bg2
        elif self.curr_bg == 2:
            bg = self.bg3
        elif self.curr_bg == 3:
            bg = self.bg4

        self.win.blit(bg, (0, 0 - self.platform_height + 25))

    def draw_platform(self):
        platform_height = self.height - self.platform_height
        if self.start_game and self.var_hero_run and not self.hero_change_dirn and not self.hero_run_bool and not self.hero_enemy_encounter and False not in self.enemy_walk_bool:
            self.platform1_x -= self.hero_speed
            if self.width+self.platform1_x <= 0:
                self.platform1_x = 0

        self.win.blit(self.platform1, (self.platform1_x, platform_height))
        self.win.blit(self.platform2, (self.platform1_x + self.width, platform_height))

    def draw_start_game(self):
        if not self.start_game:
            self.win.blit(pygame.transform.scale2x(self.button_play), (self.width//2-120, self.height//4))
            if self.curr_hero == 0:
                self.draw_hero(self.h1t1_idle, 'attack')
            elif self.curr_hero == 1:
                self.draw_hero(self.h2t1_idle, 'attack')
            elif self.curr_hero == 2:
                self.draw_hero(self.h3t1_idle, 'attack')

    def draw_hero(self, imgs, extra_info=None, extra_imgs=None):

        self.hero_anim_count += 1
        if self.hero_anim_count//self.herot1_anim_slower >= len(imgs):
            self.hero_anim_count = 0
            if extra_info == 'jump':
                self.hero_jump = False
            elif extra_info == 'attack':
                self.hero_attack = False
            elif extra_info == 'special attack':
                self.hero_special_attack = False
            elif extra_info == 'hurt':
                self.herot1_anim_slower = 9
            elif extra_info == 'die':
                self.enemy_pause = False
                self.hero_enemy_encounter = False
                self.hero_health = 100
                self.hero_regen()
            else:
                self.fire_x = self.hero_x + 10

        if extra_info != 'hurt':
            self.herot1_anim_slower = 3


        if extra_imgs is not None:
            extra_img = extra_imgs[self.hero_anim_count // self.herot1_anim_slower]

        img = imgs[self.hero_anim_count // self.herot1_anim_slower]
        if self.hero_change_dirn:
            img = pygame.transform.flip(img, True, False)
            if extra_imgs is not None:
                extra_img = pygame.transform.flip(extra_img, True, False)

        if 0 < self.hero_anim_count//self.herot1_anim_slower < 3 and extra_info == 'jump':
            self.hero_y_var -= self.hero_jump_up_speed
        elif 3 <= self.hero_anim_count//self.herot1_anim_slower and extra_info == 'jump':
            self.hero_y_var += self.hero_jump_down_speed

        self.win.blit(img, (self.hero_x, self.hero_y_var))
        if extra_imgs is not None:
            if extra_info == 'special attack':
                self.win.blit(extra_img, (self.fire_x+10, self.height - self.herot1_height))
            else:
                self.win.blit(extra_img, (self.fire_x+50, self.height-self.herot1_height+45))

    def hero1_actions(self):
        if self.hero_jump:
            self.herot1_anim_slower = self.hero_anim_slower_const
            if self.curr_hero == 0:
                self.draw_hero(self.h1t1_jump, 'jump')
            elif self.curr_hero == 1:
                self.draw_hero(self.h2t1_jump, 'jump')
            elif self.curr_hero == 2:
                self.draw_hero(self.h3t1_jump, 'jump')

        elif self.enemy_pause:
            self.hero_x = 80
            if self.curr_hero == 0:
                self.draw_hero(self.h1t1_death, 'die')
            elif self.curr_hero == 1:
                self.draw_hero(self.h2t1_death, 'die')
            elif self.curr_hero == 2:
                self.draw_hero(self.h3t1_death, 'die')
        elif self.var_hero_run:
            if self.curr_hero == 0:
                self.draw_hero(self.h1t1_run)
            elif self.curr_hero == 1:
                self.draw_hero(self.h2t1_run)
            elif self.curr_hero == 2:
                self.draw_hero(self.h3t1_run)
        elif self.hero_attack or self.hero_special_attack:
                if not self.var_hero_run or not self.hero_run_bool:
                    if not self.hero_special_attack:
                        if self.curr_hero == 0:
                            self.draw_hero(self.h1t1_attack, 'attack')
                        elif self.curr_hero == 1:
                            self.draw_hero(self.h2t1_attack, 'attack', self.h2t1_fire)
                            self.fire_x += self.fire_speed
                        elif self.curr_hero == 2:
                            self.draw_hero(self.h3t1_attack, 'attack')
                    else:
                        if self.curr_hero == 0:
                            self.draw_hero(self.h1t1_attack_extra, 'special attack')
                        elif self.curr_hero == 1:
                            self.draw_hero(self.h2t1_attack_extra, 'special attack', self.h2t1_fire_extra)
                            self.fire_x += self.fire_speed
                        elif self.curr_hero == 2:
                            self.draw_hero(self.h3t1_attack_extra, 'special attack')


        elif self.hero_enemy_encounter or False in self.enemy_walk_bool:
            if self.curr_hero == 0:
                self.draw_hero(self.h1t1_hurt, 'hurt')
            elif self.curr_hero == 1:
                self.draw_hero(self.h2t1_hurt, 'hurt')
            elif self.curr_hero == 2:
                self.draw_hero(self.h3t1_hurt, 'hurt')
        else:
            if self.curr_hero == 0:
                self.draw_hero(self.h1t1_stand)
            elif self.curr_hero == 1:
                self.draw_hero(self.h2t1_stand)
            elif self.curr_hero == 2:
                self.draw_hero(self.h3t1_stand)


    def hero_info(self):
        if self.curr_bg == 2 or self.curr_bg == 3:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)

        self.text('HERO LEVEL: ', color, (109, 10), 'Aladin', 20)
        self.text(str(self.hero_lvl), color, (222, 10), 'Aladin', 20)

        self.text('HERO HEALTH: ', color, (109, 35), 'Aladin', 20)
        self.text(str(self.hero_health), color, (237, 35), 'Aladin', 20)

        self.text('ENEMY KILLED: ', color, (109, 60), 'Aladin', 20)
        self.text(str(self.enemies_killed), color, (252, 60), 'Aladin', 20)

        self.hero_level_update()
    # Below are collision functions for hero with coin and enemy

    def hero_level_update(self):
        if self.enemies_killed//10 + self.hero_money_pts//100 - self.hero_lvl > 0:
            self.hero_lvl += 1

        if self.hero_lvl >= 10:
            self.enemy_choices = [self.enemy1_walk, self.enemy2_walk]
        if self.hero_lvl >= 20:
            self.enemy_choices = [self.enemy1_walk, self.enemy2_walk, self.enemy3_walk]
        if self.hero_lvl >= 30:
            self.enemy_choices = [self.enemy1_walk, self.enemy2_walk, self.enemy3_walk, self.enemy4_walk]
        if self.hero_lvl >= 40:
            self.enemy_choices = [self.enemy1_walk, self.enemy2_walk, self.enemy3_walk, self.enemy4_walk, self.enemy5_walk]
        if self.hero_lvl >= 50:
            self.enemy_choices = [self.enemy1_walk, self.enemy2_walk, self.enemy3_walk, self.enemy4_walk, self.enemy5_walk, self.enemy6_walk]




    def draw_coins(self, imgs, pos):
        self.coin_anim_count += 1
        if self.coin_anim_count // self.coin_anim_slower >= len(imgs):
            self.coin_anim_count = 0

        img = imgs[self.coin_anim_count//self.coin_anim_slower]
        self.win.blit(img, pos)

    def spawn_coins(self):
        while len(self.coin_x) < self.coin_max_in_1_screen_:
            self.coin_x.append(self.get_coin_rand_x())
            self.coin_y.append(self.get_coin_rand_y())
            coins = random.choice([self.money_coins] * 160 + [self.special_attack_coins] * 34 + [self.health_coins] * 4)
            self.coins.append(coins)

        ind = 0
        while ind < len(self.coin_x):
            self.draw_coins(self.coins[ind], (self.coin_x[ind], self.coin_y[ind]))
            if not self.hero_run_bool and self.var_hero_run and not self.hero_enemy_encounter and False not in self.enemy_walk_bool:
                self.coin_x[ind] -= self.hero_speed
            if self.coin_x[ind] < -40:
                self.coin_x.pop(ind)
                self.coin_y.pop(ind)
                self.coins.pop(ind)
                self.coin_max_in_1_screen_ = random.choice([2]*2 + [3] * 30 + [4] * 25 + [5] * 10)

            ind += 1

    def get_coin_rand_x(self):
        random_x = random.choice(range(self.width, 2*self.width, self.coin_min_dist))
        while random_x in self.coin_x:
            random_x = random.choice(range(self.width, 2 * self.width, self.coin_min_dist))
        return random_x

    def get_coin_rand_y(self):
        random_y_adder = random.choice([0]*70 + [58]*30)
        random_y = self.height - 90 - random_y_adder
        return random_y

    def collide_hero_coin(self):
        ind = 0
        while ind < len(self.coin_x):
            if self.modulus(self.coin_x[ind]-self.hero_x) <= 50:
                if self.coin_y[ind] == self.height-90-58:
                    if self.hero_jump:
                        self.coin_x.pop(ind)
                        self.coin_y.pop(ind)
                        if self.coins[ind] == self.money_coins:
                            self.hero_money_pts += 1
                        elif self.coins[ind] == self.health_coins:
                            self.hero_health_pts += 1
                        elif self.coins[ind] == self.special_attack_coins:
                            self.hero_special_attack_pts += 1

                        self.coins.pop(ind)
                        continue
                else:
                    if not self.hero_jump:
                        self.coin_x.pop(ind)
                        self.coin_y.pop(ind)
                        if self.coins[ind] == self.money_coins:
                            self.hero_money_pts += 1
                        elif self.coins[ind] == self.health_coins:
                            self.hero_health_pts += 1
                        elif self.coins[ind] == self.special_attack_coins:
                            self.hero_special_attack_pts += 1
                        self.coins.pop(ind)
                        continue
            ind += 1

    def display_coins(self):

        self.win.blit(self.money_coins[3], (10, 10))
        self.win.blit(self.special_attack_coins[3], (10, 50))
        self.win.blit(self.health_coins[3], (10, 90))

        if self.curr_bg == 2 or self.curr_bg == 3:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        self.text(f'x{self.hero_money_pts}', color, (46, 9), 'Aladin')
        self.text(f'x{self.hero_special_attack_pts}', color, (46, 49), 'Aladin')
        self.text(f'x{self.hero_health_pts}', color, (46, 89), 'Aladin')

    def text(self, text, color, pos, font='ToonTime', size=30):
        if font == 'ToonTime':
            font = pygame.font.Font('assets/Fonts/ToonTime/SFToontime.ttf', size)
        elif font == 'Oswald':
            font = pygame.font.Font('assets/Fonts/Oswald/Oswald-SemiBold.ttf', size)
        elif font == 'Aladin':
            font = pygame.font.Font('assets/Fonts/Aladin/Aladin-Regular.ttf', size)

        text = font.render(text, True, color)
        self.win.blit(text, pos)

    def modulus(self, num):
        if num < 0:
            return -1*num
        else:
            return num

    def spawn_enemies(self):

        while len(self.enemy_x) < self.enemy_max_in_1_screen_:
            self.enemy_x.append(self.get_enemy_rand_x())
            enemy = random.choice(range(1, len(self.enemy_choices)+1))

            if enemy == 1:
                self.enemies_walk.append(self.enemy1_walk)
                self.enemies_die.append(self.enemy1_die)
                self.enemies_hurt.append(self.enemy1_hurt)
                self.enemies_attack.append(self.enemy1_attack)
                self.enemy_y.append(self.height - 104)
                self.enemy_attack_strength.append(5)
                self.enemy_health.append(5*self.enemy_health_multiplier)
            elif enemy == 2:
                self.enemies_walk.append(self.enemy2_walk)
                self.enemies_die.append(self.enemy2_die)
                self.enemies_hurt.append(self.enemy2_hurt)
                self.enemies_attack.append(self.enemy2_attack)
                self.enemy_y.append(self.height-121)
                self.enemy_attack_strength.append(10)
                self.enemy_health.append(10*self.enemy_health_multiplier)
            elif enemy == 3:
                self.enemies_walk.append(self.enemy3_walk)
                self.enemies_die.append(self.enemy3_die)
                self.enemies_hurt.append(self.enemy3_hurt)
                self.enemies_attack.append(self.enemy3_attack)
                self.enemy_y.append(self.height-125)
                self.enemy_attack_strength.append(15)
                self.enemy_health.append(15*self.enemy_health_multiplier)
            elif enemy == 4:
                self.enemies_walk.append(self.enemy4_walk)
                self.enemies_die.append(self.enemy4_die)
                self.enemies_hurt.append(self.enemy4_hurt)
                self.enemies_attack.append(self.enemy4_attack)
                self.enemy_y.append(self.height-124)
                self.enemy_attack_strength.append(20)
                self.enemy_health.append(25*self.enemy_health_multiplier)
            elif enemy == 5:
                self.enemies_walk.append(self.enemy5_walk)
                self.enemies_die.append(self.enemy5_die)
                self.enemies_hurt.append(self.enemy5_hurt)
                self.enemies_attack.append(self.enemy5_attack)
                self.enemy_y.append(self.height-130)
                self.enemy_attack_strength.append(25)
                self.enemy_health.append(35*self.enemy_health_multiplier)
            elif enemy == 6:
                self.enemies_walk.append(self.enemy6_walk)
                self.enemies_die.append(self.enemy6_die)
                self.enemies_hurt.append(self.enemy6_hurt)
                self.enemies_attack.append(self.enemy6_attack)
                self.enemy_y.append(self.height-131)
                self.enemy_attack_strength.append(30)
                self.enemy_health.append(50*self.enemy_health_multiplier)

            self.enemy_anim_counts.append(0)
            self.enemy_walk_bool.append(True)

        ind = 0
        while ind < len(self.enemies_walk):
            self.collide_hero_enemy(ind)

            if (self.hero_attack or self.hero_special_attack) and self.hero_enemy_attack_bool:
                if self.hero_attack:
                    self.enemy_health[ind] -= self.hero_attack_val
                else:
                    self.enemy_health[ind] -= self.hero_special_attack_val

                if self.enemy_health[ind] <= 0:
                    k = 0
                    while k < len(self.enemies_die[ind]):
                        self.win.blit(self.enemies_die[ind][int(k)],
                                      (self.enemy_x[ind], self.enemy_y[ind]))
                        k += 0.01
                    self.enemies_killed += 1
                    self.enemy_x.pop(ind)
                    self.enemy_anim_counts.pop(ind)
                    self.enemies_walk.pop(ind)
                    self.enemies_attack.pop(ind)
                    self.enemies_die.pop(ind)
                    self.enemies_hurt.pop(ind)
                    self.enemy_y.pop(ind)
                    self.enemy_attack_strength.pop(ind)
                    self.enemy_health.pop(ind)
                    self.enemy_max_in_1_screen_ = random.choice([1]*100+[2]*70+[3]*30)
                    self.enemy_walk_bool.pop(ind)
                    self.hero_enemy_encounter = False
                    self.spawn_enemies()
                    ind = 0

                self.draw_enemy(ind, self.enemies_hurt[ind])

            else:
                self.draw_enemy(ind)

            if self.enemy_walk_bool[ind]:
                if self.start_game and self.var_hero_run and not self.hero_change_dirn and not self.hero_run_bool and not self.hero_enemy_encounter and False not in self.enemy_walk_bool:
                    self.enemy_x[ind] -= self.enemy_speed + self.hero_speed
                else:
                    self.enemy_x[ind] -= self.enemy_speed

            if self.enemy_x[ind] < -80:
                self.enemy_x.pop(ind)
                self.enemy_anim_counts.pop(ind)
                self.enemies_walk.pop(ind)
                self.enemies_attack.pop(ind)
                self.enemies_die.pop(ind)
                self.enemies_hurt.pop(ind)
                self.enemy_y.pop(ind)
                self.enemy_attack_strength.pop(ind)
                self.enemy_health.pop(ind)
                self.enemy_max_in_1_screen_ = random.choice([1]*100 + [2] * 70 + [3] * 30)
                self.enemy_walk_bool.pop(ind)
            ind += 1


    def get_enemy_rand_x(self):
        choices = [i for i in range(self.width, 2 * self.width, self.enemy_min_dist)]
        random_x = random.choice(choices)
        while random_x in self.enemy_x:
            random_x = random.choice(choices)
        return random_x


    def draw_enemy(self, ind, imgs=None):
        self.enemy_anim_counts[ind] += 0.5
        if self.enemy_anim_counts[ind] >= len(self.enemies_walk[ind]):
            self.enemy_anim_counts[ind] = 0


        if imgs is None:
            if self.enemy_walk_bool[ind]:
                imgs = self.enemies_walk[ind]
            else:
                imgs = self.enemies_attack[ind]


        self.win.blit(imgs[int(self.enemy_anim_counts[ind])],
                      (self.enemy_x[ind], self.enemy_y[ind]))

    def collide_hero_enemy(self, ind):
        if self.modulus(self.enemy_x[ind]-self.hero_x) <= 80 and not self.hero_jump:
            self.hero_enemy_attack_bool = True
            if self.modulus(self.enemy_x[ind]-self.hero_x) <= 20:
                self.enemy_walk_bool[ind] = False
                self.hero_enemy_encounter = True

                if self.enemy_anim_counts[ind] == 14.0:
                    self.hero_health -= int(self.enemy_attack_strength[ind])
                if self.hero_health < 0:
                    temp = int(self.game_info.loc['health'])
                    self.hero_health_pts = str(temp-1)
                    self.enemy_pause = True

            else:
                self.enemy_walk_bool[ind] = True
                self.hero_enemy_encounter = False
        else:
            self.hero_enemy_attack_bool = False


        if self.curr_hero == 1:
            if self.modulus(self.enemy_x[ind]-self.fire_x)<=80 and not self.hero_jump:
                self.hero_enemy_attack_bool=True

    def met_buttons(self):
        self.win.blit(self.button_open_menu, (self.width - 55, 6))
        self.win.blit(self.button_info, (self.width-95, 10))
        self.win.blit(self.button_restart_game, (self.width - 142, 6))
        if self.start_game:
            self.win.blit(self.button_save, (self.width - 187, 10))
            self.win.blit(self.button_paused, (self.width-232, 10))


    def met_button_open_menu(self):
        width_screen = 150
        height_screen = int(width_screen//1.709)
        self.win.blit(self.bg4_bw, (0, 0))
        self.win.blit(self.menu_img, (70, 80))
        self.win.blit(self.button_exit_menu, (self.width-150, 100))

        bg_x = 180
        bg_y = 360
        bg_cost = 0
        for bg_ind in range(len(self.bg_coloured)):
            if self.check_purchase_validity(bg_ind, 'bg'):
                img = pygame.transform.scale(self.bg_coloured[bg_ind], (width_screen, height_screen))
            else:
                img = pygame.transform.scale(self.bg_bw[bg_ind], (width_screen, height_screen))
                self.text(str(bg_cost), (255, 255, 255), (bg_x+60, bg_y+100), 'Aladin', 20)
                self.win.blit(pygame.transform.scale(self.money_coins[3], (30, 30)), (bg_x+90, bg_y+95))
            self.win.blit(img, (bg_x, bg_y))
            if self.curr_bg == bg_ind:
                self.win.blit(self.button_selected, (bg_x+70, bg_y+90))
            bg_x += 170
            bg_cost += 50


        self.text('HEROES- ', (0, 0, 0), (150, 120), 'Aladin', 20)
        self.text('BACKGROUNDS- ', (0, 0, 0), (150, 310), 'Aladin', 20)

        self.text('Knight', (255, 255, 255), (175, 155), 'Oswald', 15)
        self.text('Mage', (255, 255, 255), (280, 155), 'Oswald', 15)
        self.text('Rogue', (255, 255, 255), (375, 155), 'Oswald', 15)

        self.text('Mountains(1)', (255, 255, 255), (220,  333), 'Oswald', 15)
        self.text('Mountains(2)', (255, 255, 255), (385, 333), 'Oswald', 15)
        self.text('Forest(Night)', (255, 255, 255), (555, 333), 'Oswald', 15)
        self.text('Mountains(3)', (255, 255, 255), (725, 333), 'Oswald', 15)

        hero_x = 150
        hero_y = 125
        hero_cost = 0
        for hero_ind in range(len(self.hero_coloured_imgs)):
            if self.check_purchase_validity(hero_ind, 'hero'):
                img = self.hero_coloured_imgs[hero_ind]
            else:
                img = self.hero_bw_img[hero_ind]
                self.text(str(hero_cost), (255, 255, 255), (hero_x+30, hero_y+120), 'Aladin', 20)
                self.win.blit(pygame.transform.scale(self.money_coins[3], (30, 30)), (hero_x+60, hero_y+117))
            self.win.blit(img, (hero_x, hero_y))
            if self.curr_hero == hero_ind:
                self.win.blit(self.button_selected, (hero_x+27, 238))
            hero_x += 100
            hero_cost += 150


    def check_purchase_validity(self, ind, type):
        if type == 'hero':
            if str(ind) in str(self.game_info.loc['hero_purchased']):
                return True
        elif type == 'bg':
            if str(ind) in str(self.game_info.loc['bg_purchased']):
                return True
        return False

    def check_buy(self, ind, type):
        if type == 'hero':
            if ind == 1:
                cost = 150
            elif ind == 2:
                cost = 300
        elif type == 'bg':
            if ind == 1:
                cost = 50
            elif ind == 2:
                cost = 100
            elif ind == 3:
                cost = 150

        if self.hero_money_pts >= cost:
            return True
        else:
            return False

    def met_button_info(self):
        self.win.blit(self.info[0], (0, 0))
        self.win.blit(self.button_exit_menu, (self.width-60, 25))


    def met_button_restart(self):
        game_info_restart = pd.DataFrame(data=[0, 0, 0, 3, 0, 0, 100, 0], index=['hero_purchased', 'bg_purchased', 'coins', 'health', 'special_attack', 'hero_level', 'hero_health', 'enemies_killed'])
        self.game_info = game_info_restart.copy()
        self.write_data()
        self.hero_regen()

    def met_button_paused(self):
        self.start_game = False


    def met_button_save(self):
        self.game_info.loc['coins'] = self.hero_money_pts
        self.game_info.loc['health'] = self.hero_health_pts
        self.game_info.loc['special_attack'] = self.hero_special_attack_pts
        self.game_info.loc['enemies_killed'] = self.enemies_killed
        self.write_data()


    def write_data(self):
        self.game_info.to_csv('dataset/data.csv')
        with open('dataset/data.csv', 'r') as open_file:
            data = [i.split('\n') for i in open_file.readlines()]
        data.pop(0)
        with open('dataset/data.csv', 'w') as open_file:
            for datum in data:
                open_file.write(datum[0]+'\n')

    def hero_regen(self):
        special_attack = self.hero_special_attack_pts
        health = self.hero_health_pts
        money = self.hero_money_pts
        self.__init__()
        self.hero_special_attack_pts = special_attack
        self.hero_health_pts = health
        self.hero_money_pts = money

import sys
import pygame
import SC_sprite


class Game(object):
    def __init__(self):
        # 创建屏幕
        width = 563   # 宽
        height = 560   # 高
        size = (width, height)
        self.screen = pygame.display.set_mode(size)

        # 创建背景精灵
        self.bg = SC_sprite.Background("./image/bg2.png")
        # 创建背景精灵组
        self.bg_Group = pygame.sprite.Group()
        # 将精灵添加进精灵组
        self.bg_Group.add(self.bg)

        # 创建否认按钮
        self.no = SC_sprite.Button_No("./image/no.jpg")
        # 创建精灵组
        self.no_Group = pygame.sprite.Group()
        # 将精灵添加进精灵组
        self.no_Group.add(self.no)

        # 创建确认按钮
        self.yes = SC_sprite.Button_Yes("./image/yes.jpg")
        # 创建精灵组
        self.yes_Group = pygame.sprite.Group()
        # 将精灵添加进精灵组
        self.yes_Group.add(self.yes)

        # 创建xin精灵组
        self.heart_Group = pygame.sprite.Group()

    def start_game(self):   # 进入游戏循环 开始游戏
        while True:
            # 事件监听
            self.event_Listening()

            # 刷新屏幕
            self.update_screen()


    def event_Listening(self):   # 事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
                # sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if (mouse_x >= self.yes.rect.x and mouse_x <= self.yes.rect.x + 169) and (mouse_y >= self.yes.rect.y and mouse_y <= self.yes.rect.y + 72):
                    sys.exit()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x >= self.yes.rect.x and mouse_x <= self.yes.rect.x + 169) and (mouse_y >= self.yes.rect.y and mouse_y <= self.yes.rect.y + 72):
                heart = SC_sprite.Heart("./image/heart.png")
                dm1 = SC_sprite.Heart("./image/dm1.png")
                dm2 = SC_sprite.Heart("./image/dm2.png")
                self.heart_Group.add(heart, dm1, dm2)

    def update_screen(self):   # 刷新屏幕
        # 背景
        self.bg_Group.update()
        self.bg_Group.draw(self.screen)  

        # 否认按钮
        self.no_Group.update()
        self.no_Group.draw(self.screen) 

        # 确认按钮
        self.yes_Group.update()
        self.yes_Group.draw(self.screen)

        # 心
        self.heart_Group.update()
        self.heart_Group.draw(self.screen)

        pygame.display.update()

if __name__ == '__main__':
    game  = Game()
    game.start_game()



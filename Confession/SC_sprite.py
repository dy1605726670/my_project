import pygame
import random
import sys

class Background(pygame.sprite.Sprite):
    ''' 背景精灵 '''
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)  
        self.rect =  self.image.get_rect()  

    def update(self):
        pass


class Button_No(pygame.sprite.Sprite):
    """按钮否"""
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)   # 获取图像
        self.rect = self.image.get_rect()   # 获取矩形区域对象
        self.rect.x = 60
        self.rect.y = 470

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if (mouse_x >= self.rect.x and mouse_x <= self.rect.x + 176) and (mouse_y >= self.rect.y and mouse_y <= self.rect.y + 72):
            if random.randint(1,9) % 2 == 0:
                self.rect.x += abs(self.rect.x - mouse_x)
                self.rect.y += abs(self.rect.y - mouse_y)
            else:
                self.rect.x -= abs(self.rect.x - mouse_x)
                self.rect.y -= abs(self.rect.y - mouse_y)

        if self.rect.x > 563-176 or self.rect.x < 0:
            self.rect.x = random.randint(1, 560)
        if self.rect.y > 560-72 or self.rect.y < 0:
            self.rect.y = random.randint(1, 560)


class Button_Yes(pygame.sprite.Sprite):
    """按钮是"""
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)   
        self.rect = self.image.get_rect() 
        self.rect.x = 350
        self.rect.y = 470
    
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.x >= mouse_x-80:
            self.rect.x -= 1
        if self.rect.x <= mouse_x-80:
            self.rect.x += 1
        if self.rect.y >= mouse_y-40:
            self.rect.y -= 1
        if self.rect.y <= mouse_y-40:
            self.rect.y += 1
        

class Heart(pygame.sprite.Sprite):
    """heart"""
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect()  
        self.rect.x = -50
        self.rect.y = random.randint(0, 500)

    def update(self):
        self.rect.x += random.randint(1, 4)
        if self.rect.x > 600:
            self.kill()
        
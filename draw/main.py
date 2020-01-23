import turtle as t
from sys import argv
from cv2 import imread
from cv2 import resize
from cv2 import INTER_CUBIC

def move(x,y):
    '''移动画笔'''
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw(image_path, adjustment=True):
    '''绘制'''
    img = imread(image_path)
    print(img.shape)   # 查看维度

    # 调整尺寸为200*200
    if adjustment:
        if img.shape[0] > 200 and img.shape[1] > 200:
            img = resize(img, (200,200), interpolation=INTER_CUBIC)

    t.screensize(img.shape[0]+200, img.shape[1]+200)

    move(-img.shape[0]//2,img.shape[1]//2)
    t.colormode(255) 
    t.speed(10)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            ls = [int(i) for i in img[x,y]]
            rgb = tuple(ls)

            t.pencolor(rgb[::-1])   # 注意反转 bgr 为 rgb
            t.fd(1)
        move(-img.shape[0]//2, (img.shape[1]//2)-x)

    t.done()


if __name__ == '__main__':
    draw(argv[1])
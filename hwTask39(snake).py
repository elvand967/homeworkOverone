# Домашнее задание Задача №39 (snake)
# игра змейка (заготовка overone)
# Продолжить разработку игры. Доработать еду для змейки (змейка увеличивается при поедании чего-нибудь)
# По желанию добавить:
# -Фон
# -Счётчик очков

import pygame
import random
pygame.init()

# словарь цветов (color_dictionary)
cd = {'red':(255,0,0), 'orange':(255,128,0),
                    'yellow':(255,255,0), 'green':(0,128,0),
                    'blue':(0,0,255),'violet':(238,130,238),
                    'black':(0,0,0),'white':(255,255,255),
                    'gray':(128,128,128),'cobaltgreen':(61,145,64),
                    'coldgrey':(128,138,135)}
W = 800  # ширина экрана
H = 500  # высота экрана

# определяем середину экрана виджета
# голову змеюки сюда
x = W // 2 # координаты по горизонтали
y = H // 2 # координаты по вертикали

l = 10     # ширина прямоугольника (квадрата) - елемента тела змейки
h = 10     # высота прямоугольника (квадрата) -/-
# При старте змейку соберу из 4-х элементов:
# - голова красного цвета (эффект открытия/закрытия рта, попробую обеспечить сменой
# закрашенного квадрата и рамки квадрата толщиной 2 px)
# - тело из трех квадратов (эффект движения усилить поочередной сменой заливки квадратов
# болотно-зеленым и  темно-серым цветами (cobaltgreen; coldgrey))
# Движение змейки исполнить сменой элементов координат списка тела змейки,
# добавлением нового элемента с координатами головы и удалением элемента с координатами хвоста
# + чередование цветов окраски
# Задумка: после поедания «кроликов» при дальнейшем движении, квадрат тела змейки на месте кролика
# увеличить на пару пикселей (как будто проходит по кишечнику),
# когда очередь дойдет до удаления хвоста на месте кролика (движение), его не удалять а вернуть
# к нормальному размеру, тем самым увеличив длину змейки.





# (!!! переделать исключающий цвет на кортеж цветов)функия генератор цветов, котороя в качестве аргументов принимает...
def f_color_generator(color_dictionary, exclude_color = None ): # словарь цветов и цвет который нужно исключить
    # словарь цветов (color_dictionary)
    # color_dictionary = {'red': (255, 0, 0), 'orange': (255, 128, 0),...}
    list_color = list(color_dictionary) # преобразуем наш словарь цветов в список ключей типа: ['red','orange',...]
    if exclude_color is not None:   # если указан цвет для искючения, в виде 'white'...
        list_color.remove(exclude_color)  # ... удалим его из списка
    shape_color = cd[random.choice(list_color)] # генерируем случайный цвет в виде кортежа, пример: (0, 128, 0)
    return shape_color # кортеж (..., ..., ...)




dis = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")

game_over = False

x1 = 300
y1 = 400

x1_change = 0
y1_change = 0

clock =pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True

            elif event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1>=800 or x1<0 or y1>=600 or y1<0:
        game_over = True

    x1+=x1_change
    y1+=y1_change
    dis.fill(cd['white'])

    pygame.draw.rect(dis, cd['red'], [x1,y1,10,10],2)
    pygame.display.update()

    clock.tick(30)



pygame = quit()
quit()
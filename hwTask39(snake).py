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
cd = {'red': (255, 0, 0), 'orange': (255, 128, 0),
      'yellow': (255, 255, 0), 'green': (0, 128, 0),
      'blue': (0, 0, 255), 'violet': (238, 130, 238),
      'black': (0, 0, 0), 'white': (255, 255, 255),
      'gray': (128, 128, 128), 'cobaltgreen': (61, 145, 64),
      'coldgrey': (128, 138, 135)}
W = 800  # ширина экрана
H = 500  # высота экрана

# определяем середину экрана виджета
# голову змеюки сюда
x = W // 2  # координаты по горизонтали
y = H // 2  # координаты по вертикали
x1_change = 0
y1_change = 0
l = 15  # ширина прямоугольника (квадрата) - елемента тела змейки
h = 15  # высота прямоугольника (квадрата) -/-
snake_mouth = [0, 3]  # 3- открыт, 0 - закрыт
f_start = False
snake_body_color = [cd['cobaltgreen'], cd['coldgrey']]
# При старте змейку соберу из 4-х элементов:
# - голова красного цвета (эффект открытия/закрытия рта, попробую обеспечить сменой
# закрашенного квадрата и рамки квадрата толщиной 3 px)
# - тело из трех квадратов (эффект движения усилить поочередной сменой заливки квадратов
# болотно-зеленым и  темно-серым цветами (cobaltgreen; coldgrey))
# Движение змейки исполнить сменой элементов координат списка тела змейки,
# добавлением нового элемента с координатами головы и удалением элемента с координатами хвоста
# + чередование цветов окраски
# Задумка: после поедания «кроликов» при дальнейшем движении, квадрат тела змейки на месте кролика
# увеличить на пару пикселей (как будто проходит по кишечнику),
# когда очередь дойдет до удаления хвоста на месте кролика (движение), его не удалять а вернуть
# к нормальному размеру, тем самым увеличив длину змейки.


# так-как list.append(x) добавляет новый элемент в конец списка, определимся,
# что элементы списка (наши составные части змейки) идут от хвоста к голове
list_snake = []
for i in range(-3, 1):
    list_snake.append([cd['red'], [x + (i * l), y, l, h]])
print(list_snake)


# (!!! переделать исключающий цвет на кортеж цветов)функия генератор цветов, котороя в качестве аргументов принимает...
def f_color_generator(color_dictionary, exclude_color=None):  # словарь цветов и цвет который нужно исключить
    # словарь цветов (color_dictionary)
    # color_dictionary = {'red': (255, 0, 0), 'orange': (255, 128, 0),...}
    list_color = list(color_dictionary)  # преобразуем наш словарь цветов в список ключей типа: ['red','orange',...]
    if exclude_color is not None:  # если указан цвет для искючения, в виде 'white'...
        list_color.remove(exclude_color)  # ... удалим его из списка
    shape_color = cd[random.choice(list_color)]  # генерируем случайный цвет в виде кортежа, пример: (0, 128, 0)
    return shape_color  # кортеж (..., ..., ...)


dis = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")

game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            f_start = True  # нажатие любой кнопки - старт игры
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_LEFT:
                x1_change = -l
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = l
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -h
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = h

    x += x1_change
    y += y1_change
    dis.fill(cd['white'])

    # pygame.draw.rect(dis, cd['red'], [x,y,10,10],2)
    if f_start:
        list_snake.append([cd['red'], [x, y, l, h]])
        list_snake.pop(0)

    # раскрасим змейку
    snake_body_color.reverse()
    for i in range(len(list_snake) - 1):
        if i % 2:
            list_snake[i][0] = snake_body_color[1]
        else:
            list_snake[i][0] = snake_body_color[0]

    # откроем/закроим ротик
    snake_mouth.reverse()

    pygame.draw.rect(dis, (230, 230, 250), [10, 30, W - 20, H - 40], 0)
    border = pygame.draw.rect(dis, cd['black'], [10, 30, W - 20, H - 40], 3)

    for i in range(len(list_snake)):
        if i == len(list_snake) - 1:
            snake = pygame.draw.rect(dis, list_snake[i][0], list_snake[i][1], snake_mouth[0])
            continue
        pygame.draw.rect(dis, list_snake[i][0], list_snake[i][1])

    # если голова змейки вышла за пределя границы (фигуры - 'border')
    if not pygame.Rect.contains(border, snake):
        game_over = True

    pygame.display.update()
    clock.tick(10)

pygame = quit()
quit()

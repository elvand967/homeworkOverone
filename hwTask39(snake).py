# Домашнее задание Задача №39 (snake)
# игра змейка (заготовка overone)
# Продолжить разработку игры. Доработать еду для змейки (змейка увеличивается при поедании чего-нибудь)
# По желанию добавить:
# -Фон
# -Счётчик очков

import sys
import pygame
import pygame as pg
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
cobaltgreen = (61, 145, 64)  # тело змейки
coldgrey = (128, 138, 135)  # тело змейки

# словарь цветов (rainbow - радуга)
rainbow = {'red': (255, 0, 0), 'orange': (255, 128, 0),
           'yellow': (255, 255, 0), 'green': (0, 128, 0),
           'blue': (0, 0, 255), 'violet': (238, 130, 238)}
L = 600  # ширина экрана
H = 600  # высота экрана

# определяем середину экрана виджета
# голову змеюки сюда
x = L // 2  # координаты по горизонтали
y = H // 2  # координаты по вертикали
x_change = 0
y_change = 0
l = 15  # ширина прямоугольника (квадрата) - елемента тела змейки
h = 15  # высота прямоугольника (квадрата) -/-
snake_mouth = rabbit_body = [0, l // 5]  # 3- открыт, 0 - закрыт
snake_body_color = [cobaltgreen, coldgrey]
rabbit_line = 0
n = 0  # счетчик тиков для кролика
f_rabbit = False  # Флаг кролика
total_rabbits = 0
cardionate_rabbit = ()
color_rabbit = ()
f_start = False

# При старте змейку соберу из 4-х элементов:
# - голова красного цвета (эффект открытия/закрытия рта, попробую обеспечить сменой
# закрашенного квадрата и рамки квадрата толщиной 3 px)
# - тело из трех квадратов (эффект движения усилить поочередной сменой заливки квадратов
# болотно-зеленым и  темно-серым цветами (cobaltgreen; coldgrey))
# Движение змейки исполнить сменой элементов координат списка тела змейки,
# добавлением нового элемента с координатами головы и удалением элемента с координатами хвоста
# + чередование цветов окраски

# так-как list.append(x) добавляет новый элемент в конец списка, определимся,
# что элементы списка (наши составные части змейки) идут от хвоста к голове
list_snake = []
for i in range(-3, 1):
    list_snake.append([rainbow['red'], [x + (i * l), y - 1, l, h]])


# функия генератор цветов, котороя в качестве аргументов принимает...
def fun_color_generator(color_dictionary):  # ...словарь цветов
    # color_dictionary =rainbow или {'red': (255, 0, 0), 'orange': (255, 128, 0),...}
    list_color = list(color_dictionary)  # преобразуем наш словарь цветов в список ключей типа: ['red','orange',...]
    shape_color = rainbow[random.choice(list_color)]  # генерируем случайный цвет в виде кортежа, пример: (0, 128, 0)
    return shape_color  # кортеж (..., ..., ...)


# функия генератор кардионат и размеров кролика и его цвета для передачи в pygame.draw.rect()
def fun_rabbit():
    l1 = random.randrange(l, L - l, l)
    h1 = random.randrange((4 * h), H - (4 * h), h)

    return [l1, h1, l, h]


dis = pygame.display.set_mode((L, H))
pygame.display.set_caption("Snake")



game_over = False

clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            f_start = True  # нажатие любой кнопки - старт игры
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT:
                x_change = -l
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = l
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -h
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = h

    dis.fill(white)
    pygame.draw.rect(dis, (196, 239, 228), [l, 3 * h, L - (2 * l), H - (4 * h)], 0)

    if not game_over:
        x += x_change
        y += y_change
    else:
        t1 = pygame.font.SysFont('arial', 48)
        txt1 = t1.render("Game over", True, rainbow['red'])
        dis.blit(txt1, (L // 2 - 100, H // 2 - 90))

    t2 = pygame.font.SysFont('arial', 16)
    txt2 = t2.render(f'Всего кроликов: {str(total_rabbits)}', True, rainbow['blue'])
    dis.blit(txt2, (l, h))


    if f_start:  # начинаем движение
        list_snake.append([rainbow['red'], [x, y, l, h]])
        if list_snake[0][1] == cardionate_rabbit:
            total_rabbits += 1 # посчитаем кролика
            f_rabbit = False
        else:
            list_snake.pop(0)

    # откроем/закроим ротик
    snake_mouth.reverse()

    # раскрасим змейку
    # snake_body_color.reverse() - не эфективно

    for i in range(len(list_snake) - 1):
        if i % 2:
            list_snake[i][0] = snake_body_color[1]
        else:
            list_snake[i][0] = snake_body_color[0]

    # граница поля
    border = pygame.draw.rect(dis, (35, 137, 111), [l, 3 * h, L - (2 * l), H - (4 * h)], 1)

    if not f_rabbit:  # если кролика еще нет
        cardionate_rabbit = fun_rabbit()  # генерируем ему новые кардионаты
        color_rabbit = fun_color_generator(rainbow)
        f_rabbit = True  # и даем добро на отрисовку
    else:
        # поморгаем кроликом
        n += 1
        if n == 3:
            rabbit_body.reverse()
            rabbit_line = rabbit_body[0]
            n = -3
        rabbit = pygame.draw.rect(dis, color_rabbit, cardionate_rabbit, rabbit_line)

    for i in range(len(list_snake)):
        if i == len(list_snake) - 1:
            snake = pygame.draw.rect(dis, list_snake[i][0], list_snake[i][1], snake_mouth[0])
            continue
        pygame.draw.rect(dis, list_snake[i][0], list_snake[i][1])


    # если голова змейки вышла за предел границы (фигуры - 'border')
    if not pygame.Rect.contains(border, snake):
        game_over = True

    pygame.display.update()
    clock.tick(10)

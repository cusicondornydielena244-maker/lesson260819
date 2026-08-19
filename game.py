import pygame
import random
# Инициализация всех модулей pygame
pygame.init()
# Создание окна размером 800x600 пикселей
screen = pygame.display.set_mode((800,600))
# Установка заголовка окна
pygame.display.set_caption("Моя игра")
running = True
x = 0
y = 50
clock = pygame.time.Clock()
FPS = 60
# Главный цикл программы
while running:


    # Обработка очереди событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


    #(0, 0, 0) — черный
    #(255, 255, 255) — белый
    #(255, 0, 0) — чисто красный
    #(0, 255, 0) — чисто зеленый
    #(0, 0, 255) — чисто синий


    # фон: очистка и заливка экрана цветом
    screen.fill((92, 224, 94))


    color1 = (0, 0, 255)
    #x = random.randint(0, 700)
    #y = random.randint(0, 550)
    x = x + 1
    if x > 799:
        x = 0
    rect_settings = (x,y,100,50)
    pygame.draw.rect(screen, color1, rect_settings)




    # 2. Круг (circle)
    # Параметры: поверхность, цвет (красный), (X центра, Y центра), радиус
    pygame.draw.circle(screen, (255, 0, 0), (400, 100), 60)


    # 3. Линия (line)
    # Параметры: поверхность, цвет (черный), начальная точка (X, Y), конечная точка (X, Y), толщина
    pygame.draw.line(screen, (0, 0, 0), (50, 220), (750, 220), 50)


    # 4. Эллипс (ellipse)
    # Рисуется внутри воображаемого прямоугольника. 
    # Параметры: поверхность, цвет (зеленый), (X, Y, ширина, высота описывающего прямоугольника)
    pygame.draw.ellipse(screen, (0, 200, 0), (50, 300, 200, 100))


    # 5. Многоугольник (polygon) - в данном случае треугольник
    # Параметры: поверхность, цвет (оранжевый), список координат углов [(X1, Y1), (X2, Y2), (X3, Y3)]
    pygame.draw.polygon(screen, (255, 165, 0), [(500, 300), (400, 450), (600, 450)])


    # Обновление экрана (отображение кадра)
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()

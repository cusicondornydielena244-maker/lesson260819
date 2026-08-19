import pygame
# Инициализация всех модулей pygame
pygame.init()
# Создание окна размером 800x600 пикселей
screen = pygame.display.set_mode((800,600))
# Установка заголовка окна
pygame.display.set_caption("Моя игра")
running = True
# Главный цикл программы
while running:


    # Обработка очереди событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


    # очистка и заливка экрана цветом
    screen.fill((92, 224, 94))


    # Обновление экрана (отображение кадра)
    pygame.display.flip()


pygame.quit()

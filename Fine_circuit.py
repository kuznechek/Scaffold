import pygame
from classes import *

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Виселица 1.2")
clock = pygame.time.Clock()

decorations = pygame.sprite.Group()
gameobjects = pygame.sprite.Group()

while True:
    clock.tick(FPS)

    #Спрайты декораций
    title = draw_decs(1, WIDTH / 2, 100)
    gameobjects.add(title)

    #Cпрайты игровых объектов
    for letter in draw_alphabet():
        gameobjects.add(letter)

    #Выбор слова
    words = get_content(0, None)
    choice = random.choice(words).split('\n')[0].upper()
    word = Word(choice, '_' * len(choice))
    print(word.full)

    while True:
        #Написать слово
        word.draw(decorations, a, b)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = Click(event.pos, 10)
                    click.draw(screen)
                    for obj in gameobjects:
                        if obj.check_collisions(event.pos) == True and obj.name in word.undiscovered:
                            word.update(obj.name)
                            obj.kill_me()
                            break
            # Рендеринг
            screen.fill(BLACK)
            decorations.draw(screen)
            gameobjects.draw(screen)
            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()
    break
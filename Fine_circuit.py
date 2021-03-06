import pygame
import time
from classes import *

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Виселица 1.2")
clock = pygame.time.Clock()

decorations_group = pygame.sprite.Group()
gameobjects_group = pygame.sprite.Group()
screamers_group = pygame.sprite.Group()

screamer = False

while True:
    clock.tick(FPS)

    #Спрайты декораций
    #title = draw_decs(1, WIDTH / 2, 100)
    #decorations.add(title)
    scr_im = draw_decs(3, 640, 360, decs)
    decorations_group.add(scr_im)

    #Cпрайты игровых объектов
    for letter in draw_alphabet():
        gameobjects_group.add(letter)

    #Выбор слова
    words = get_content(0, None)
    choice = random.choice(words).split('\n')[0].upper()
    word = Word(choice, '_' * len(choice))
    #print(word.full)
    tryies = 10

    while True:
        clock.tick(FPS)


        
        if word.game == word.full:
            break
        
        if tryies == 9:
            final = draw_decs(2, 980, 400, decs)
            decorations_group.add(final)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for obj in gameobjects_group:
                        if obj.check_collisions(event.pos) == True:
                            obj.kill_me()
                            if obj.name in word.undiscovered:
                                word.update(obj.name)
                            elif obj.name not in word.full:
                                screamers_group.add(draw_decs(random.randint(0,2), 640, 360, screamers))
                                screamer = True
                                tryies -= 1
                                print(tryies)
                            break

        if screamer == True:
            screamers_group.draw(screen)
            screamer = False
            pygame.display.flip()
            for s in screamers_group:
                s.kill()
            time.sleep(1)
        else:
            # Рендеринг
            decorations_group.draw(screen)
            gameobjects_group.draw(screen)

            # Написать слово
            word.draw(decorations_group)
            pygame.display.flip()
    break
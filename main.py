import pygame
import random

pygame.init()

Clock = pygame.time.Clock()

screen = pygame.display.set_mode((288, 351))
pygame.display.set_caption('Packman!!!')

Mx = (6, 63, 120, 177, 234)
My = (69, 126, 183, 240, 297)

player_image = pygame.image.load('packman_game/packman.png')
player = player_image.get_rect(topleft=(6,69))

coin_image = pygame.image.load('packman_game/coin.png')
coin = coin_image.get_rect(topleft=(random.choice(Mx), random.choice(My)))

happy_pm = pygame.image.load('packman_game/happy_pm.png').convert_alpha()

winning = pygame.image.load('packman_game/winning.png').convert_alpha()

field = pygame.image.load('packman_game/field.png').convert()

pygame.display.set_icon(player_image)

speed = 57
touches = 0
win = False
my_font = pygame.font.Font('packman_game/Minecraft.ttf', 40)
# my_font2 = pygame.font.Font('packman_game/Minecraft.ttf', 40)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(field, (0,0))
    touches_text = my_font.render(f'Touches {touches}-10', False, (60, 163, 112))
    screen.blit(touches_text, (10,16))
    if win:
        screen.blit(winning, (4, 4))
        screen.blit(happy_pm, player)
    if not win:
        screen.blit(coin_image, coin)
        screen.blit(player_image, player)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

        if player.x < 6:
            player.x = 6
        if player.x > 234:
            player.x = 234

        if player.y > 297:
            player.y = 297
        if player.y < 69:
            player.y = 69

        if player.colliderect(coin):
            touches += 1
            Mx = (6, 63, 120, 177, 234)
            My = (69, 126, 183, 240, 297)
            coin.x = random.choice(Mx)
            coin.y = random.choice(My)

        if touches >= 10:
            win = True
            

        
        
    
    
    
    

    pygame.display.flip()
    Clock.tick(10)
    
print(player.bottomleft)

pygame.quit()
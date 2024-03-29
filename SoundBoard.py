import pygame
from pygame.locals import*
pygame.init
app_display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Sound Board')

#Функция для проигрывания файла
def play(sound_file):
    pygame.init()
    g = sound_file
    pygame.mixer.music.load(g)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

#Функция для анализа событий внутри дисплея
def event_handler(): 
    for event in pygame.event.get(): 
        if (event.type == QUIT): 
            pygame.quit() 
            quit()
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Button 1:
            if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 365 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 170:
                play("content\\sounds\\sample-3s.wav")
            # Button 2:
            if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 565 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 170:
                play("content\\sounds\\sample-3s.wav")
            # Button 3:
            if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 365 and pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 325:
                play("content\\sounds\\sample-3s.wav")
            # Button 4:
            if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 565 and pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 325:
                play("content\\sounds\\sample-3s.wav")
            # Button 5:
            if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 365 and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 470:
                play("content\\sounds\\sample-3s.wav")
            # Button 6:
            if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 565 and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 470:
                play("content\\sounds\\sample-3s.wav")
    clock.tick(60)

#Визуал:
app_display.fill('white')
img = pygame.image.load('content\\visuals\\button_sb.png')
button1 = pygame.image.load('content\\visuals\\1_sb.png')
button2 = pygame.image.load('content\\visuals\\2_sb.png')
button3 = pygame.image.load('content\\visuals\\3_sb.png')
button4 = pygame.image.load('content\\visuals\\4_sb.png')
button5 = pygame.image.load('content\\visuals\\5_sb.png')
button6 = pygame.image.load('content\\visuals\\6_sb.png')

app_display.blit(img, (200, 50))
app_display.blit(img, (200, 200))
app_display.blit(img, (400, 50))
app_display.blit(img, (400, 200))
app_display.blit(img, (200, 350))
app_display.blit(img, (400, 350))

app_display.blit(button1, (200, 50))
app_display.blit(button3, (200, 200))
app_display.blit(button2, (400, 50))
app_display.blit(button4, (400, 200))
app_display.blit(button5, (200, 350))
app_display.blit(button6, (400, 350))

while True: 
    event_handler() 
    pygame.display.update()

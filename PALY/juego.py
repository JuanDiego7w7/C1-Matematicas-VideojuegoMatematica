import pygame
from pygame.locals import*

pygame.init() #Iniciar pygame

screen=pygame.display.set_mode((1500,900)) #Ajustar medida de pantalla
pygame.display.set_caption("Maze runner") #Titulo
fondo = pygame.image.load("img/bgplay.png") #Fondo de imagen

chico = pygame.image.load("img/chico.png")#Chico 1

gato = pygame.image.load("img/gato_derecha.png")


corazon1 = pygame.image.load("img/corazon.png")
corazon2 = pygame.image.load("img/corazonverde.png")
mouse = pygame.image.load("img/mouse.png")


#Datos
PosX=450
PosY=430
Vel=10

# Texto
pygame.font.init() #Iniciamos la fuente
fuente1 = pygame.font.SysFont("Comic Sans MS", 40) #Citamos fuente y tamaño de letra
texto = fuente1.render("ENCUENTRA EL CAMINO", True, "pink") #Escribimos el texto; True: Suavizado, False: Con ruido; color del texto
fondo.blit(texto,(50,100)) #Mostramos el texto y su posición


# #Sonidos
# pygame.mixer.init()
# ambiente = pygame.mixer.Sound('space_ambiente.wav')
# ambiente.play()

#score

Ejecuta=True
while(Ejecuta): #Variable
    screen.blit(fondo,(1,0))
    # Lineas Horizontales (Filas)
    pygame.draw.line(screen,"yellow",(1067,170),(440,170),10) # Linea 1
    pygame.draw.line(screen,"yellow",(565,295),(1065,295),10) # Linea 2
    pygame.draw.line(screen,"yellow",(565,415),(431,415),10) # Linea 3
    pygame.draw.line(screen,"Yellow",(950,415),(810,415),10) # Linea 3.1
    pygame.draw.line(screen,"yellow",(820,530),(695,530),10) # Linea 4
    pygame.draw.line(screen,"yellow",(562,650),(820,650),10) # Linea 5
    pygame.draw.line(screen,"yellow",(1067,775),(440,775),10) # Linea 6

    # Lineas Verticales (Columnas)
    pygame.draw.line(screen,"skyblue",(435,166),(435,415),10) # linea  1
    pygame.draw.line(screen,"skyblue",(435,535),(435,780),10) # linea  1.1
    pygame.draw.line(screen,"skyblue",(560,535),(560,415),10) # Linea  2
    pygame.draw.line(screen,"skyblue",(692,535),(692,300),10) # linea  3
    pygame.draw.line(screen,"skyblue",(815,655),(815,534),10) # Linea 4
    pygame.draw.line(screen,"skyblue",(945,415),(945,780),10) # linea  5
    pygame.draw.line(screen,"skyblue",(1070,166),(1070,415),10) # linea  6 
    pygame.draw.line(screen,"skyblue",(1070,535),(1070,780),10) # linea  6.1


    screen.blit(chico,(1150,300))
    screen.blit(gato,(PosX,PosY))
    screen.blit(corazon1,(980,450))
    screen.blit(corazon2,(730,690))
    screen.blit(mouse,(600,450))
    for evento in pygame.event.get():
        if(evento.type==QUIT):
            Ejecuta=False
            break
        if(evento.type==pygame.KEYDOWN):
            if(evento.key == K_RIGHT):
                gato = pygame.image.load("img/gato_derecha.png")
                PosX = PosX + Vel
                if((PosX >= 431)and(PosX <= 565)) and ((PosY >= 400)and(PosY <= 525)): #Linea 2
                    PosX = 458
                if((PosX >= 969)and(PosX <= 979)) and ((PosY >= 170) and (PosY <= 210)):#01
                    PosX = 969
                if((PosX >= 459)and(PosX <= 550)) and ((PosY >= 211)and(PosY <= 299)):#03
                    PosX = 459
                if((PosX >= 589)and(PosX <= 620)) and ((PosY >= 300) and (PosY <= 529)):#05
                    PosX = 589
                if((PosX >= 708)and(PosX <= 722))and((PosY >= 530)and(PosY <= 570)): #07
                    PosX = 708
                if((PosX >= 460)and(PosX <= 500))and((PosY >= 561)and(PosY <= 649)):#09
                    PosX = 460
                if((PosX >= 960)and(PosX <= 1000))and((PosY >= 300)and(PosY <= 409)):#15
                    PosX = 960
                if((PosX >= 960)and(PosX <= 1000))and((PosY >= 451)and(PosY <= 690)):#16
                    PosX = 960
                if((PosX >= 710)and(PosX <= 740))and((PosY >= 331)and(PosY <= 419)):#22
                    PosX = 710
                if((PosX >= 840)and(PosX <= 860))and((PosY >= 420)and(PosY <= 670)):#24
                    PosX = 840
                print(PosX,PosY)
                
            if(evento.key == K_LEFT):
                gato = pygame.image.load("img/gato_izquierda.png")
                PosX = PosX - Vel
                if((PosX >= 430)and(PosX <= 440)) and ((PosY >= 400)and(PosY <= 700)):
                    PosX = 440
                if((PosX >= 558)and(PosX <=590)) and ((PosY >= 331) and (PosY <= 529)):
                    PosX = 569
                if((PosX >= 428) and (PosX <= 439)) and (PosY >= 170)and(PosY <= 310):
                    PosX = 439
                if((PosX >= 800)and(PosX <= 820))and((PosY >= 451)and(PosY<= 649)):#11
                    PosX = 820
                if((PosX >= 680)and(PosX <= 700))and((PosY >= 300)and(PosY <= 450)):#13
                    PosX = 700
                if((PosX >= 930)and(PosX <= 950))and((PosY >= 331)and(PosY <= 670)):#20
                    PosX = 950
                print(PosX,PosY)

            if(evento.key == K_UP):
                gato = pygame.image.load("img/gato_arriba.png")
                PosY = PosY - Vel
                if((PosX >= 420)and(PosX <= 565)) and (PosY==400):
                    PosY = 410
                if((PosX >= 479)and(PosX <=567))and((PosY >= 500)and(PosY <=540)):
                    PosY = 540
                if((PosX >= 439) and (PosX <=989)) and ((PosY >= 160)and(PosY <=170)):
                    PosY = 170
                if((PosX >= 490)and(PosX <= 609)) and ((PosY >= 290) and (PosY <= 300)):#04
                    PosY = 300
                if((PosX >= 610)and(PosX <= 730)) and ((PosY >= 520)and(PosY <= 530)): #06
                    PosY = 530
                if((PosX >= 481)and(PosX <= 818))and((PosY >= 630)and(PosY <= 650)):#10
                    PosY = 650
                if((PosX >= 700)and(PosX <= 990))and((PosY >= 280)and(PosY <= 300)):#14
                    PosY = 300
                if(PosX >= 991)and((PosY >= 400)and(PosY <= 420)):#17
                    PosY = 420
                if((PosX >= 731)and(PosX <= 860))and((PosY >= 380)and(PosY <= 420)):#23
                    PosY = 420
                print(PosX,PosY)
                
                
            if(evento.key == K_DOWN):
                gato = pygame.image.load("img/gato_abajo.png")
                PosY = PosY + Vel
                if((PosX >= 420)and(PosX <= 880)) and (PosY >= 670):
                    PosY = 670
                if((PosX >= 438) and (PosX <= 560)) and ((PosY >= 300)and(PosY <= 341)):
                    PosY = 310
                if((PosX >= 490)and(PosX <= 969)) and ((PosY >= 190) and (PosY <= 200)):#02
                    PosY = 190
                if((PosX >= 480)and(PosX <= 708))and((PosY >= 550)and(PosY <= 570)):#08
                    PosY = 550
                if((PosX >= 700)and(PosX <= 820))and((PosY >= 430)and(PosY <= 460)):#12
                    PosY = 430
                if(PosX >= 981)and((PosY >= 429)and(PosY <= 460)):#18
                    PosY = 430
                if((PosX >= 950)and(PosX <= 980))and((PosY >= 670)and(PosY <= 690)):#19
                    PosY = 670
                if((PosX >= 731)and(PosX <= 950))and((PosY >= 310)and(PosY <= 340)):#21
                    PosY = 310
                print(PosX,PosY)

    pygame.display.update()
pygame.quit()
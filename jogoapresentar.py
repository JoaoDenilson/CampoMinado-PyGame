import pygame, os
from pygame.locals import *
from sys import exit
import random 
import time

os.environ['SDL_VIDEO_CENTERED']='1' #Centraliza a tela.
pygame.init()
pygame.font.init()

tela = pygame.display.set_mode((420,540 ), 0, 32)
pygame.display.set_caption('Campo bombado')
tela.fill((200,200,200))
#variáveis



comp_casa = 61
alt_casa = 50

pygame.mixer.pre_init(44100,32,2,4096)#Qualidade do audio

#imagnes
bola= pygame.image.load("casaclik.png")
xis = pygame.image.load("img_bomba.jpg")
inic_logo = pygame.image.load("logo.jpg")

#fontes
font_name = pygame.font.get_default_font()
font_game = pygame.font.SysFont(font_name,40)
font_inic = pygame.font.SysFont(font_name,25)

cont = 0
PosX = 0
PosY = 0
#relogio
clock = pygame.time.Clock()

#lista dos objetos(bomba,casa normal)
pecas=[xis, xis, xis, xis, xis, xis, bola, bola, bola, bola, bola, bola, bola,
           bola, bola, bola ,bola, bola, bola, bola, bola, bola, bola, bola, bola,
           bola, bola, bola, bola, bola, bola, bola, bola, bola, bola, bola]
           
#Defini apenas 1 ponto por casa após clik
#flag= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] 

#Função Embaralhar os objetos.
#Gerando o local das bombas aleatoriamente 
def embaralhar():
    random.shuffle(pecas)

  
def criarmesa() :
    global cont, flag
    if pygame.mouse.get_pressed()[0]: #Evento do clik do mouse
        PosX = pygame.mouse.get_pos()[0]
        PosY = pygame.mouse.get_pos()[1] 
        #Posicionamento
        #linha 01
        if(PosX > 61 and PosX < 110 and PosY > 61 and PosY < 110):
            (tela.blit(pecas[0],(61,61)))
            if pecas[0] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 111 and PosX < 160 and PosY > 61 and PosY < 110):
            (tela.blit(pecas[1],(111,61)))
            if pecas[1] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 161 and PosX < 210 and PosY > 61 and PosY < 110):
            (tela.blit(pecas[2],(161,61)))
            if pecas[2] == bola:
                
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
        
        elif(PosX > 211 and PosX < 260 and PosY > 61 and PosY < 110):
            (tela.blit(pecas[3],(211,61)))
            if pecas[3] == bola:
                acerto()
                cont = cont + 1   
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 261 and PosX < 310 and PosY > 61 and PosY < 110):
            (tela.blit(pecas[4],(261,61)))
            if pecas[4] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 311 and PosX < 360 and PosY > 61 and PosY < 110):
            (tela.blit(pecas[5],(311,61)))
            if pecas[5] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
        #linha 02
        elif(PosX > 61 and PosX < 110 and PosY > 111 and PosY < 160):
            (tela.blit(pecas[6],(61,111)))
            if pecas[6] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 111 and PosX < 160 and PosY > 111 and PosY < 160):
            (tela.blit(pecas[7],(111,111)))
            if pecas[7] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 161 and PosX < 210 and PosY > 111 and PosY < 160):
            (tela.blit(pecas[8],(161,111)))
            if pecas[8] == bola:
                
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
        
        elif(PosX > 211 and PosX < 260 and PosY > 111 and PosY < 160):
            (tela.blit(pecas[9],(211,111)))
            if pecas[9] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 261 and PosX < 310 and PosY > 111 and PosY < 160):
            (tela.blit(pecas[10],(261,111)))
            if pecas[10] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 311 and PosX < 360 and PosY > 111 and PosY < 160):
            (tela.blit(pecas[11],(311,111)))
            if pecas[11] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        #Linha 03
        elif(PosX > 61 and PosX < 110 and PosY > 161 and PosY < 210):
            (tela.blit(pecas[12],(61,161)))
            if pecas[12] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 111 and PosX < 160 and PosY > 161 and PosY < 210):
            (tela.blit(pecas[13],(111,161)))
            if pecas[13] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 161 and PosX < 210 and PosY > 161 and PosY < 210):
            (tela.blit(pecas[14],(161,161)))
            if pecas[14] == bola:
                cont = cont + 1
                acerto()
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
        
        elif(PosX > 211 and PosX < 260 and PosY > 161 and PosY < 210):
            (tela.blit(pecas[15],(211,161)))
            if pecas[15] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 261 and PosX < 310 and PosY > 161 and PosY < 210):
            (tela.blit(pecas[16],(261,161)))
            if pecas[16] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 311 and PosX < 360 and PosY > 161 and PosY < 210):
            (tela.blit(pecas[17],(311,161)))
            if pecas[17] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        #Linha 04
        elif(PosX > 61 and PosX < 110 and PosY > 211 and PosY < 260):
            (tela.blit(pecas[18],(61,211)))
            if pecas[18] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 111 and PosX < 160 and PosY > 211 and PosY < 260):
            (tela.blit(pecas[19],(111,211)))
            if pecas[19] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 161 and PosX < 210 and PosY > 211 and PosY < 260):
            (tela.blit(pecas[20],(161,211)))
            if pecas[20] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
        
        elif(PosX > 211 and PosX < 260 and PosY > 211 and PosY < 260):
            (tela.blit(pecas[21],(211,211)))
            if pecas[21] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 261 and PosX < 310 and PosY > 211 and PosY < 260):
            (tela.blit(pecas[22],(261,211)))
            if pecas[22] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 311 and PosX < 360 and PosY > 211 and PosY < 260):
            (tela.blit(pecas[23],(311,211)))
            if pecas[23] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        #Linha 05
        elif(PosX > 61 and PosX < 110 and PosY > 261 and PosY < 310):
            (tela.blit(pecas[24],(61,261)))
            if pecas[24] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 111 and PosX < 160 and PosY > 261 and PosY < 310):
            (tela.blit(pecas[25],(111,261)))
            if pecas[25] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 161 and PosX < 210 and PosY > 261 and PosY < 310):
            (tela.blit(pecas[26],(161,261)))
            if pecas[26] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
        
        elif(PosX > 211 and PosX < 260 and PosY > 261 and PosY < 310):
            (tela.blit(pecas[27],(211,261)))
            if pecas[27] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 261 and PosX < 310 and PosY > 261 and PosY < 310):
            (tela.blit(pecas[28],(261,261)))
            if pecas[28] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 311 and PosX < 360 and PosY > 261 and PosY < 310):
            (tela.blit(pecas[29],(311,261)))
            if pecas[29] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        #Linha 06
        elif(PosX > 61 and PosX < 110 and PosY > 311 and PosY < 360):
            (tela.blit(pecas[30],(61,311)))
            if pecas[30] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 111 and PosX < 160 and PosY > 311 and PosY < 360):
            (tela.blit(pecas[31],(111,311)))
            if pecas[31] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
            
        elif(PosX > 161 and PosX < 210 and PosY > 311 and PosY < 360):
            (tela.blit(pecas[32],(161,311)))
            if pecas[32] == bola:
                cont = cont + 1
                acerto()
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()
        
        elif(PosX > 211 and PosX < 260 and PosY > 311 and PosY < 360):
            (tela.blit(pecas[33],(211,311)))
            if pecas[33] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 261 and PosX < 310 and PosY > 311 and PosY < 360):
            (tela.blit(pecas[34],(261,311)))
            if pecas[34] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()

        elif(PosX > 311 and PosX < 360 and PosY > 311 and PosY < 360):
            (tela.blit(pecas[35],(311,311)))
            if pecas[35] == bola:
                acerto()
                cont = cont + 1
                print(cont)
                pygame.display.flip()
            else:
                mensagem()
                pygame.display.flip()
                reinicio()                                
 
#--------------------------------------------------------------#                
        if cont == 30:
            text1 = font_game.render("Venceu o Jogo", 1,(255,0,0))
            tela.blit(text1,(120,420))
            ganhou()
            posiçoes()
            pygame.display.flip()
            reinicio()
             
def acerto():
    acertou = pygame.mixer.Sound("acertou.ogg")
    acertou.play()
    
def ganhou():
    global comp_casa
    ganhou = pygame.mixer.music.load("ganhou.ogg")
    pygame.mixer.music.play()
    text3 =  font_inic.render("Pontos: %d" %(cont), 1,(255,0,0))
    (tela.blit(text3,(20,460)))

#mostra todas as posições dos objetos
def posiçoes():
    comp_casa = 61
    for linha1 in range(0,6):
        tela.blit(pecas[linha1],(comp_casa,61))
        comp_casa = comp_casa + 50
          
    comp_casa = 61    
    for linha2 in range(6,12):
        tela.blit(pecas[linha2],(comp_casa,111))
        comp_casa = comp_casa + 50
        
    comp_casa = 61    
    for linha3 in range(12,18):
        tela.blit(pecas[linha3],(comp_casa,161))
        comp_casa = comp_casa + 50
          
    comp_casa = 61    
    for linha4 in range(18,24):
        tela.blit(pecas[linha4],(comp_casa,211))
        comp_casa = comp_casa + 50
        
    comp_casa = 61    
    for linha5 in range(24,30):
        tela.blit(pecas[linha5],(comp_casa,261))
        comp_casa = comp_casa + 50
          
    comp_casa = 61    
    for linha6 in range(30,36):
        tela.blit(pecas[linha6],(comp_casa,311))
        comp_casa = comp_casa + 50

#Reinicia o jogo        
def reinicio():
    time.sleep(7)
    continuar = False
    jogar = True
    telainicial()
 #Mostra a mensagem que perdeu   
def mensagem():
    text = font_game.render("GAME OVER", 1,(255,0,0))
    (tela.blit(text,(120,420)))
    text3 =  font_inic.render("Pontos: %d" %(cont), 1,(255,0,0))
    (tela.blit(text3,(20,460)))
    perdeu()
    posiçoes()
     
 #Toca o audio que perdeu.     
def perdeu():
    global comp_casa
    bomba = pygame.mixer.Sound("s_bomba.ogg")
    bomba.play()
    pygame.mixer.music.stop() 
    
#------------------------------------------#        
def jogando():
    global cont

    continuar = False
    jogar = True
    tela.fill((192,192,192))
    som_bomb = pygame.mixer.music.load("c.ogg")
    pygame.mixer.music.play(-1)
    embaralhar()
    
    while jogar:
        
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                quit()
            if  event.type == MOUSEBUTTONDOWN:
                PosX = pygame.mouse.get_pos()[0]
                PosY = pygame.mouse.get_pos()[1]
                cenario()
                criarmesa()

                pygame.display.update()
    pygame.display.flip()
    
def cenario():
    cont1 = 60
    for i in range(0,7):
        pygame.draw.line(tela,(0,0,0),(60,cont1),(360,cont1),1)
        pygame.draw.line(tela,(0,0,0),(cont1,60),(cont1,360),1)
        cont1 = cont1 + 50

        
    pygame.display.update()
    
def telainicial():
    global cont
    continuar = True
    tela.fill((250,250,250))
    
    while continuar == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                
        PosX = pygame.mouse.get_pos()[0]
        PosY = pygame.mouse.get_pos()[1] 
        tela.blit(inic_logo,(0,100)) 
        text2 = font_inic.render("Novo jogo", 1,(255,0,0))
        tela.blit(text2,(180,440))

        text4 = font_inic.render("Sair", 1,(255,0,0))
        tela.blit(text4,(180,480))
        pygame.display.update()

        if  event.type == MOUSEBUTTONDOWN:
            if((PosX >= 180 and PosX <= 260) and (PosY >= 440 and PosY <= 460)):
                continuar = False
                cont = 0
                jogando()
        if  event.type == MOUSEBUTTONDOWN:
            if((PosX >= 180 and PosX <= 250) and (PosY >= 480 and PosY <= 500)):
                pygame.quit() 

telainicial()


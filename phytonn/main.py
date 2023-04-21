from email.mime import message
from World import *
from Buttons import *
import pygame
from Board import *

def humanmove(): #human movement
    for event in pygame.event.get():
        position_x = human.get_x()
        position_y = human.get_y()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                print("U")
                if position_y == 0:
                    return 
                else:
                    human.set_y(position_y-1)
                    print("Human move to:" + str(human.get_x()) + str(human.get_y()))
                    return
            if event.key ==pygame.K_LEFT:
                print("L")
                if position_x == 0:
                    return
                else:
                    human.set_x(position_x - 1)
                    print("Human move to:" + str(human.get_x()) + str(human.get_y()))
                    return			
            if event.key ==pygame.K_DOWN:
                print("D")
                if position_y == world.get_m() - 1:
                    return
                else:
                    human.set_y(position_y+1)
                    print("Human move to:" + str(human.get_x()) + str(human.get_y()))
                    return
            if event.key ==pygame.K_RIGHT:
                print("R")
                if position_x == world.get_n() - 1:
                    return
                else:
                    human.set_x(position_x+1)
                    print("Human move to:" + str(human.get_x()) + str(human.get_y()))
                    return
            if event.key ==pygame.K_8: #turn on special ability
                if human.get_noability() == 0:
                    print("Ability on")
                    human.set_ability(5)
                    break
                else:
                    print("You cant use a special ability")
                    break


print("Object Oriented Programming Project 3")
print("Human-RED  Wolf-BLACK  Sheep-DARK_GRAY  Fox-ORANGE  Turtle-GREEN  Antelope-YELLOW  Cybersheep- PURPLE")
print("Grass - GREEN  Sow thistle - LIGHT_BLUE  Guarana - DARK_PINK  Belladonna -LIGHT_PINK  Sosnowsky's hogweed-DARK_BLUE")
print("Enter the size of the board NxM: ")
n= input()
m=input()
print("Size of the world:" + n + "x" + m)
n=int(n)
m=int(m)
world=World(n,m,0)
world.place_organism()
human=world.get_human()

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Object Oriented Programming Project 3')
background_colour = (192,192,192)
screen.fill(background_colour)
surface=pygame.Surface([500,500])
info=pygame.Surface([250,500]) #surface with info about what is going on on the board
surface.fill((255,255,255))
info.fill((255,255,255))
text_font = pygame.font.SysFont('Arial', 10) #font for text 

save = Buttons(20, 10, 'Save', screen, False)
load = Buttons(245, 10, 'Load', screen, False)
next_turn = Buttons(470, 10, 'Next Turn', screen, False)

board=Board(world, surface)
board.paint()
game = True

while game:
    
    screen.blit(surface,(70,80)) 
    screen.blit(info,(600,80)) 
    humanmove()
    if save.draw_button(): #saving the state of the game to file wynik.txt
        print('Save')
        world.save_game()
    if load.draw_button(): #loading game from wynik.txt
        print('Load')
        file=open("wynik.txt")
        lines=[]
        for line in file:  
            lines.append(line)
        words=[] #array where one line is one element
        for i in range(len(lines)):
            words.append(lines[i].split())  
        wrd=words[0]
        wrd1=words[1]
        turn=wrd1[3]
        turn=int(turn)
        world=World(str(wrd[2]), str(wrd[3]),turn)
        wrd2=words[2]
        num=wrd2[3]
        num=int(num)
        org=world.get_organism()
        for i in range(0,num):
            wrd_obj=words[i+3]
            name=wrd_obj[0]
            draw=wrd_obj[1]
            pos_x=wrd_obj[2]
            pos_x=int(pos_x)
            pos_y=wrd_obj[3]
            pos_y=int(pos_y)
            age=wrd_obj[4]
            age=int(age)
            strength=wrd_obj[5]
            strength=int(strength)
            if name=="Wolf":
                w=Wolf(pos_x, pos_y,world)
                w.set_age(age)
                w.set_strength(strength)
                world.get_organism().append(w)
            if name=="Sheep":
                s=Sheep(pos_x, pos_y,world)
                s.set_age(age)
                s.set_strength(strength)
                world.get_organism().append(s)
            if name=="Antelope":
                a=Antelope(pos_x, pos_y,world)
                a.set_age(age)
                a.set_strength(strength)
                world.get_organism().append(a)
            if name=="Fox":
                f=Fox(pos_x, pos_y,world)
                f.set_age(age)
                f.set_strength(strength)
                world.get_organism().append(f)
            if name=="Turtle":
                t=Turtle(pos_x, pos_y,world)
                t.set_age(age)
                t.set_strength(strength)
                world.get_organism().append(t)
            if name=="Grass":
                gr=Grass(pos_x, pos_y,world)
                gr.set_age(age)
                gr.set_strength(strength)
                world.get_organism().append(gr)
            if name=="Guarana":
                gu=Guarana(pos_x, pos_y,world)
                gu.set_age(age)
                gu.set_strength(strength)
                world.get_organism().append(gu)
            if name=="Belladonna":
                b=Belladonna(pos_x, pos_y,world)
                b.set_age(age)
                b.set_strength(strength)
                world.get_organism().append(b)
            if name=="Sowthistle":
                sow=Sowthistle(pos_x, pos_y,world)
                sow.set_age(age)
                sow.set_strength(strength)
                world.get_organism().append(sow)
            if name=="Sosnowskyshogweed":
                sos=Sosnowskyshogweed(pos_x, pos_y,world)
                sos.set_age(age)
                sos.set_strength(strength)
                world.get_organism().append(sos)
            if name=="Human":
                human=Human(pos_x, pos_y,world)
                human.set_age(age)
                human.set_strength(strength)
                world.get_organism().append(human)
        
        wrd3=words[num+3]
        ability=wrd3[2]
        human.set_ability(ability)
        wrd4=words[num+4]
        noability=wrd4[1]
        human.set_noability(noability)
        file.close()
        world.draw_world()
        board=Board(world, surface)
        surface.fill((255,255,255))
        board.paint()

    if next_turn.draw_button(): #NEXT TURN
        info.fill(pygame.Color("white"))
        surface.fill((255,255,255))
        world.make_turn()
        j=0
        for obj in world.get_messageinfo():
            text_surface= text_font.render(obj, True, (0, 0, 0))
            info.blit(text_surface, (0,j))
            j+=10
        board.paint()
        world.get_messageinfo().clear()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.flip()
pygame.quit()

# coding: utf-8
import random
from tkinter import *
Cases = []
for i in range(200) :
    Cases.append([0]*200)
for i in range(4000) :
    Cases[random.randint(1,199)][random.randint(1,199)] = "1"
    Cases[random.randint(1,199)][random.randint(1,199)] = "2"
    #Cases[random.randint(1,199)][random.randint(1,199)] = "4"
for i in range(301) :
    Cases[random.randint(1,199)][random.randint(1,199)] = "3"
comd=0
sens=3
x=100
y=100
savchoice ='nope'
menu = Tk()
menu.resizable(width=False,height=False)
menu.title("menu")
menu.geometry("150x60")
def quit():
    menu.destroy()
def cunm():
    global savchoice
    savchoice='encode'
    menu2()
def cum():
    global savchoice
    savchoice='decode'  
    menu2()
b1=Button(menu,text="créer un nouveau monde",width=20,command=cunm)
b1.place(x=5,y=0)
b2=Button(menu,text="charger le monde",width=20,command=cum)
b2.place(x=5,y=30)
e=Entry(menu)
def menu2() :
    b1.place_forget()
    b2.place_forget()
    e.place(x=5,y=0)
    #quit()
menu.mainloop()

if savchoice=="encode" :
    sav = open("saves/1.SAV", "w")
    sav.write(str(Cases))
    sav.close()
    
elif savchoice =="decode" :
    sav = open("saves/1.SAV", "r")
    Cases=sav.readline()
    Cases=eval(Cases)
    sav.close()
    sav = open("saves/1.SAV", "r")
    sav.readline() 
    x=int(sav.readline())
    y=eval(sav.readline())
    sav.close()    
        

i=0
game = Tk()
game.resizable(width=False,height=False)
game.title("adventure box")
game.geometry("640x640")

gamec = Canvas(game,width=1000, height=1000)
water = PhotoImage(file="assets/textures/terrain/water.png")
bcks= PhotoImage(file="assets/textures/gui/back.png")
select= PhotoImage(file="assets/textures/gui/select.png")
treegrass = PhotoImage(file="assets/textures/terrain/treegrass.png")
grass = PhotoImage(file="assets/textures/terrain/grass.png")
rock =PhotoImage(file="assets/textures/terrain/rock.png")
block =PhotoImage(file="assets/textures/terrain/block.png")
stone=PhotoImage(file="assets/textures/terrain/stone.png")


fichier = open("config.txt", "r")
for i in range(2) :
    config =fichier.readline()
fichier.close()
if str(config) == "true" :
    tux = PhotoImage(file="assets/textures/terrain/tux.png")
    d1=PhotoImage(file="assets/textures/terrain/1.png")
    d2=PhotoImage(file="assets/textures/terrain/2.png")
    d3=PhotoImage(file="assets/textures/terrain/3.png")
    d4=PhotoImage(file="assets/textures/terrain/4.png")    
else :
    tux = PhotoImage(file="assets/textures/player/wiliam/tux.png")
    d1=PhotoImage(file="assets/textures/player/wiliam/1.png")
    d2=PhotoImage(file="assets/textures/player/wiliam/2.png")
    d3=PhotoImage(file="assets/textures/player/wiliam/3.png")
    d4=PhotoImage(file="assets/textures/player/wiliam/4.png")   
mo = False
xg = 0
yg = 0


lgn1 = ' '
lgn2 = ' '
lgn3 = ' '
lgn4 = ' '
lgn5 = ' '
cwc = 0

print(lgn1)
print(lgn2)
print(lgn3)
print(lgn4)
print(lgn5)
#0=herbe / 1=arbre / 2=cochon
def placetux() :
    if sens == 1 :
        gamec.create_image(128, 128, anchor=NW, image=d1)
    elif sens == 2 :
        gamec.create_image(128, 128, anchor=NW, image=d2)
    elif sens == 3 :
        gamec.create_image(128, 128, anchor=NW, image=d3)
    elif sens == 4 :
        gamec.create_image(128, 128, anchor=NW, image=d4) 
        
class gui :
    x=384
    y=0
    def rock() :
        print("my rock is hard !")
        
def bck() :
    x=-64
    y=-64
    for i in range(10) :
        x=x+64
        for i in range(12):
            if y>640 :
                y=-64
            y=y+64
            gamec.create_image(x, y, anchor=NW, image=bcks)
             
def reload():
    global bck
    global x
    global y
    global cwc
    global xg
    global yg    
    sav = open("saves/1.SAV", "w")
    sav.write(str(Cases))
    sav.write('\n'+str(x))
    sav.write('\n'+str(y))
    sav.close()    
    cwc=0
    i=0
    xg = 0
    yg = 0
    gamec.delete(ALL)

    bck()
    global gui
    gamec.create_image(gui.x, gui.y, anchor=NW, image=select)
    lgn1 = str(Cases[x-2][y+2]) + str(Cases[x-1][y+2]) + str(Cases[x][y+2]) + str(Cases[x+1][y+2]) + str(Cases[x+2][y+2])
    lgn2 = str(Cases[x-2][y+1]) + str(Cases[x-1][y+1]) + str(Cases[x][y+1]) + str(Cases[x+1][y+1]) + str(Cases[x+2][y+1])
    lgn3 = str(Cases[x-2][y]) + str(Cases[x-1][y]) + str(Cases[x][y]) + str(Cases[x+1][y]) + str(Cases[x+2][y])
    lgn4 = str(Cases[x-2][y-1]) + str(Cases[x-1][y-1]) + str(Cases[x][y-1]) + str(Cases[x+1][y-1]) + str(Cases[x+2][y-1])
    lgn5 = str(Cases[x-2][y-2]) + str(Cases[x-1][y-2]) + str(Cases[x][y-2]) + str(Cases[x+1][y-2]) + str(Cases[x+2][y-2])
    #xg=64
    affw = str("/"+lgn1 + "/" + lgn2 + "/" +lgn3 + "/" + lgn4 + "/" +lgn5 +"*")
    b = affw[cwc]    
    while b != "*" :
        affw = str("/"+lgn1 + "/" + lgn2 + "/" +lgn3 + "/" + lgn4 + "/" +lgn5 +"*")
        b = affw[cwc]

        if cwc == 0:
            if b == "0" :
                gamec.create_image(xg, yg, anchor=NW, image=grass)
                if cwc == 4 :
                    gamec.create_image(xg, yg, anchor=NW, image=tux)
            elif b == "1" :
                gamec.create_image(xg, yg, anchor=NW, image=treegrass)
                if cwc == 4 :
                    gamec.create_image(xg, yg, anchor=NW, image=tux)
            elif b == "2" :
                gamec.create_image(xg, yg, anchor=NW, image=water)
            cwc = cwc +1
        elif b == "/" :
            cwc=cwc+1
            yg = yg + 64
            xg = 0
        elif b == "0" :
            cwc = cwc + 1
            gamec.create_image(xg, yg, anchor=NW, image=grass)
            xg = xg +64
        elif b == "1" :
            cwc = cwc + 1
            gamec.create_image(xg, yg, anchor=NW, image=treegrass)
            xg = xg +64
        elif b == "2" :
            cwc = cwc + 1
            gamec.create_image(xg, yg, anchor=NW, image=water)
            xg = xg +64
        elif b == "3" :
            cwc = cwc + 1
            gamec.create_image(xg, yg, anchor=NW, image=rock)
            xg = xg +64   
        elif b == "4" :
            cwc = cwc + 1
            gamec.create_image(xg, yg, anchor=NW, image=stone)
            xg = xg +64           
        gamec.create_image(128, 128, anchor=NW, image=tux)
        placetux()
    if str(Cases[x][y]) == "3" :
        print("oh my rock !")
        gui.rock()
    gamec.update()
    game.update()




def q(event) :
    global x
    global sens
    sens = 4
    print(x,y)
    if x> 3 :
        if (str(Cases[x-1][y])!="1") and (str(Cases[x-1][y]) != "2"):
            x=x-1
        reload()
    else :
        reload()
        gamec.create_image(128, 128, anchor=NW, image=block)

def d(event) :
    global x
    global sens
    sens = 2
    print(x,y)
    if x < 197 :
        if (str(Cases[x+1][y])!="1") and (str(Cases[x+1][y]) != "2"):
            x=x+1
        reload()
    else :
        reload()
        gamec.create_image(128, 128, anchor=NW, image=block)
    
def z(event) :
    global y
    global sens
    sens = 1
    print(x,y)
    if y < 197 :
        if (str(Cases[x][y+1])!="1") and (str(Cases[x][y+1]) !="2"):
            y=y+1
        reload()
    else :
        reload()
        gamec.create_image(128, 128, anchor=NW, image=block)
    
def s(event) :
    global y
    global sens
    sens = 3
    print(x,y)
    if y>3 :
        if (str(Cases[x][y-1])!="1") and (str(Cases[x][y-1]) != "2"):
            y=y-1
        reload()
    else :
        reload()
        gamec.create_image(128, 128, anchor=NW, image=block)
    
def up(event) :
    global gui
    if gui.y > 0:
        gui.y = gui.y - 64
    reload()
    print('up')
    
def down(event) :
    global gui
    if gui.y <576 :
        gui.y=gui.y+64
    reload()
    print('down')
    
def right(event) :
    global gui
    if gui.x<576 :
        gui.x = gui.x + 64
    reload()
    print('right')
    
def left(event) :
    global gui
    if gui.x>320 :
        gui.x = gui.x - 64
    reload()
    print('left')
    
gamec.bind("<Key-d>", d)
gamec.bind("<Key-q>", q)
gamec.bind("<Key-z>", z)
gamec.bind("<Key-s>", s)

gamec.bind("<Up>", up)
gamec.bind("<Down>", down)
gamec.bind("<Left>", left)
gamec.bind("<Right>", right)

def point(event):
    global sens
    global x
    global y
    print(str(sens))
    if sens == 1 :
        if str(Cases[x][y+1])=="1" :
            Cases[x][y+1]=0
            reload()
    elif sens == 2 :
        if str(Cases[x+1][y])=="1" :
            Cases[x+1][y]=0
            reload()
    elif sens == 3 :
        if str(Cases[x][y-1])=="1" :
            Cases[x][y-1]=0
            reload()
    elif sens == 4:
        if str(Cases[x-1][y])=="1" :
            Cases[x-1][y]=0
            reload()
gamec.bind("<Button-1>",point)
gamec.bind("<space>",point)
reload()

while True :
    gamec.focus_set()
    gamec.update()
    gamec.pack()
    game.update()
    gamec.pack()
game.mainloop()
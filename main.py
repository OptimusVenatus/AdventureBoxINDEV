import random
from tkinter import *
Cases = []
for i in range(200) :
    Cases.append([0]*200)
for i in range(4000) :
    Cases[random.randint(1,199)][random.randint(1,199)] = "1"
    Cases[random.randint(1,199)][random.randint(1,199)] = "2"
comd=0
sens=3
############
#00000
#00000
#00#00
#00000
#00000


#   y+1
#x-1#x+1
#   y-1
#############
i=0
game = Tk()
game.resizable(width=False,height=False)
game.title("adventure box")
game.geometry("320x384")

gamec = Canvas(game,width=1000, height=1000)
water = PhotoImage(file="assets/textures/terrain/water.png")
treegrass = PhotoImage(file="assets/textures/terrain/treegrass.png")
grass = PhotoImage(file="assets/textures/terrain/grass.png")
tux = PhotoImage(file="assets/textures/terrain/tux.png")

d1=PhotoImage(file="assets/textures/terrain/1.png")
d2=PhotoImage(file="assets/textures/terrain/2.png")
d3=PhotoImage(file="assets/textures/terrain/3.png")
d4=PhotoImage(file="assets/textures/terrain/4.png")

mo = False
xg = 0
yg = 0


x = 100
y = 100
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

def reload():
    global x
    global y
    global cwc
    global xg
    global yg
    cwc=0
    i=0
    xg = 0
    yg = 0
    gamec.delete(ALL)

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
        gamec.create_image(128, 128, anchor=NW, image=tux)
        if sens == 1 :
            gamec.create_image(128, 128, anchor=NW, image=d1)
        elif sens == 2 :
            gamec.create_image(128, 128, anchor=NW, image=d2)
        elif sens == 3 :
            gamec.create_image(128, 128, anchor=NW, image=d3)
        elif sens == 4 :
            gamec.create_image(128, 128, anchor=NW, image=d4)
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

def d(event) :
    global x
    global sens
    sens = 2
    print(x,y)
    if x < 197 :
        if (str(Cases[x+1][y])!="1") and (str(Cases[x+1][y]) != "2"):
            x=x+1
        reload()

def z(event) :
    global y
    global sens
    sens = 1
    print(x,y)
    if y < 197 :
        if (str(Cases[x][y+1])!="1") and (str(Cases[x][y+1]) !="2"):
            y=y+1
        reload()

def s(event) :
    global y
    global sens
    sens = 3
    print(x,y)
    if y>3 :
        if (str(Cases[x][y-1])!="1") and (str(Cases[x][y-1]) != "2"):
            y=y-1
        reload()

gamec.bind("<Key-d>", d)
gamec.bind("<Key-q>", q)
gamec.bind("<Key-z>", z)
gamec.bind("<Key-s>", s)
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
reload()

while True :
    gamec.focus_set()
    gamec.update()
    gamec.pack()
    game.update()
    gamec.pack()
game.mainloop()
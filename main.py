import random
from tkinter import *
Cases = []
for i in range(200) :
    Cases.append([0]*200)
for i in range(13333) :
    Cases[random.randint(1,199)][random.randint(1,199)] = "1"
    Cases[random.randint(1,199)][random.randint(1,199)] = "2"

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
game.geometry("1000x800")

gamec = Canvas(game,width=1000, height=800)
water = PhotoImage(file="assets/textures/terrain/water.png")
treegrass = PhotoImage(file="assets/textures/terrain/treegrass.png")
grass = PhotoImage(file="assets/textures/terrain/grass.png")
tux = PhotoImage(file="assets/textures/terrain/tux.png")

mo = False
xg = 0
yg = 0


x = 100
y = 100
lgn1 = str(Cases[x-2][y+2]) + str(Cases[x-1][y+2]) + str(Cases[x][y+2]) + str(Cases[x+1][y+2]) + str(Cases[x+2][y+2])
lgn2 = str(Cases[x-2][y+1]) + str(Cases[x-1][y+1]) + str(Cases[x][y+1]) + str(Cases[x+1][y+1]) + str(Cases[x+1][y+1])
lgn3 = str(Cases[x-2][y]) + str(Cases[x-1][y]) + str(Cases[x][y]) + str(Cases[x+1][y]) + str(Cases[x+2][y])
lgn4 = str(Cases[x-2][y-1]) + str(Cases[x-1][y-1]) + str(Cases[x][y-1]) + str(Cases[x+1][y-1]) + str(Cases[x+2][y-1])
lgn5 = str(Cases[x-2][y-2]) + str(Cases[x-1][y-2]) + str(Cases[x][y-2]) + str(Cases[x+1][y-2]) + str(Cases[x+2][y-2])
cwc = 0

print(lgn1)
print(lgn2)
print(lgn3)
print(lgn4)
print(lgn5)
#0=herbe / 1=arbre / 2=cochon

for i in range(29) :
    affw = lgn1 + "/" + lgn2 + "/" +lgn3 + "/" + lgn4 + "/" +lgn5 + "*"
    b = affw[cwc]
    if cwc == 14:
        xg = xg + 64
        if b == "0" :
            gamec.create_image(xg, yg, anchor=NW, image=grass)
        elif b == "1" :
            gamec.create_image(xg, yg, anchor=NW, image=treegrass)
        elif b == "2" :
            gamec.create_image(xg, yg, anchor=NW, image=water)

        gamec.create_image(xg, yg, anchor=NW, image=tux)
        cwc = cwc +1

    elif b == "/" :
        cwc=cwc+1
        yg = yg + 64
        xg = 0
    elif b == "0" :
        cwc = cwc + 1
        xg = xg + 64
        gamec.create_image(xg, yg, anchor=NW, image=grass)
    elif b == "1" :
        cwc = cwc + 1
        xg = xg + 64
        gamec.create_image(xg, yg, anchor=NW, image=treegrass)
    elif b == "2" :
        cwc = cwc + 1
        xg = xg + 64
        gamec.create_image(xg, yg, anchor=NW, image=water)



gamec.pack()
game.mainloop()
import tkinter as tk
from PIL import Image,ImageTk
import Game as game
import time

app = tk.Tk()
app.geometry("800x800")

button = []
positionX = [110, 310, 510]
turn = 0
parner = True

def menu():
    global button
    button = []
    img = Image.open('img/menu1.png')
    img = img.resize((639, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    button.append(tk.Label(app, image = img))
    button[0].place(x = 80, y = 50)

    img2 = Image.open('img/menu2.png')
    img2 = img2.resize((432, 141), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    button.append( tk.Button(app, image=img2, width=432, height=141, compound="c", relief="flat", borderwidth=5, command=lambda: conAmigo(1)) ) 
    button[1].place(x = 183, y = 370)

    img3 = Image.open('img/menu3.png')
    img3 = img3.resize((632, 141), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    button.append(tk.Button( app, image=img3, width=632, height=141, compound="c", relief="flat", borderwidth=5, command=lambda: conAmigo(0)) ) 
    button[2].place(x = 84, y = 521)

    app.mainloop()

def table():
    global turn
    turn = 0
    img = Image.open('img/cube.png')
    img = img.resize((190, 190), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    game.again()
    button.clear()
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(1)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(2)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(3)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(4)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(5)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(6)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(7)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(8)))
    button.append(tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5, command=lambda: movement(9)))


    for i in range (0,9):
        button[i].place(x= positionX[i%3], y = positionX[i//3])
    
    app.mainloop()

def clearall():
    for i in button:
            i.destroy()

def ganaX():
    img = Image.open('img/GanaX.png')
    img = img.resize((800, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    background = tk.Label(image = img)
    background.place(x = 0, y = 0)
    app.update()
    time.sleep(2)
    background.destroy()
    menu()

def ganaO():
    img = Image.open('img/GanaO.png')
    img = img.resize((800, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    background = tk.Label(image = img)
    background.place(x = 0, y = 0)
    app.update()
    time.sleep(2)
    background.destroy()
    menu()

def empate():
    img = Image.open('img/Empate.png')
    img = img.resize((800, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    background = tk.Label(image = img)
    background.place(x = 0, y = 0)
    app.update()
    time.sleep(2)
    background.destroy()
    menu()

def conAmigo(i):
    global parner 
    if i == 0:
        parner = False
    else:
        parner = True

    clearall()
    table()

def movement(i):
    global turn 
    global parner

    if (turn%2 == 0 or parner):
        game.move(i-1, 1)
        img = Image.open('img/X.png')
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        button[i-1].destroy()
        button[i-1] = tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5)
        button[i-1].place(x= positionX[(i-1)%3], y = positionX[(i-1)//3])
        turn = turn + 1
        
        if game.win(1):
            app.update()
            time.sleep(1.5)
            print("GANA X")
            clearall()
            ganaX() 
        elif parner and turn <9:
            movementMachine(game.machine())
        app.mainloop()
    
    else: 
        game.move(i-1, 2)
        img = Image.open('img/circulo.png')
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        button[i-1].destroy()
        button[i-1] = tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5)
        button[i-1].place(x= positionX[(i-1)%3], y = positionX[(i-1)//3])
        turn = turn + 1
        if turn >= 9:
            app.update()
            time.sleep(1.5)
            print ("Empate")
            clearall()
            empate()
        else:
            if game.win(2):
                app.update()
                time.sleep(1.5)
                print("GANA O")
                clearall()
                ganaO()
        app.mainloop()
                

def movementMachine(i):
    img = Image.open('img/circulo.png')
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    button[i].destroy()
    button[i] = tk.Button(app, image=img, width=200, height=200, compound="c", relief="flat", borderwidth=5)
    button[i].place(x= positionX[(i)%3], y = positionX[(i)//3])
    if game.win(2):
        app.update()
        time.sleep(1.5)
        print("GANA O")
        clearall()
        ganaO()
        time.sleep(2)
        table()
    app.mainloop()
   
# table()
menu()
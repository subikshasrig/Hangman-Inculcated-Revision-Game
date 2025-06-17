import tkinter as tk
from random import choice
import csv
import pickle

h1='''
  +---+
      |
      |
      |
      |
      |
========='''
h2='''
  +---+
  |   |
      |
      |
      |
      |
========='''
h3='''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
h4='''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
h5='''
   +---+
   |   |
   O   |
 //|   |
       |
       |
========='''
h6='''
   +---+
   |   |
   O   |
 //|\\  |
       |
       |
========='''
h7='''
   +---+
   |   |
   O   |
 //|\\  |
 //    |
       |
========='''
h8='''
   +---+
   |   |
   O   |
 //|\\  | 
 // \\  |
       |
========='''

scores=[0,0,0]

def Phy():
    physics=tk.Tk()
    physics.title('Physics')
    physics['bg']='teal'
    title=tk.Label(master=physics, text='''Welcome to Hangman: Physics! In this revision plan, you will have to guess the term based on the assigned definition. You have 8 chances to fill in the letters, good luck!''', bg='teal', fg='white', height='10', width='60', font=('MV Boli','15'))
    title.pack(fill=tk.BOTH, expand=True)

    game=tk.Frame(master=physics, bg='teal')
    game.rowconfigure(0,weight=1)
    game.columnconfigure([0,1],weight=1)
    game.pack(fill=tk.BOTH, expand=True)

    guess=tk.Label(master=game, text='Guess a letter: ', bg='teal', fg='white', height=1, width=25, font=('MV Boli','15'))
    guess.grid(row=0,column=1)

    image=tk.Label(master=game, text='', bg='teal', fg='white', height=15, width=20, font=('Courier New','10'))
    image.grid(row=0,column=0)

    entry=tk.Entry(master=game, width=5)
    entry.grid(row=0,column=1,sticky='E',padx=40)

    text=tk.Label(master=game, text='', bg='teal', fg='white', font=('MV Boli','15'))
    text.grid(row=0,column=1,sticky='S',padx=20)

    hint=tk.Label(master=physics, text='', bg='teal', fg='white', font=('MV Boli','15'))
    hint.pack(fill=tk.BOTH, expand=True)

    blank=tk.Label(master=game, text='', bg='teal', fg='white', height=1, width=25, font=('MV Boli','15'))
    blank.grid(row=0,column=1,padx=50)

    f=open('Physics.csv','r')
    num=[]
    e=0
    r=csv.reader(f)
    line=0
    for i in r:
        if line!=0:
            e+=1
            num.append(e)
        line+=1
    f.close()

def phy_play():
    start.destroy()
    image['text']=''
    text['text']=''
    blank['text']=''
    hint['text']=''
    replay.pack_forget()

    f=open('Physics.csv','r')
    r=csv.DictReader(f)
    n=choice(num)

    for i in r:
        if str(n)==i['Serial No.']:
            hint['text']=i['Hint']
            Ans=i['Answer']
            num.remove(n)
            break
    ns=''
    for i in Ans:
        ns+=i+' '
    l=ns.split()
    y=''
    for i in s:
        y+='_'
    l1=y.split()
    blank['text']=y
    chance=0

    def phy_yes():
        x=entry.get()
        entry.delete(0,tk.END)
        nx=''
        for i in range(len(l)):
            if l[i]==x.upper():
                l1[i]=x
            nx+=str(l1[i])+' '
        blank['text']=nx
        text['text']=''

    def phy_enter():
        x=entry.get()
        if x.upper() in Ans:
            phy_yes()
        else:
            entry.delete(0,tk.END)
            text['text']='The letter does not belong in the word.'
            nonlocal chance
            chance+=1
            if chance==1:
                image['text']=h1
            elif chance==2:
                image['text']=h2
            elif chance==3:
                image['text']=h3
            elif chance==4:
                image['text']=h4
            elif chance==5:
                image['text']=h5
            elif chance==6:
                image['text']=h6
            elif chance==7:
                image['text']=h7
            elif chance==8:
                image['text']=h8
                text['text']='Game over. The term was: ' + s
                submit.destroy()
                replay.pack()
        if blank['text'].upper()==ns:
            text['text']='You are well-versed in the concept!'
            scores[0]+=1
            submit.destroy()
            replay.pack()

    submit=tk.Button(master=game, text='Enter', command=phy_enter)
    submit.grid(row=0,column=1,sticky='E',pady=20)
    f.close()

start=tk.Button(master=game,text='Start',command=phy_play)
start.grid(row=0,column=0)
replay=tk.Button(master=hphysics,text='Play Again',command=phy_play)
replay.pack_forget()
physics.mainloop()
  








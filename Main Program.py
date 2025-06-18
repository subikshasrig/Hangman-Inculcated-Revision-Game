import tkinter as tk, csv, pickle, os
from random import choice
from tabulate import tabulate
from Player_Module import *
from Admin_Module import *
import mysql.connector

window=tk.Tk()

greeting=tk.Label(master=window, text='Welcome to Revision!', bg='indigo', fg='cyan', width=60, font=('Cascadia Code' '25'))
greeting.pack(fill=tk.BOTH, expand=True)

login_window=tk.Tk()
login_window.withdraw()
player_window=tk.Tk()
player_window.withdraw()
admin_window=tk.Tk()
admin_window.withdraw()

flag='green' #for login window
x=''

def Next():
    menu_label=tk.Label(master=menu, text='Login as:', bg='indigo', fg='cyan', height=1, font=('Cascadia Code' '25'))
    menu_label.grid(row=2, column=0)
    menu_pl=tk.Button(master=menu, text='Player', command=Play)
    menu_pl.grid(row=2, column=0, sticky='E', padx=40)
    menu_admin=tk.Button(master=menu, text='Admin', command=Ad)
    menu_admin.grid(row=2, column=1, sticky='W')
    menu_quit=tk.Button(master=menu, text='Quit', command=Quit)
    menu_quit.grid(row=2, column=0, sticky='W')
    menu_show=tk.Button(master=menu, text='Show Leaderboard', command=Show)
    menu_show.grid(row=3, column=0, sticky='W')

def Back():
    window.deiconify()

def Quit():
    obj=mysql.connector.connect(host='localhost', user='root', database='PROJECT', password='@Bcd3fghi')
    c=obj.cursor()
    window.destroy()
    player_window.destroy()
    admin_window.destroy()
    total=sum(scores)
    scores.append(total)
    scores.insert(0,x)
    t=tuple(scores)
    c.execute('INSERT INTO LEADERBOARD VALUES(%s,%s,%s,%s,%s)',t)
    obj.commit()
    obj.close()
    c.close()

def Show():
    obj=mysql.connector.connect(host='localhost', user='root', database='PROJECT', password='@Bcd3fghi')
    c=obj.cursor()
    c.execute('SELECT * FROM LEADERBOARD ORDER BY TOTAL DESC')
    l=c.fetchall()
    l.insert(0,['PLAYER','PHYSICS','CHEMISTRY','ENGLISH','TOTAL'])
    table=tabulate(l,headers='firstrow',tablefmt='grid')
    print(table)
    c.close()
    obj.close()

def Login():
    global flag
    global x
    flag='red'
    x=login_name.get()
    login_window.destroy()
    player_window.deiconify()
    print(x)

def Play():
    window.withdraw()
    if flag=='green':
        login_window.deiconify()
    else:
        player_window.deiconify()

def Back_p():
    player_window.withdraw()
    Back()

def Ad():
    window.withdraw()
    admin_window.deiconify()

def Back_a():
    admin_window.withdraw()
    Back()

player_window['bg']='indigo'
player=tk.Frame(master=player_window, bg='indigo')
player.pack(fill=tk.BOTH, expand=True)
play_label=tk.Label(master=player, text='Which game do you want to play?', bg='indigo', fg='cyan', height=1, font=('Cascadia Code' '25'))
play_label.pack(fill=tk.BOTH, expand=True)
play_physics=tk.Button(master=player, text='Physics', bg='teal', fg='white', font=('MV Boli', '15'), command=Phy)
play_physics.grid(row=2, column=0, sticky='E', padx=250, pady=250)
play_chemistry=tk.Button(master=player, text='Chemistry', bg='lavender', fg='navy blue', font=('MV Boli', '15'), command=Chem)
play_chemistry.grid(row=2, column=1, sticky='W', padx=150, pady=250)
play_english=tk.Button(master=player, text='English', bg='pink', fg='purple', font=('MV Boli', '15'), command=Eng)
play_english.grid(row=2, column=2, sticky='W', padx=250, pady=250)
back_player=tk.Button(master=player_window, text='Back', command=Back_p)
back_player.pack()

admin_window['bg']='indigo'
admin=tk.Frame(master=admin_window, bg='indigo')
admin.pack(fill=tk.BOTH, expand=True)
ad_label=tk.Label(master=admin_window, text='Which game do you want to edit?', bg='indigo', fg='cyan', height=1, font=('Cascadia Code' '25'))
ad_label.pack(fill=tk.BOTH, expand=True)
ad_phylabel=tk.Label(master=admin, text='Physics', bg='indigo', fg='cyan', height=1, font=('Cascadia Code' '15'))
ad_phylabel.grid(row=0, column=0, sticky='E', padx=250, pady=50)
ad_aphysics=tk.Label(master=admin, text='Add', bg='teal', fg='white', font=('MV Boli' '15'), command=AdPhy)
ad_aphysics.grid(row=1, column=0, sticky='E', padx=250, pady=50)
ad_rphysics=tk.Label(master=admin, text='Remove', bg='teal', fg='white', font=('MV Boli' '15'), command=RePhy)
ad_rphysics.grid(row=2, column=0, sticky='E', padx=250, pady=50)
ad_vphysics=tk.Label(master=admin, text='View File', bg='teal', fg='white', font=('MV Boli' '15'), command=VPhy)
ad_vphysics.grid(row=3, column=0, sticky='E', padx=250, pady=50)

ad_chemlabel=tk.Label(master=admin, text='Chemistry', bg='indigo', fg='cyan', height=1, font=('Cascadia Code' '15'))
ad_chemlabel.grid(row=0, column=1, sticky='W', padx=150, pady=50)
ad_achemistry=tk.Label(master=admin, text='Add', bg='lavender', fg='navy blue', font=('MV Boli' '15'), command=AdChem)
ad_achemistry.grid(row=1, column=1, sticky='W', padx=150, pady=50)
ad_rchemistry=tk.Label(master=admin, text='Remove', bg='lavender', fg='navy blue', font=('MV Boli' '15'), command=ReChem)
ad_rchemistry.grid(row=2, column=1, sticky='W', padx=150, pady=50)
ad_vchemistry=tk.Label(master=admin, text='View File', bg='lavender', fg='navy blue', font=('MV Boli' '15'), command=VChem)
ad_vchemistry.grid(row=3, column=1, sticky='W', padx=150, pady=50)

ad_englabel=tk.Label(master=admin, text='English', bg='indigo', fg='cyan', height=1, font=('Cascadia Code' '15'))
ad_englabel.grid(row=0, column=1, sticky='W', padx=250, pady=50)
ad_aenglish=tk.Label(master=admin, text='Add', bg='pink', fg='purple', font=('MV Boli' '15'), command=AdEng)
ad_aenglish.grid(row=1, column=2, sticky='W', padx=250, pady=50)
ad_renglish=tk.Label(master=admin, text='Remove', bg='pink', fg='purple', font=('MV Boli' '15'), command=ReEng)
ad_renglish.grid(row=2, column=2, sticky='W', padx=250, pady=50)
ad_venglish=tk.Label(master=admin, text='View File', bg='pink', fg='purple', font=('MV Boli' '15'), command=VEng)
ad_venglish.grid(row=3, column=2, sticky='W', padx=250, pady=50)

back_admin=tk.Button(master=admin_window, text='Back', command=Back_a)
back_admin.pack()

menu=tk.Frame(master=window, bg='indigo')
menu.rowconfigure([0,1,2], minsize=2, weight=1)
menu.columnconfigure([0,1], minsize=1, weight=1)
menu.pack(fill=tk.BOTH, expand=True)
menu_next=tk.Button(master=menu, text='Next', command=Next)
menu_next.grid(row=2, column=0)

login_window['bg']='indigo'
login_label=tk.Label(master=login_window, text='Enter Username: ', bg='indigo', fg='cyan', height=1, font=('Cascadia Code' '15'))
login_label.pack(fill=tk.BOTH, expand=True)

l_user=tk.Frame(master=login_window, bg='indigo')
l_user.pack(fill=tk.BOTH, exapnd=True)

login_name=tk.Entry(master=l_user, width=20)
login_name.grid(row=1, column=0, sticky='E', padx=250)

login=tk.Button(master=l_user, text='Login', command=Login)
login.grid(row=2, column=0, pady=250)













#!/usr/bin/env python
# coding: utf-8

# In[19]:


import sys
import datarc_basic as dab
import datarc_medium as dam
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import * 
from functools import partial
from tkinter import filedialog


# In[45]:


def inputTable(username, password, host, database):
    filename = filedialog.askopenfilename()
    table = dam.xlsx_to_csv(filename, "temp")
    db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
    dam.whole_table_input(db, table)
    db.commit()
    db.close()
    messagebox.showinfo(title="Message", message="Upload successful!")
    return

def inputRank(username, password, host, database, rank, idnum):
    db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
    dam.update_rank_other_info(db, idnum.get(), rank.get())
    db.commit()
    db.close()
    messagebox.showinfo(title="Message", message="Rank input successful!")
    return

def Close():
    tkWindow.destroy()

#window
tkWindow = Tk()  
tkWindow.geometry('400x530')  
tkWindow.title('VT-ARC Database Input Management Panel')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").place(x = 170, y = 10)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x = 130, y = 40)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").place(x = 172, y = 70)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x = 130, y = 100)

#hostlabel and host entry box
hostLabel = Label(tkWindow,text="Host").place(x = 182, y = 130)
host = StringVar()
hostEntry = Entry(tkWindow, textvariable=host).place(x = 130, y = 160)

#databaselabel and database entry box
databaseLabel = Label(tkWindow,text="Database").place(x = 172, y = 190)
database = StringVar()
databaseEntry = Entry(tkWindow, textvariable=database).place(x = 130, y = 220)

#idlabel and id entry box
idLabel = Label(tkWindow,text="ID").place(x = 186, y = 300)
idnum = StringVar()
idEntry = Entry(tkWindow, textvariable=idnum).place(x = 130, y = 330)

#ranklabel and rank id box
rankLabel = Label(tkWindow,text="Rank").place(x = 182, y = 360)
rank = StringVar()
rankEntry = Entry(tkWindow, textvariable=rank).place(x = 130, y = 390)

inputTable = partial(inputTable, username, password, host, database)
inputRank = partial(inputRank, username, password, host, database, rank, idnum)

#input table button
inputTableButton = Button(tkWindow, text="Upload Table", command=inputTable).place(x = 155, y = 260)

#input rank button
inputRankButton = Button(tkWindow, text="Input Rank", command=inputRank).place(x = 160, y = 430)
Button(tkWindow, text= "Quit", command=Close).place(x = 180, y = 480)

tkWindow.resizable(False,False)
tkWindow.mainloop()


# In[ ]:





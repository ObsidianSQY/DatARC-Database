#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datarc_basic as dab
import datarc_medium as dam
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import * 
from functools import partial
from tkinter import filedialog


# In[2]:


def delete_row():
    db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
    dam.delete_uniq(db, uni_idnum.get())

def updateInfo():
    db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
    try:
        if not rank.get() == "":
            dam.update_rank_other_info(db, uni_idnum.get(), rank.get(), False)

        if not rankvtac.get() == "":
            dam.update_rank_vtarc_info(db, uni_idnum.get(), rankvtac.get(), False)

        if not just.get() == "":
            dam.update_just_info(db, uni_idnum.get(), just.get(), False)

        if not source.get() == "":
            dam.update_source_info(db, uni_idnum.get(), source.get(), False)

        if not name.get() == "":
            dam.update_name_info(db, uni_idnum.get(), name.get(), False)

        if not lname.get() == "":
            dam.update_last_name_info(db, uni_idnum.get(), lname.get(), False)

        if not inst.get() == "":
            dam.update_institution_info(db, uni_idnum.get(), inst.get(), False)

        if not title.get() == "":
            dam.update_title_info(db, uni_idnum.get(), title.get(), False)

        if not domain.get() == "":
            dam.update_domain_info(db, uni_idnum.get(), domain.get(), False)

        if not gender.get() == "":
            dam.update_gender_info(db, uni_idnum.get(), gender.get(), False)

        if not topic.get() == "":
            dam.update_topic_info(db, uni_idnum.get(), topic.get(), False)

        if not descrip.get() == "":
            dam.update_description_info(db, uni_idnum.get(), descrip.get(), False)

        if not field.get() == "":
            dam.update_fields_info(db, uni_idnum.get(), field.get(), False)

        if not keynotes.get() == "":
            dam.update_key_notes_info(db, uni_idnum.get(), keynotes.get(), False)

        if not links.get() == "":
            dam.update_links_info(db, uni_idnum.get(), links.get(), False)

        if not email.get() == "":
            dam.update_email_info(db, uni_idnum.get(), email.get(), False)

        if not website.get() == "":
            dam.update_website_info(db, uni_idnum.get(), website.get(), False)

        if not pub.get() == "":
            dam.update_pub_info(db, uni_idnum.get(), pub.get(), False)

        if not cite.get() == "":
            dam.update_citation_info(db, uni_idnum.get(), cite.get(), False)

        if not h.get() == "":
            dam.update_hindex(db, uni_idnum.get(), h.get(), False)

        if not h5.get() == "":
            dam.update_h5index_info(db, uni_idnum.get(), h5.get(), False)

        if not intid.get() == "":
            dam.update_actualid_info(db, uni_idnum.get(), intid.get(), False)
        db.commit()
        db.close()
        messagebox.showinfo(title="Message", message="Information update successful!")
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_row():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.delete_uniq(db, uni_idnum.get())
        db.commit()
        db.close()
        msg = "Row at Unique ID " +  uni_idnum.get()  + " cleared successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_rank_other():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_rank_other_info(db, uni_idnum.get(), rank.get(), True)
        db.commit()
        db.close()
        msg = "Clear Rank Other at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_rank_vtarc():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_rank_vtarc_info(db, uni_idnum.get(), rankvtac.get(), True)
        db.commit()
        db.close()
        msg = "Clear Rank VT-ARC at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_rank_just():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_just_info(db, uni_idnum.get(), just.get(), True)
        db.commit()
        db.close()
        msg = "Clear Rank Justification at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            

def del_source():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_source_info(db, uni_idnum.get(), source.get(), True)
        db.commit()
        db.close()
        msg = "Clear Source at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            
                            
def del_name():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_name_info(db, uni_idnum.get(), name.get(), True)
        db.commit()
        db.close()
        msg = "Clear Name at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return 
                            
def del_lname():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_last_name_info(db, uni_idnum.get(), lname.get(), True)
        db.commit()
        db.close()
        msg = "Clear Last Name at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return 

def del_inst():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_institution_info(db, uni_idnum.get(), inst.get(), True)
        db.commit()
        db.close()
        msg = "Clear Institution at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                             

def del_title():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_title_info(db, uni_idnum.get(), title.get(), True)
        db.commit()
        db.close()
        msg = "Clear Title at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            

def del_domain():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_domain_info(db, uni_idnum.get(), domain.get(), True)
        db.commit()
        db.close()
        msg = "Clear Domain at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return    
                            
def del_gender():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_gender_info(db, uni_idnum.get(), gender.get(), True)
        db.commit()
        db.close()
        msg = "Clear Gender at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_topic():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_topic_info(db, uni_idnum.get(), topic.get(), True)
        db.commit()
        db.close()
        msg = "Clear Topic at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            

def del_desc():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_description_info(db, uni_idnum.get(), descrip.get(), True)
        db.commit()
        db.close()
        msg = "Clear Description at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_fields():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_fields_info(db, uni_idnum.get(), field.get(), True)
        db.commit()
        db.close()
        msg = "Clear Fields at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return   
                            
def del_keynote():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_key_notes_info(db, uni_idnum.get(), keynotes.get(), True)
        db.commit()
        db.close()
        msg = "Clear Key Notes at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_links():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_links_info(db, uni_idnum.get(), links.get(), True)
        db.commit()
        db.close()
        msg = "Clear Links at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_email():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_email_info(db, uni_idnum.get(), email.get(), True)
        db.commit()
        db.close()
        msg = "Clear E-mail at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_website():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_website_info(db, uni_idnum.get(), website.get(), True)
        db.commit()
        db.close()
        msg = "Clear Website at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_pub():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_pub_info(db, uni_idnum.get(), pub.get(), True)
        db.commit()
        db.close()
        msg = "Clear Pub at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_cite():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_citation_info(db, uni_idnum.get(), cite.get(), True)
        db.commit()
        db.close()
        msg = "Clear Citation at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_hindex():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_hindex(db, uni_idnum.get(), h.get(), True)
        db.commit()
        db.close()
        msg = "Clear H-index at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_h5index():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_h5index_info(db, uni_idnum.get(), h5.get(), True)
        db.commit()
        db.close()
        msg = "Clear H5-index at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_id():
    try:
        db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
        dam.update_actualid_info(db, uni_idnum.get(), intid.get(), True)
        db.commit()
        db.close()
        msg = "Clear ID at Unique ID " +  uni_idnum.get()  + " successful!"
        messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def Close():
    tkWindow.destroy()
    

def inputTable():
    filename = filedialog.askopenfilename()
    table = dam.xlsx_to_csv(filename, "temp")
    db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
    try:
        dam.whole_table_input(db, table)
        db.commit()
        db.close()
        messagebox.showinfo(title="Message", message="Upload successful!")
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
    
def inputHandInfo():
    db = dam.mysql_connect(host.get(), username.get(), password.get(), database.get())
    try:
        dam.handle_input(db, rank.get(), rankvtac.get(), just.get(), source.get(), name.get(), lname.get(), inst.get(), title.get(), domain.get(), gender.get(), topic.get(), descrip.get(), field.get(), keynotes.get(), links.get(), email.get(), website.get(), pub.get(), cite.get(), h.get(), h5.get(), intid.get())
        db.commit()
        db.close()
        messagebox.showinfo(title="Message", message="Information input successful!")
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

#window
tkWindow = Tk()  
tkWindow.geometry('1300x600')   
tkWindow.title('VT-ARC Database Input Management Panel')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").place(x = 170, y = 60)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x = 130, y = 90)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").place(x = 172, y = 120)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x = 130, y = 150)

#hostlabel and host entry box
hostLabel = Label(tkWindow,text="Host").place(x = 182, y = 180)
host = StringVar()
hostEntry = Entry(tkWindow, textvariable=host).place(x = 130, y = 210)

#databaselabel and database entry box
databaseLabel = Label(tkWindow,text="Database").place(x = 172, y = 240)
database = StringVar()
databaseEntry = Entry(tkWindow, textvariable=database).place(x = 130, y = 270)

#idlabel and id entry box
idLabel = Label(tkWindow,text="Unique ID").place(x = 800, y = 10)
uni_idnum = StringVar()
idEntry = Entry(tkWindow, textvariable=uni_idnum).place(x = 760, y = 40)
                            
Button(tkWindow, text= "X", command=del_row).place(x = 890, y = 35)

#ranklabel and rank id box
rankLabel = Label(tkWindow,text="Rank").place(x = 460, y = 70)
rank = StringVar()
rankEntry = Entry(tkWindow, textvariable=rank).place(x = 460, y = 100)
                            
Button(tkWindow, text= "X", command=del_rank_other).place(x = 590, y = 95)

#rankarclabel and rankarc box
rankvtacLable = Label(tkWindow,text="Rank (VT-ARC)").place(x = 460, y = 130)
rankvtac = StringVar()
rankvtacEntry = Entry(tkWindow, textvariable=rankvtac).place(x = 460, y = 160)
                            
Button(tkWindow, text= "X", command=del_rank_vtarc).place(x = 590, y = 155)

#rankjustificationlabel and box
justLable = Label(tkWindow,text="Rank Justification").place(x = 460, y = 190)
just = StringVar()
justEntry = Entry(tkWindow, textvariable=just).place(x = 460, y = 220)

Button(tkWindow, text= "X", command=del_rank_just).place(x = 590, y = 215)

#sourcelabel and box
sourceLable = Label(tkWindow,text="Source").place(x = 460, y = 250)
source = StringVar()
sourceEntry = Entry(tkWindow, textvariable=source).place(x = 460, y = 280)

Button(tkWindow, text= "X", command=del_source).place(x = 590, y = 275)

#namelabel and box
nameLable = Label(tkWindow,text="Name").place(x = 460, y = 310)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name).place(x = 460, y = 340)

Button(tkWindow, text= "X", command=del_name).place(x = 590, y = 335)
                            
#lastnamelabel and box
lnameLable = Label(tkWindow,text="Last Name").place(x = 460, y = 370)
lname = StringVar()
lnameEntry = Entry(tkWindow, textvariable=lname).place(x = 460, y = 400)

Button(tkWindow, text= "X", command=del_lname).place(x = 590, y = 395)                        
                            
#institutionlabel and box
instLable = Label(tkWindow,text="Institution").place(x = 460, y = 430)
inst = StringVar()
instEntry = Entry(tkWindow, textvariable=inst).place(x = 460, y = 460)

Button(tkWindow, text= "X", command=del_inst).place(x = 590, y = 455)                            
                            
#titlelabel and box
titleLable = Label(tkWindow,text="Title").place(x = 760, y = 70)
title = StringVar()
titleEntry = Entry(tkWindow, textvariable=title).place(x = 760, y = 100)

Button(tkWindow, text= "X", command=del_title).place(x = 890, y = 95)                            
                            
#domainlabel and box
domainCLable = Label(tkWindow,text="Domain").place(x = 760, y = 130)
domain = StringVar()
domainEntry = Entry(tkWindow, textvariable=domain).place(x = 760, y = 160)

Button(tkWindow, text= "X", command=del_domain).place(x = 890, y = 155)                            
                            
#genderlabel and box
genderLable = Label(tkWindow,text="Gender").place(x = 760, y = 190)
gender = StringVar()
genderEntry = Entry(tkWindow, textvariable=gender).place(x = 760, y = 220)

Button(tkWindow, text= "X", command=del_gender).place(x = 890, y = 215)                            
                            
#topiclabel and box
topicLable = Label(tkWindow,text="Topic").place(x = 760, y = 250)
topic = StringVar()
topicEntry = Entry(tkWindow, textvariable=topic).place(x = 760, y = 280)

Button(tkWindow, text= "X", command=del_topic).place(x = 890, y = 275)                            
                            
#descriptionlabel and box
descripLable = Label(tkWindow,text="Description").place(x = 760, y = 310)
descrip = StringVar()
descripEntry = Entry(tkWindow, textvariable=descrip).place(x = 760, y = 340)

Button(tkWindow, text= "X", command=del_desc).place(x = 890, y = 335)                            
                            
#fieldlabel and box
fieldARCLable = Label(tkWindow,text="Fields").place(x = 760, y = 370)
field = StringVar()
fieldEntry = Entry(tkWindow, textvariable=field).place(x = 760, y = 400)

Button(tkWindow, text= "X", command=del_fields).place(x = 890, y = 395)                            
                            
#keynoteslabel and box
keynotesLable = Label(tkWindow,text="Key Notes").place(x = 760, y = 430)
keynotes = StringVar()
keynotesEntry = Entry(tkWindow, textvariable=keynotes).place(x = 760, y = 460)

Button(tkWindow, text= "X", command=del_keynote).place(x = 890, y = 455)                            
                            
#linkslabel and box
linksLable = Label(tkWindow,text="Links").place(x = 1060, y = 70)
links = StringVar()
linksEntry = Entry(tkWindow, textvariable=links).place(x = 1060, y = 100)

Button(tkWindow, text= "X", command=del_links).place(x = 1190, y = 95)                            
                            
#emaillabel and box
emailLable = Label(tkWindow,text="E-mail").place(x = 1060, y = 130)
email = StringVar()
emailEntry = Entry(tkWindow, textvariable=email).place(x = 1060, y = 160)

Button(tkWindow, text= "X", command=del_email).place(x = 1190, y = 155)                            
                            
#websitelabel and box
websiteLable = Label(tkWindow,text="Website").place(x = 1060, y = 190)
website = StringVar()
websiteEntry = Entry(tkWindow, textvariable=website).place(x = 1060, y = 220)

Button(tkWindow, text= "X", command=del_website).place(x = 1190, y = 215)                            
                            
#publabel and box
pubLable = Label(tkWindow,text="Pub").place(x = 1060, y = 250)
pub = StringVar()
pubEntry = Entry(tkWindow, textvariable=pub).place(x = 1060, y = 280)

Button(tkWindow, text= "X", command=del_pub).place(x = 1190, y = 275)                            
                            
#citationlabel and box
citeLable = Label(tkWindow,text="Citation").place(x = 1060, y = 310)
cite = StringVar()
citeEntry = Entry(tkWindow, textvariable=cite).place(x = 1060, y = 340)

Button(tkWindow, text= "X", command=del_cite).place(x = 1190, y = 335)                            
                            
#hindexlabel and box
hLable = Label(tkWindow,text="H index").place(x = 1060, y = 370)
h = StringVar()
hEntry = Entry(tkWindow, textvariable=h).place(x = 1060, y = 400)

Button(tkWindow, text= "X", command=del_hindex).place(x = 1190, y = 395)                            
                            
#h5indexlabel and box
h5Lable = Label(tkWindow,text="H5 index").place(x = 1060, y = 430)
h5 = StringVar()
h5Entry = Entry(tkWindow, textvariable=h5).place(x = 1060, y = 460)

Button(tkWindow, text= "X", command=del_h5index).place(x = 1190, y = 455)                            
                            
#idlabel and box
idLable = Label(tkWindow,text="ID").place(x = 760, y = 490)
intid = StringVar()
idEntry = Entry(tkWindow, textvariable=intid).place(x = 760, y = 520)

Button(tkWindow, text= "X", command=del_id).place(x = 890, y = 515)                            
                            
Button(tkWindow, text= "Input Information", command=inputHandInfo).place(x = 145, y = 350)
Button(tkWindow, text= "Import Table", command=inputTable).place(x = 155, y = 400)
Button(tkWindow, text= "Update Information", command=updateInfo).place(x = 135, y = 450)
Button(tkWindow, text= "Quit", command=Close).place(x = 180, y = 500)

tkWindow.resizable(False,False)
tkWindow.mainloop()


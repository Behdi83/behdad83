from tkcalendar import DateEntry

from tkinter import *
from tkinter.ttk import Notebook, Treeview
import datetime

import database


def to_year(date):
    m, d, y = date.split('/')
    return '20{}-{}-{}'.format(y.zfill(2), m.zfill(2), d.zfill(2))


def double_click(event):
    def edit():
        database.StudentUpdate(
            t_name.get(),
            t_fname.get(),
            t_IDN.get(),
            t_BD.get(),
            t_color.get(),
            item['text'])
    item_id = event.widget.focus()
    item = event.widget.item(item_id)
    top = Toplevel()
    Label(top,text="name").grid(row=0,column=0)
    t_name = StringVar()
    t_name.set(item['values'][0])
    Entry(top, textvariable=t_name).grid(row=0,column=1)

    Label(top,text="name").grid(row=1,column=0)
    t_fname = StringVar()
    t_fname.set(item['values'][1])
    Entry(top, textvariable=t_fname).grid(row=1,column=1)

    Label(top,text="name").grid(row=2,column=0)
    t_IDN = StringVar()
    t_IDN.set(item['values'][2])
    Entry(top, textvariable=t_IDN).grid(row=2,column=1)

    Label(top,text="name").grid(row=3,column=0)
    t_BD = StringVar()
    t_BD.set(item['values'][3])
    Entry(top, textvariable=t_BD).grid(row=3,column=1)

    Label(top,text="name").grid(row=4,column=0)
    t_color = StringVar()
    t_color.set(item['values'][4])
    Entry(top, textvariable=t_color).grid(row=4,column=1)

    Button(top, text="edit").grid(row=5,column=0,columnspan=2, sticky="nsew")
    Button(top, text="delete", command=edit).grid(row=6,column=0,columnspan=2, sticky="nsew")
    Button(top, text="cancel").grid(row=7,column=0,columnspan=2, sticky="nsew")


def student_insert():
    database.StudentInsert(
        name.get(),
        family.get(),
        idN.get(),
        to_year(birth.get()),
        color.get()
    )
    name.set('')
    family.set('')
    idN.set('')
    birth.set('')
    color.set('')

def search_Student():
    names =database.Studentselect(full_name.get()).get()

    tree = Treeview(s_select)
    tree["columns"]=("one","two","three","four","five")
    tree.column("#0", width=20, minwidth=20, stretch=NO)
    tree.column("one", width=100, minwidth=150, stretch=NO)
    tree.column("two", width=150, minwidth=200)
    tree.column("three", width=80, minwidth=50, stretch=NO)
    tree.column("four", width=80, minwidth=50, stretch=NO)
    tree.column("five", width=40, minwidth=50, stretch=NO)
    tree.heading("#0",text="ID",anchor=W)
    tree.heading("one", text="Name",anchor=W)
    tree.heading("two", text="Family",anchor=W)
    tree.heading("three", text="ID Number",anchor=W)        
    tree.heading("four", text="Birth Date",anchor=W)
    tree.heading("five", text="Class Color",anchor=W)
    tree.grid(row=1, column=0,columnspan=5)
    for name in names:
        tree.insert("",1,text=name[0],values=(name[1], name[2], name[3], name[4], name[5]))
    tree.bind("<Double-Button-1>",double_click)
 








root = Tk()

date = datetime.datetime.now()

note = Notebook()
note.grid(row=0, column=0)

s_insert = Frame()
s_update = Frame()
s_delete = Frame()
s_select = Frame()


note.add(s_insert, text='Student Insert')
note.add(s_update, text='Student Update')
note.add(s_delete, text='Student Delete')
note.add(s_select, text='Student Select')


# ######################################### #
Label(s_insert, text="Name").grid(row=0, column=0)
name = StringVar()
Entry(s_insert, textvariable=name).grid(row=0, column=1)

Label(s_insert, text="Family").grid(row=1, column=0)
family = StringVar()
Entry(s_insert, textvariable=family).grid(row=1, column=1)

Label(s_insert, text="ID N.").grid(row=2, column=0)
idN = StringVar()
Entry(s_insert, textvariable=idN).grid(row=2, column=1)

Label(s_insert, text="B. Date").grid(row=3, column=0)
birth = StringVar()
DateEntry(s_insert, textvariable=birth, year=date.year, month=date.month, 
          day=date.day).grid(row=3, column=1, sticky=W+E)

Label(s_insert, text="C. Color").grid(row=4, column=0)
color = StringVar()
color.set('Red')
OptionMenu(s_insert, color, 'Yellow', 'Red', 'Green', 'Orange').grid(row=4, column=1, sticky=W+E)

Button(s_insert, text='Create', command=student_insert).grid(row=5, column=0, columnspan=2, sticky=W+E)
Button(s_insert, text='Cancel', command=root.destroy).grid(row=6, column=0, columnspan=2, sticky=W+E)
# ######################################### #


Label(s_select,text="Name").grid(row=0,column=0)
full_name=StringVar()
Entry(s_select, textvariable=full_name).grid(row=0,column=1)
Button(s_select,text="search", command=search_Student).grid(row=0,column=2)

root.mainloop()
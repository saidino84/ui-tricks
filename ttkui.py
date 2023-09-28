from tkinter import Tk, ttk
from tkinter.ttk import *


root=Tk()
root.title='Product List comparations'

columns=('id',"date","barcode","description","old_cost","new_cost","difer","obs","invoice","provider")
tree=Treeview(root,columns=columns,show='headings',
              displaycolumns=[0,1,2]
              )
tree.grid(row=1,column=1)
tree.heading('id',text='id')
tree.heading('date',text='date')
tree.heading('barcode',text='barcode')
tree.heading('')

# root.pack()

if __name__=='__main__':
    root.mainloop()
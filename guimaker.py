import pygsheets
path='C:/Users/kyles/Desktop/auth.json'
gc=pygsheets.authorize(service_account_file=path)
sh=gc.open('tester') #opens the file
wk1=sh[0] #selects first sheet
l1=wk1.get_all_values(include_tailing_empty=False)
# Starting of Tkinter window code. 
from tkinter import ttk
import tkinter as tk
# Creating tkinter my_w
my_w = tk.Tk()
my_w.geometry("400x400") 
my_w.title("Patient List")  
# Using treeview widget
trv = ttk.Treeview(my_w, selectmode ='browse')
trv.grid(row=1,column=1,padx=20,pady=20)
# number of columns
trv["columns"] = ("1", "2", "3","4","5")
  
# Defining heading
trv['show'] = 'headings'
trv['height']=15 # Number of rows to display by default. 
# width of columns and alignment 
trv.column("1", width = 80, anchor ='c')
trv.column("2", width = 80, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')
trv.column("5", width = 80, anchor ='c')
  
# Headings  
# respective column heading are taken from google sheets
# if only data is taken from google sheet then below lines can be added
#trv.heading("1", text ="id")
#trv.heading("2", text ="Name")
#trv.heading("3", text ="Class")
#trv.heading("4", text ="Mark")  
#trv.heading("5", text ="Gender")
#trv['displaycolumns']=["1","2","3"]

#adding data to treeview

for data in l1:
    trv.insert('','end', iid=data[0],text=data[0],values=(data[0],data[1],data[2],data[3],data[4]))
my_w.mainloop()
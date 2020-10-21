import tkinter as tk                                    
from OOPbackend import Database                         

database = Database()

class Buttons:
    def get_selected_row(self,event):                        #selecting one entry from the entered data
        try:
            global selected_tuple                       #global variable for selected entries
            index = L1.curselection()[0]                #returns the index(row number) of the currently selected entry, its a tuple containing a single integer entry 
            selected_tuple = L1.get(index)              #getting the entire entry at the index
            e1.delete(0,tk.END)                         #putting the selected entries in the entry boxes
            e1.insert(tk.END,selected_tuple[1])
            e2.delete(0,tk.END)
            e2.insert(tk.END,selected_tuple[2])
            e3.delete(0,tk.END)
            e3.insert(tk.END,selected_tuple[3])
            e4.delete(0,tk.END)
            e4.insert(tk.END,selected_tuple[4])
        except IndexError:                              #not executing if clicking on any place in the list box which is not a entry
            pass

    def view_command(self):                                 #Executing the view all button
        L1.delete(0, tk.END)                            #clearing the list box
        for row in database.view():                      #view function imported from backend.py
            L1.insert(tk.END,row)                       #row wise inserting the values in the listbox

    def search_command(self):                               #Executing the search button
        L1.delete(0, tk.END)                            #clearing the list box
        for row in database.search(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()):          #search function imported from backend.py
            L1.insert(tk.END,row)                       #searching and inserting the entries in list box

    def enter_command(self):                                #executing the enter values in the table
        L1.delete(0, tk.END)                            #clearing the list box
        database.insert(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())                      #insert function imported from backend.py
        L1.insert(tk.END,"INSERTED - ")         
        L1.insert(tk.END,(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()))

    def delete_command(self):                               #delete button function
        database.delete(selected_tuple[0])               #delete function imported from backend.py
        self.view_command()                                  #displaying the whole data base 
        
    def update_command(self):                               #update button function
        database.update(selected_tuple[0],e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())    #update function imported from backend.py
        self.view_command()                                  #displaying the whole data base 

buttons = Buttons()

window = tk.Tk()                                    #opening a window 

window.wm_title("BookStore")                        #window title name

#TITLE 
l1 = tk.Label(window,text = "Title")                #defining the label "Title"
l1.grid(row = 0, column = 0)                        #defining the grid position

e1_title = tk.StringVar()                           #passing the StringVar object in e1_title variable
e1 = tk.Entry(window,textvariable =  e1_title)      #defining the entry box 
e1.grid(row = 0, column = 1)                        #defining the grid position

#AUTHOR
l2 = tk.Label(window,text = "Author")               #defining the label "Author"
l2.grid(row = 0, column = 2)                        #defining the grid position

e2_author = tk.StringVar()                          #passing the StringVar object in e1_title variable
e2 = tk.Entry(window,textvariable =  e2_author)     #defining the entry box 
e2.grid(row = 0, column = 3)                        #defining the grid position

#YEAR
l3 = tk.Label(window,text = "Year")                 #defining the label "Year"
l3.grid(row = 1, column = 0)                        #defining the grid position

e3_year = tk.StringVar()                            #passing the StringVar object in e1_title variable
e3 = tk.Entry(window,textvariable =  e3_year)       #defining the entry box 
e3.grid(row = 1, column = 1)                        #defining the grid position

#ISBN
l4 = tk.Label(window,text = "ISBN")                 #defining the label "ISBN"
l4.grid(row = 1, column = 2)                        #defining the grid position

e4_isbn = tk.StringVar()                            #passing the StringVar object in e1_title variable
e4 = tk.Entry(window,textvariable =  e4_isbn)       #defining the entry box 
e4.grid(row = 1, column = 3)                        #defining the grid position

#LISTBOX
L1 = tk.Listbox(window,height = 20,width = 60)                          #defining the listbox
L1.grid(row = 2, column = 0, rowspan = 5, columnspan = 2)               #defining the grid position

#SCROLL BAR
s1 = tk.Scrollbar(window)                           #defining the scrollbar
s1.grid(row = 2, column = 2, rowspan = 6)           #defining the grid position

s2 = tk.Scrollbar(window,orient = "horizontal")     #defining horizontla scroll
s2.grid(row = 7, column = 0, columnspan = 2)        #defining the grid position

L1.configure(yscrollcommand = s1.set)               #configuring the listbox with the widget scroll in vertical view
s1.configure(command = L1.yview)                    #passing the vertical view command on the scroll

L1.configure(xscrollcommand = s2.set)               #configuring the listbox with the widget scroll in vertical view
s2.configure(command = L1.xview)                    #passing the vertical view command on the scroll

L1.bind('<<ListboxSelect>>',buttons.get_selected_row)       #Bind to this widget at event ListboxSelect a call to function get_selected_row.

#VIEW ALL BUTTON
b1 = tk.Button(window, text="View All",width = 15,command = buttons.view_command)               #view all button
b1.grid(row=2,column=3)                                                                 #defining the grid position

#SEARCH ENTRY BUTTON
b1 = tk.Button(window, text="Search Entry",width = 15,command = buttons.search_command)         #search entry button
b1.grid(row=3,column=3)                                                                 #defining the grid position

#ADD ENTRY BUTTON
b1 = tk.Button(window, text="Add Entry",width = 15,command = buttons.enter_command)             #add entry button
b1.grid(row=4,column=3)                                                                 #defining the grid position

#UPDATE SELECTED BUTTON
b1 = tk.Button(window, text="Update Selected",width = 15, command = buttons.update_command)     #update selected button
b1.grid(row=5,column=3)                                                                 #defining the grid position

#DELETE SELECTED BUTTON
b1 = tk.Button(window, text="Delete Selected",width = 15,command = buttons.delete_command)      #delete selected button
b1.grid(row=6,column=3)                                                                 #defining the grid position 

#CLOSE BUTTON
b1 = tk.Button(window, text="Close",width = 15,command = window.destroy)                #close button
b1.grid(row=7,column=3)                                                                 #defining the grid position

window.mainloop()                           #invoking the main loop

"""
to create the executable file -
->pip install pyinstaller
->pyinstaller --onefile --windowed frontend.py
"""

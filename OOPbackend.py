import sqlite3

class Database:                                    
        
    def __init__(self):                                     
        self.conn = sqlite3.connect("books.db")         #creating table if doesn't exists
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS BOOK(ID INTEGER PRIMARY KEY, TITLE TEXT, AUTHOR TEXT, YEAR INTEGER, ISBN INTEGER)")
        self.conn.commit()

    def insert(self,TITLE,AUTHOR,YEAR,ISBN):             #insert function
        self.cursor.execute("INSERT INTO BOOK VALUES(NULL,?,?,?,?)",(TITLE,AUTHOR,YEAR,ISBN))
        self.conn.commit()

    def view(self,):                                     #view function, return rows of data
        self.cursor.execute("SELECT * FROM BOOK")
        rows = self.cursor.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""): #search function for values entered
        self.cursor.execute("SELECT * FROM BOOK WHERE TITLE = ? OR AUTHOR = ? OR YEAR = ? OR ISBN = ?",(title,author,year,isbn))
        rows = self.cursor.fetchall()
        return rows

    def delete(self,id):                                 #delete entries with id
        self.cursor.execute("DELETE FROM BOOK WHERE ID = ?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):          #update the entries in the database
        self.cursor.execute("UPDATE BOOK SET TITLE=?,AUTHOR=?,YEAR=?,ISBN=? WHERE ID=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):                                  #this function is executed when the script is exited
        self.conn.close()

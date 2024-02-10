import tkinter
from tkinter import ttk
from tkinter import messagebox
import connection_module
import print_documents

class report_module():
    
    def __init__(self,master='1'):
        self.master = master
       
    def print_ref_book(self):
        self.report_generator.reports = self.report_conn.people_book_reference()
        self.report_generator.print_report_book()
        
    def print_history_report(self):   
        self.report_generator.reports = self.report_conn.people_history_visits()
        self.report_generator.print_history_report()
        
        
    def main(self):
        self.window = tkinter.Toplevel(self.master)
        self.window.title("Reports")

        self.report_conn = connection_module.sql_driver('1','1','1','1')
        self.report_generator = print_documents.document_printer()

        frame = tkinter.Frame(self.window)
        frame.pack(padx=50,pady=30)
        
        self.button_enter_entity = tkinter.Button(frame,text="Visit histroy report", command=self.print_history_report)
        self.button_enter_entity.grid(row=1,column=0,padx=10,pady=10)
        
        self.button_report_entity = tkinter.Button(frame,text="Visitors reference", command = self.print_ref_book)
        self.button_report_entity.grid(row=2,column=0,padx=10,pady=10)
        
        
        self.window.mainloop()


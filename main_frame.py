import tkinter
from tkinter import ttk
import open_window_planning_3
import open_insert_persons
import report_module

class main_frame():
    def __init__(self,window_1,window_2,window_3):
        self.window_1=window_1
        self.window_2=window_2
        self.window_3=window_3

    def launch_windows(self,indicator):
    
        if indicator == '1':
            self.window_1.main()
        elif indicator == '2':  
            self.window_2.main()
        elif indicator == '3':  
            self.window_3.main()
        else:
            print("error")
  
        
    def main(self):
        window = tkinter.Tk()
        window.geometry('600x400')
        window.title('multiple windows')
        self.window_1.master = window
        self.window_2.master = window
        self.window_3.master = window
        
        button_planning_entity = tkinter.Button(window,text="Insert persons", command= lambda: self.launch_windows(indicator='1'))
        button_planning_entity.pack(expand=True)


        button_enter_entity = tkinter.Button(window,text="Enter entitiy", command= lambda: self.launch_windows(indicator='2'))
        button_enter_entity.pack(expand=True)
        
        button_report_entity = tkinter.Button(window,text="Reports", command= lambda: self.launch_windows(indicator='3'))
        button_report_entity.pack(expand=True)
        
        window.mainloop()

        

window_entring = open_insert_persons.open_insert_person_window()
window_planing = open_window_planning_3.open_insert_planing()
window_report = report_module.report_module()
main_frame_object = main_frame(window_entring,window_planing,window_report)
main_frame_object.main()






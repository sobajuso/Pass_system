import tkinter
from tkinter import ttk
import outside_class_action_2
import connection_module
import copy


class window_change_entity():

    def __init__(self,*args,**kwargs):
        self.persona_entity=kwargs.pop('persona_entity')
        self.organization_entity=kwargs.pop('organization_entity')
        self.laptop_name=kwargs.pop('laptop_name')
        self.entred_phrase=kwargs.pop('entred_phrase')
        self.status=kwargs.pop('status')
        self.master=kwargs.pop('master')
        super(window_change_entity,self).__init__(*args,**kwargs)


    def get_entred_value(self):
        self.entred_phrase = self.change_entity_entry.get()
        self.connection_objecta = connection_module.sql_driver(self.persona_entity,self.organization_entity,self.laptop_name,self.entred_phrase)
        if self.status == 'person':
            self.connection_objecta.update_entity_person()
        elif self.status == 'organization':
            self.connection_objecta.update_entity_organization()
        elif self.status == 'laptop':
            self.connection_objecta.update_entity_laptops()
        else:
            print('istake ------ \n')
        del self.connection_objecta


    
    def open_window_change_entity(self):

        
        window = tkinter.Toplevel(self.master)
        window.title("Enter another name")
 
        test_label = tkinter.Label(window, text="Enter changes")
        test_label.grid(row=0,column=0)
        self.change_entity_entry = tkinter.Entry(window)
        self.change_entity_entry.grid(row=1,column=0,padx=10,pady=10)
        change_entity_button = tkinter.Button(window, text = "Change entities",command=self.get_entred_value)
        change_entity_button.grid(row=2,column=0,sticky="news",padx=20,pady=5)
        window.mainloop()
     
    


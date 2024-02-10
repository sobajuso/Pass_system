import tkinter
from tkinter import ttk
import outside_class_action_2
from open_window_planning import open_window_planning
import connection_module
import connection_module_planing_mang
import copy
import open_window_change_entity



class window_change_enter_real_date(tkinter.Toplevel):
    def __init__(self,*args,**kwargs):
        self.persona_entity=kwargs.pop('persona_entity')
        self.organization_entity=kwargs.pop('organization_entity')
        self.laptop_name=kwargs.pop('laptop_name')
        self.entred_phrase=kwargs.pop('entred_phrase')
        self.status=kwargs.pop('status')
        #self.changing_phrase=kwargs.pop('changing_phrase')
        super(window_change_entity,self).__init__(*args,**kwargs)

    def get_entred_value(self):
        #print(self.change_entity_entry.get())
        self.entred_phrase = self.change_entity_entry.get()
        connection_objecta = connection_module.sql_driver(self.persona_entity,self.organization_entity,self.laptop_name,self.entred_phrase)
        if self.status == 'person':
            connection_objecta.update_entity_person()
        elif self.status == 'organization':
            print(str(self.organization_entity) + ' то что попало')
            connection_objecta.update_entity_organization()
        elif self.status == 'laptop':
            connection_objecta.update_entity_laptops()
        else:
            print('whtfck ------ \n')
            print(self.persona_entity)
            print(self.organization_entity)
            print(self.laptop_name)
            print('------ \n')
        #listbox_pers_id.Update(ajj_test.cast_data_pers())
        #return self.change_entity_entry.get()
        
    
    def open_window_change_entity(self):

        
        window = tkinter.Toplevel()
        window.title("Enter another name")
 
        test_label = tkinter.Label(window, text="Enter changes")
        test_label.grid(row=0,column=0)
        self.change_entity_entry = tkinter.Entry(window)
        self.change_entity_entry.grid(row=1,column=0,padx=10,pady=10)
        change_entity_button = tkinter.Button(window, text = "Change entities",command=self.get_entred_value)
        change_entity_button.grid(row=2,column=0,sticky="news",padx=20,pady=5)

        window.mainloop()
     
    


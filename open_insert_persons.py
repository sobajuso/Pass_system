import tkinter
from tkinter import ttk
import outside_class_action_2
import connection_module
import copy
import open_window_change_entity
from tkinter import messagebox
import re

class open_insert_person_window():
    def __init__(self,master='1'):
        self.master = master

    #======= Add new organization and laptop
    
    def add_entity_db_person(self):
        check_enter = self.pers_id_entry.get()
        check_marker = re.search('^[а-яА-Я]+ [а-яА-Я]+ [а-яА-Я]+',check_enter)
      
        if check_marker == None:
            tkinter.messagebox.showerror("Error","Вы указали неверный формат имени")
            raise Exception("your name data is wrong")
            
        self.connection_object.input_pers = str(self.pers_id_entry.get())
        self.connection_object.insert_data_pers()
        self.listbox_pers_id.list_1 = self.connection_object.cast_data_pers()



    def add_entity_db_organization(self):
        check_enter = self.org_label_entry.get()
        check_marker = re.search(' +$|(^$)|(^ )|(^[0-9])',check_enter)
        
        if check_marker != None:
            tkinter.messagebox.showerror("Error","Недопустимый формат имени организации")
            raise Exception("your name data is wrong")
        self.connection_object.input_org = str(self.org_label_entry.get())
        self.connection_object.insert_data_org()
        self.listbox_organization.list_1 = self.connection_object.cast_data_org()
   

    def add_entity_db_equipment(self):
        check_enter = self.equipment_name_entry.get()
        check_marker = re.search(' +$|(^$)|(^ )|(^[0-9])',check_enter)
        
        if check_marker != None:
            tkinter.messagebox.showerror("Error","Недопустимый формат имени устройства")
            raise Exception("your name data is wrong")
            
        self.connection_object.input_laptop = str(self.equipment_name_entry.get())
        self.connection_object.insert_data_laptop()
        self.listbox_equipment_name.list_1 = self.connection_object.cast_data_laptops()


    #==== show tied to person organization and laptop ===== (you need to change this on selection) =====

    def listbox_organizat_entry_bind(self,event):
    
        for i in self.listbox_pers_id.curselection():
           self.connection_object.input_pers = str(self.listbox_pers_id.get(i))
        
        self.listbox_organization.Scankey(event)
        self.listbox_organization_show.list_1 = self.connection_object.cast_data_org_show()
        self.listbox_organization_show.Scankey(event)


    def listbox_laptops_entry_bind(self,event):
        for i in self.listbox_pers_id.curselection():
           self.connection_object.input_pers = str(self.listbox_pers_id.get(i))

        self.listbox_equipment_name.Scankey(event)
        self.listbox_laptops_show.list_1 = self.connection_object.cast_data_laptops_show()
        self.listbox_laptops_show.Scankey(event)

    #======= fucntions for tie buttons ======

    def tie_org(self):
        
        if self.listbox_organization.curselection() == ():
            tkinter.messagebox.showerror("Error","Организация не выбрана")
            raise Exception("your name data is wrong")
            
        if self.listbox_pers_id.curselection() == ():
            tkinter.messagebox.showerror("Error","Сотрудник не выбран")
            raise Exception("your name data is wrong")
        
        
        for i in self.listbox_organization.curselection():
            temp_str = self.listbox_organization.get(i)
        
        for i in self.listbox_pers_id.curselection():
            temp_name = self.listbox_pers_id.get(i)
        
        #self.connection_object.input_pers = str(self.pers_id_entry.get())
        self.connection_object.input_pers = str(temp_name)
        self.connection_object.input_org = str(temp_str)
        self.connection_object.tie_org_to_person()
        self.listbox_organization_show.list_1 = self.connection_object.cast_data_org_show()



    def tie_laptop(self):
    
        if self.listbox_equipment_name.curselection() == ():
            tkinter.messagebox.showerror("Error","Устройство не выбрано")
            raise Exception("your name data is wrong")
            
        if self.listbox_pers_id.curselection() == ():
            tkinter.messagebox.showerror("Error","Сотрудник не выбран")
            raise Exception("your name data is wrong")
    
        for i in self.listbox_equipment_name.curselection():
            temp_str = self.listbox_equipment_name.get(i)
            
        for i in self.listbox_pers_id.curselection():
            temp_name = self.listbox_pers_id.get(i)
        
        self.connection_object.input_pers = str(temp_name)
        self.connection_object.input_laptop = str(temp_str)
        self.connection_object.tie_laptop_to_person()
        self.listbox_equipment_name.list_1 = self.connection_object.cast_data_laptops_show()
   
    
    
    #============== delte ties button ==========================
    def delete_tie_tie(self):
        if self.listbox_laptops_show.curselection() == () and self.listbox_organization_show.curselection() == ():
            tkinter.messagebox.showerror("Error","Не выбрано ни одной связи для удаления")
            raise Exception("your name data is wrong")
            
        if self.listbox_pers_id.curselection() == ():
            tkinter.messagebox.showerror("Error","Сотрудник не выбран")
            raise Exception("your name data is wrong")  
        
        
        for i in self.listbox_pers_id.curselection():
            temp_name = self.listbox_pers_id.get(i)
        
        
        if self.listbox_laptops_show.curselection() == ():
            for i in self.listbox_organization_show.curselection():
                temp_str = self.listbox_organization_show.get(i)
            self.connection_object.input_pers = str(temp_name)
            self.connection_object.input_org = str(temp_str)
            self.connection_object.delete_tie_org_to_person()
            self.listbox_organization_show.list_1 = self.connection_object.cast_data_org_show()
        elif self.listbox_organization_show.curselection() == ():
            for i in self.listbox_laptops_show.curselection():
                temp_str = self.listbox_laptops_show.get(i)
            self.connection_object.input_pers = str(temp_name)
            self.connection_object.input_laptop = str(temp_str)
            self.connection_object.delete_tie_laptop_to_person()
            self.listbox_laptops_show.list_1 = self.connection_object.cast_data_laptops_show()
        else:
            print(' ----- \n nothing selected')



    #============= update entity ===============================
    
    def update_entities(self):
        if self.listbox_organization.curselection() == () and self.listbox_equipment_name.curselection() == ():
            for i in self.listbox_pers_id.curselection():
                self.change_window.persona_entity = str(self.listbox_pers_id.get(i))
                self.change_window.status = 'person'
        if self.listbox_pers_id.curselection() == () and self.listbox_equipment_name.curselection() == ():
            for i in self.listbox_organization.curselection():
                self.change_window.organization_entity = str(self.listbox_organization.get(i))
                self.change_window.status = 'organization'
        if self.listbox_pers_id.curselection() == () and self.listbox_organization.curselection() == ():
            for i in self.listbox_equipment_name.curselection():
                self.change_window.laptop_name = str(self.listbox_equipment_name.get(i))
                self.change_window.status = 'laptop'
        else:
            print('unknow action')
        self.change_window.open_window_change_entity()
        

    def Update_info(self,event):
        self.listbox_pers_id.list_1=self.connection_object.cast_data_pers()
        self.listbox_equipment_name.list_1 = self.connection_object.cast_data_laptops()
        self.listbox_organization.list_1 = self.connection_object.cast_data_org()


    def synchronized_update_click(self,event):
        self.org_label_entry.delete(0,tkinter.END)
        self.equipment_name_entry.delete(0,tkinter.END)
        
        for i in self.listbox_pers_id.curselection():
            self.connection_object.input_pers = str(self.listbox_pers_id.get(i))
        self.listbox_organization_show.list_1 = self.connection_object.cast_data_org_show()
        self.listbox_laptops_show.list_1 = self.connection_object.cast_data_laptops_show()
        self.listbox_organization_show.without_event_update()
        self.listbox_laptops_show.without_event_update()

    
    
    def main(self):
        
        self.window = tkinter.Toplevel(self.master)
        self.window.title("Enter Persons")
        #self.window.withdraw()
        self.connection_object = connection_module.sql_driver('1','1','1','1')
    
        self.change_window = open_window_change_entity.window_change_entity(persona_entity='1',organization_entity='1',laptop_name='1',entred_phrase='1',status='1',master=self.window)

        frame = tkinter.Frame(self.window)
        frame.pack(padx=30,pady=10)
        
    #================================ Laptop ===============================
        self.equipment_name_label = tkinter.Label(frame, text="laptop")
        self.equipment_name_label.grid(row=0,column=2)
        self.equipment_name_entry = tkinter.Entry(frame)
        self.equipment_name_entry.grid(row=1,column=2,padx=10,pady=10)
        self.listbox_equipment_name=outside_class_action_2.listbox_set(frame,list_1=self.connection_object.cast_data_laptops(),entry=self.equipment_name_entry,width=25,height=10)
        self.listbox_equipment_name.grid(row=2,column=2,padx=20,pady=5)
        self.equipment_name_entry.bind('<KeyRelease>',self.Update_info)
        self.equipment_name_entry.bind('<KeyRelease>',self.listbox_laptops_entry_bind,add='+')
        self.listbox_equipment_name.Update(self.connection_object.cast_data_laptops())
        self.listbox_equipment_name.bind('<Double-Button-1>',self.listbox_equipment_name.focused_stuff)
    #================================ Person ===============================
        self.pers_id_label = tkinter.Label(frame, text="Person")
        self.pers_id_label.grid(row=0,column=0)
        self.pers_id_entry = tkinter.Entry(frame)
        self.pers_id_entry.grid(row=1,column=0,padx=10,pady=10)
        self.listbox_pers_id=outside_class_action_2.listbox_set(frame,list_1=self.connection_object.cast_data_pers(),entry=self.pers_id_entry,exportselection=False,width=25,height=10)
        self.listbox_pers_id.grid(row=2,column=0,padx=20,pady=5)
        self.pers_id_entry.bind('<KeyRelease>',self.Update_info)
        self.pers_id_entry.bind('<KeyRelease>',self.listbox_pers_id.Scankey,add='+')
        self.listbox_pers_id.Update(self.connection_object.cast_data_pers())
        self.listbox_pers_id.bind('<Double-Button-1>',self.listbox_pers_id.focused_stuff)
        self.listbox_pers_id.bind('<Double-Button-1>',self.synchronized_update_click,add='+')
    #=============================== Organization ==========================
        self.org_label = tkinter.Label(frame, text="Organization")
        self.org_label.grid(row=0,column=1)
        self.org_label_entry = tkinter.Entry(frame)
        self.org_label_entry.grid(row=1,column=1,padx=10,pady=10)
        self.listbox_organization=outside_class_action_2.listbox_set(frame,list_1=self.connection_object.cast_data_org(),entry=self.org_label_entry,width=25,height=10)
        self.listbox_organization.grid(row=2,column=1,padx=20,pady=5)
        self.org_label_entry.bind('<KeyRelease>',self.Update_info)
        self.org_label_entry.bind('<KeyRelease>',self.listbox_organizat_entry_bind,add='+')
        self.listbox_organization.Update(self.connection_object.cast_data_org())
        self.listbox_organization.bind('<Double-Button-1>',self.listbox_organization.focused_stuff)
    #=======================================================================
    #==================== Button Bar =======================================
    #=======================================================================
        self.commit_person_button = tkinter.Button(frame, text = "Add item",command=self.add_entity_db_person)
        self.commit_person_button.grid(row=4,column=0,sticky="news",padx=20,pady=5)

        self.commit_organization_button = tkinter.Button(frame, text = "Add item",command=self.add_entity_db_organization)
        self.commit_organization_button.grid(row=4,column=1,sticky="news",padx=20,pady=5)
    
        self.commit_equipment_button = tkinter.Button(frame, text = "Add item",command=self.add_entity_db_equipment)
        self.commit_equipment_button.grid(row=4,column=2,sticky="news",padx=20,pady=5)
    
        self.change_entity_button = tkinter.Button(frame, text = "Change entities",command=self.update_entities)
        self.change_entity_button.grid(row=8,column=0,sticky="news",padx=20,pady=5,columnspan=4)

    #========== test buttona ===
        '''
        self.test_label = tkinter.Label(frame, text="laptop")
        self.test_label.grid(row=1,column=3)
        self.change_entity_entry = tkinter.Entry(frame)
        self.change_entity_entry.grid(row=2,column=3,padx=10,pady=10)
        '''

    #==== instead of tree bar ======================

        self.listbox_organization_show=outside_class_action_2.listbox_set(frame,list_1=self.connection_object.cast_data_org_show(),entry=self.org_label_entry,width=25,height=10)
        self.listbox_organization_show.grid(row=5,column=1,padx=20,pady=5)

        self.listbox_organization_show.Update(self.connection_object.cast_data_org_show())


        self.listbox_organization_show.bind('<Double-Button-1>',self.listbox_organization_show.focused_stuff)


    
    
    
        self.listbox_laptops_show=outside_class_action_2.listbox_set(frame,list_1=self.connection_object.cast_data_laptops_show(),entry=self.equipment_name_entry,width=25,height=10)
        self.listbox_laptops_show.grid(row=5,column=2,padx=20,pady=5)
        self.listbox_laptops_show.Update(self.connection_object.cast_data_laptops_show())

        self.listbox_laptops_show.bind('<Double-Button-1>',self.listbox_laptops_show.focused_stuff)


    

        self.tie_org_button = tkinter.Button(frame, text = "Tie organization",command=self.tie_org)
        self.tie_org_button.grid(row=6,column=1,columnspan=1,sticky="news",padx=20,pady=5)
        self.tie_laptop_button = tkinter.Button(frame, text = "Tie laptop",command=self.tie_laptop)
        self.tie_laptop_button.grid(row=6,column=2,columnspan=1,sticky="news",padx=20,pady=5)
    


    #===============================================

        self.delete_entity_button = tkinter.Button(frame, text = "Delete entity", command=self.delete_tie_tie)
        self.delete_entity_button.grid(row=7,column=0,columnspan=4,sticky="news",padx=20,pady=5)
        frame.mainloop()
    

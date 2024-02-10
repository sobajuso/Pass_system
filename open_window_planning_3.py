import tkinter
from tkinter import ttk
from tkinter import messagebox
import outside_class_action_2
import connection_module
import copy
import open_window_change_entity
import connection_module_planing_mang
import re
import between_dates
from datetime import timedelta, date
import print_documents

class open_insert_planing():
    
    def __init__(self,master='1'):
        self.master = master
        
    def check_date(self):
        checking_start_date = self.start_date_entry.get()
        checking_finish_date = self.finish_date_entry.get()

        check_start = re.search('[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9][0-9][0-9]',checking_start_date)
        check_finish = re.search('[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9][0-9][0-9]',checking_finish_date)
        marker = True
        if (check_start == None) or (check_finish == None):
            marker = False
        else:
            date_I_transform = list(checking_start_date.split('.'))
            date_II_transform = list(checking_finish_date.split('.'))
            date_I = [int(date_I_transform[0]),int(date_I_transform[1]),int(date_I_transform[2])]
            date_II = [int(date_II_transform[0]),int(date_II_transform[1]),int(date_II_transform[2])]
            condition_list = []
            condition_list.append((date_I[0] < 32) and (date_II[0] < 32))
            condition_list.append((date_I[1] < 13) and (date_II[1] < 13))
            condition_list.append(date_I[0] <= date_II[0])
            condition_list.append(date_I[1] <= date_II[1])                  
            condition_list.append(date_I[2] <= date_II[2])
            expression_check = True       
            for item in condition_list:
                if item == False:
                    expression_check = False
                    break
                else:
                    expression_check = item
            if expression_check == True:
                marker = True
            else:
                marker = False     
        return marker
    
    def refresh_focus_tree(self):
        selected = self.tree.focus()
        opa = self.tree.item(selected,'values')
        self.entity_object.persname=self.tree.item(selected)["values"][0]
        self.entity_object.orgname=self.tree.item(selected)["values"][1]
        self.entity_object.startdateplaning=self.tree.item(selected)["values"][2]
        self.entity_object.finishdateplaning=self.tree.item(selected)["values"][3]
        self.entity_object.laptopID=self.tree.item(selected)["values"][4]
        self.entity_object.startdateactual=self.tree.item(selected)["values"][5]
        self.entity_object.finishdateactual=self.tree.item(selected)["values"][6]
        
    def delete_entity_from_visiting_table(self):
        self.refresh_focus_tree()
        self.entity_object.Delete_Entity_From_VisitTable()
        self.show_entities_visitng()

    
    def clear_item(self):
        self.pers_id_entry.delete(0,tkinter.END)
        self.pers_id_entry.insert(0,"")
        self.org_label_entry.delete(0,tkinter.END)
        self.start_date_entry.delete(0,tkinter.END)
        self.finish_date_entry.delete(0,tkinter.END)
        self.equipment_name_entry.delete(0,tkinter.END)
    
    def add_item(self):

        check = self.check_date()

        if check != True:
            tkinter.messagebox.showerror("Title","Your data worng")
            raise Exception("your data wrong")
        	
        laptop_get_2 = []
        	
        for i in self.listbox_pers_id.curselection():
            pers_get = str(self.listbox_pers_id.get(i))
        for i in self.listbox_organization_show.curselection():
            org_get = str(self.listbox_organization_show.get(i))
        #for i in self.listbox_organization_show.curselection():
        for i in self.listbox_laptops_show.curselection():
            laptop_get = str(self.listbox_laptops_show.get(i))
            laptop_get_2.append(self.listbox_laptops_show.get(i))

        pers_id_middle = list(pers_get.split(' '))
        pers_id = str(pers_id_middle[1])+' '+str(pers_id_middle[2])+' '+str(pers_id_middle[3])
        self.entity_object.persname=pers_id
        

        org_middle = list(org_get.split(' ',1))
        org = str(org_middle[1])
        self.entity_object.orgname=org


        #equipment_name_middle = list(laptop_get.split(' ',1))
        string_media = []
        for i in laptop_get_2:
            equipment_mid = list(i.split(' ',1))
            equipment_mid_2 = str(equipment_mid[1]+';')
            string_media.append(equipment_mid_2)
        equipment_name_middle = str(''.join(string_media))
        print(string_media)
        #equipment_name = str(equipment_name_middle[1])
        equipment_name = str(equipment_name_middle)
        self.entity_object.laptopID=equipment_name
        
        start_date = self.start_date_entry.get()
        self.entity_object.startdateplaning=str(self.start_date_entry.get())
        finish_date = self.finish_date_entry.get()
        self.entity_object.finishdateplaning=str(self.finish_date_entry.get())
        self.entity_object.add_entity_planing_visit()
        self.show_entities_visitng()


    def show_entities_visitng(self):
    
        self.tree.delete(*self.tree.get_children())
        temp_obj=self.entity_object.ShowDataFromPlaningVisits()
        
        for i in range(len(temp_obj)):
            inner_temp_obj = temp_obj[i]
            pers_id = inner_temp_obj[0]
            org = inner_temp_obj[1]
            start_date = inner_temp_obj[2]
            finish_date = inner_temp_obj[3]
            equipment_name = inner_temp_obj[4]
            actual_come = inner_temp_obj[5]
            actual_go = inner_temp_obj[6]
            planing_entity_item = [pers_id, org, start_date, finish_date, equipment_name,actual_come,actual_go]
            self.tree.insert('',0,values=planing_entity_item)
        self.clear_item()
        
    #======= Add new organization and laptop
    
    def add_entity_db_person(self):
        self.ajj_test.input_pers = str(self.pers_id_entry.get())
        self.ajj_test.insert_data_pers()
        self.listbox_pers_id.list_1 = self.ajj_test.cast_data_pers()
        print(self.pers_id_entry.get())


    def add_entity_db_organization(self):
        self.ajj_test.input_org = str(self.org_label_entry.get())
        self.ajj_test.insert_data_org()
        self.listbox_organization.list_1 = self.ajj_test.cast_data_org()


    def add_entity_db_equipment(self):
        self.ajj_test.input_laptop = str(self.equipment_name_entry.get())
        self.ajj_test.insert_data_laptop()
        self.listbox_equipment_name.list_1 = self.ajj_test.cast_data_laptops()


    #==== show tied to person organization and laptop ===== (you need to change this on selection) =====

    def listbox_organizat_entry_bind(self,arg_entry):
        for i in self.listbox_pers_id.curselection():
           self.ajj_test.input_pers = str(self.listbox_pers_id.get(i))
        self.listbox_organization_show.list_1 = self.ajj_test.cast_data_org_show()
        self.listbox_organization_show.Scankey(arg_entry)
       

    def listbox_laptops_entry_bind(self,arg_entry):
        for i in self.listbox_pers_id.curselection():
           self.ajj_test.input_pers = str(self.listbox_pers_id.get(i))
        self.listbox_laptops_show.list_1 = self.ajj_test.cast_data_laptops_show()
        self.listbox_laptops_show.Scankey(arg_entry)
    

    #================= add real dates =============
    def add_real_dates(self):
        self.refresh_focus_tree()
        check = self.check_date()
        if check != True:
            tkinter.messagebox.showerror("Error message","Your data worng")
            raise Exception("your data wrong")
        self.entity_object.startdateactual = str(self.start_date_entry.get())
        self.entity_object.finishdateactual = str(self.finish_date_entry.get())
        self.entity_object.Add_real_vist_date()
        self.show_entities_visitng()
    #============ adding visit to history ===========
    def add_to_history(self):
        self.refresh_focus_tree()
        check = (self.entity_object.persname!='None' and self.entity_object.startdateplaning!='None' and self.entity_object.finishdateplaning!='None' and self.entity_object.startdateactual!='None' and self.entity_object.finishdateactual!='None')
        if check == False:
            tkinter.messagebox.showerror("Error message","Your data worng")
            raise Exception("your data wrong")
        self.entity_object.Add_entity_to_history()
        print("added to history")

    def synchronized_update(self,event):
        self.org_label_entry.delete(0,tkinter.END)
        self.equipment_name_entry.delete(0,tkinter.END)
        self.listbox_organization_show.list_1 = self.ajj_test.cast_data_org_show()
        self.listbox_laptops_show.list_1 = self.ajj_test.cast_data_laptops_show()
        self.listbox_organization_show.without_event_update()
        self.listbox_laptops_show.without_event_update()

    def synchronized_update_click(self,event):
        self.org_label_entry.delete(0,tkinter.END)
        self.equipment_name_entry.delete(0,tkinter.END)
        for i in self.listbox_pers_id.curselection():
            self.ajj_test.input_pers = str(self.listbox_pers_id.get(i))
        self.listbox_organization_show.list_1 = self.ajj_test.cast_data_org_show()
        self.listbox_laptops_show.list_1 = self.ajj_test.cast_data_laptops_show()
        self.listbox_organization_show.without_event_update()
        self.listbox_laptops_show.without_event_update()
        



    def print_documents(self):
        selected = self.tree.focus()
        opa = self.tree.item(selected,'values')
        person_name = self.tree.item(selected)["values"][0]
        date_I = self.tree.item(selected)["values"][2].split('.')
        date_II = self.tree.item(selected)["values"][3].split('.')
        laptop_dis = self.tree.item(selected)["values"][4].split('.')
        dates_list = between_dates.Dateline(date(int(date_I[2]),int(date_I[1]),int(date_I[0])),date(int(date_II[2]),int(date_II[1]),int(date_II[0])))
        dates_list.show_dates()
        dates_list.printing()
        document_a = print_documents.document_printer(person_name, dates_list.show_dates(),laptop_dis)
        document_a.print_doc_laptops()
        document_a.print_person_pass_doc()
        del dates_list
        del document_a

    def multiple_visit(self):
        selected_persons = self.tree.selection()
        data_for_pass = []
        extrem_dates_start = []
        extrem_dates_finish = []
        data_massive = {}
        data_massive_fin = {}
        for i in selected_persons:
        	name = self.tree.item(i)["values"][0]
        	org = self.tree.item(i)["values"][1]
        	date_start = self.tree.item(i)["values"][2]
        	date_finish = self.tree.item(i)["values"][3]
        	data_for_pass.append([name,org,date_start,date_finish])

        index_dict = 0
        
        for j in data_for_pass:
            data_middle = j
            data_I = str(data_middle[2]).split('.')
            data_II = str(data_middle[3]).split('.')
            
            data_massive[index_dict] = {"day": int(data_I[0]),
                                        "month": int(data_I[1]),
                                        "year": int(data_I[2])
                                       }
                                       
            data_massive_fin[index_dict] = {"day": int(data_II[0]),
                                        "month": int(data_II[1]),
                                        "year": int(data_II[2])
                                       }
            
            index_dict += 1
            
        
        minimum_date = self.find_min_date(data_massive)
        maximum_date = self.find_max_date(data_massive_fin)

        
        document_a = print_documents.document_printer(mult_vis=data_for_pass,dates_doc=[minimum_date,maximum_date])
        document_a.print_person_mult_visit()
        del document_a
       
    def find_min_date(self,data_massive):
        year_sort = []
        for item in data_massive:
            year_sort.append(int(data_massive[item]["year"]))
        year_sort.sort()
        minimum_year = list(year_sort)[0]
        
        list_items_with_min_year = []
        for item in data_massive:
            if data_massive[item]["year"] == minimum_year:
                list_items_with_min_year.append(int(item))
        
        month_sort_string = []
        for index_a in list_items_with_min_year:
            month_sort_string.append(int(data_massive[index_a]["month"]))
        month_sort_string.sort()
        minimum_month = list(month_sort_string)[0]
        
        list_items_with_min_month = []
        for item in list_items_with_min_year:
            if data_massive[item]["month"] == minimum_month:
                list_items_with_min_month.append(int(item))
        
        day_sort_string = []
        for index_a in list_items_with_min_month:
            day_sort_string.append(int(data_massive[index_a]["day"]))
        day_sort_string.sort()
        minimum_day = list(day_sort_string)[0]

        
        minimum_date = [int(minimum_day),int(minimum_month),int(minimum_year)]
        return(minimum_date)
        
    def find_max_date(self,data_massive):
        year_sort = []
        for item in data_massive:
            year_sort.append(int(data_massive[item]["year"]))
        year_sort.sort()
        maximum_year = list(year_sort)[-1]
        
        list_items_with_max_year = []
        for item in data_massive:
            if data_massive[item]["year"] == maximum_year:
                list_items_with_max_year.append(int(item))
        
        month_sort_string = []
        for index_a in list_items_with_max_year:
            month_sort_string.append(int(data_massive[index_a]["month"]))
        month_sort_string.sort()
        maximum_month = list(month_sort_string)[-1]

        
        list_items_with_max_month = []
        for item in list_items_with_max_year:
            if data_massive[item]["month"] == maximum_month:
                list_items_with_max_month.append(int(item))
       
        day_sort_string = []
        for index_a in list_items_with_max_month:
            day_sort_string.append(int(data_massive[index_a]["day"]))
        day_sort_string.sort()
        maximum_day = list(day_sort_string)[-1]
        
        maximum_date = [int(maximum_day),int(maximum_month),int(maximum_year)]
        return(maximum_date)
        
    #==================================================
    #==============MAIN_METHOD=========================
    #==================================================
    
    def main(self):
        self.window = tkinter.Toplevel(self.master)
        self.window.title("Enter planning dates")

        self.ajj_test = connection_module.sql_driver('1','1','1','1')
        self.entity_object = connection_module_planing_mang.sql_driver_visit_handler()

        frame = tkinter.Frame(self.window)
        frame.pack(padx=30,pady=10)

    
    
    #================================ Laptop ===============================
        self.equipment_name_label = tkinter.Label(frame, text="laptop")
        self.equipment_name_label.grid(row=0,column=2)
        self.equipment_name_entry = tkinter.Entry(frame)
        self.equipment_name_entry.grid(row=1,column=2,padx=10,pady=10)
 
    #================================ Person ===============================
        self.pers_id_label = tkinter.Label(frame, text="Person")
        self.pers_id_label.grid(row=0,column=0)
        self.pers_id_entry = tkinter.Entry(frame)
        self.pers_id_entry.grid(row=1,column=0,padx=10,pady=10)
        self.listbox_pers_id=outside_class_action_2.listbox_set(frame,list_1=self.ajj_test.cast_data_pers(),entry=self.pers_id_entry,exportselection=False,width=25,height=10)
        self.listbox_pers_id.grid(row=2,column=0,padx=20,pady=5)
        self.pers_id_entry.bind('<KeyRelease>',self.listbox_pers_id.Scankey)
        self.listbox_pers_id.Update(self.ajj_test.cast_data_pers())
        self.listbox_pers_id.bind('<Double-Button-1>',self.listbox_pers_id.focused_stuff)
        self.listbox_pers_id.bind('<Double-Button-1>',self.synchronized_update_click,add='+')
    #=============================== Organization ==========================
        self.org_label = tkinter.Label(frame, text="Organization")
        self.org_label.grid(row=0,column=1)
        self.org_label_entry = tkinter.Entry(frame)
        self.org_label_entry.grid(row=1,column=1,padx=10,pady=10)
  

    #==== instead of tree bar ======================
 
        self.listbox_organization_show=outside_class_action_2.listbox_set(frame,list_1=self.ajj_test.cast_data_org_show(),entry=self.org_label_entry,exportselection=False,width=25,height=10)
        self.listbox_organization_show.grid(row=2,column=1,padx=20,pady=5)
        self.listbox_organization_show.Update(self.ajj_test.cast_data_org_show())
        self.org_label_entry.bind('<KeyRelease>',self.listbox_organizat_entry_bind)
        self.listbox_organization_show.bind('<Double-Button-1>',self.listbox_organization_show.focused_stuff)


        self.listbox_laptops_show=outside_class_action_2.listbox_set(frame,list_1=self.ajj_test.cast_data_laptops_show(),entry=self.equipment_name_entry,exportselection=False,selectmode = "multiple",width=25,height=10)
        self.listbox_laptops_show.grid(row=2,column=2,padx=20,pady=5)
        self.listbox_laptops_show.Update(self.ajj_test.cast_data_laptops_show())
        self.listbox_laptops_show.bind('<KeyRelease>',self.listbox_laptops_entry_bind)
        self.equipment_name_entry.bind('<KeyRelease>',self.listbox_laptops_entry_bind)
        self.listbox_laptops_show.bind('<Double-Button-1>',self.listbox_laptops_show.focused_stuff)

    #====== enter data bar =======
    
        self.start_date_label = tkinter.Label(frame, text="start date")
        self.start_date_label.grid(row=3,column=0)
        self.finish_date_label = tkinter.Label(frame, text="finish date")
        self.finish_date_label.grid(row=3,column=1)


        self.start_date_entry = tkinter.Entry(frame)
        self.finish_date_entry = tkinter.Entry(frame)

        self.start_date_entry.grid(row=4,column=0)
        self.finish_date_entry.grid(row=4,column=1)
    
    
    

    #========== tree bar =========
        self.add_item_button = tkinter.Button(frame, text = "Add item", command=self.add_item)
        self.add_item_button.grid(row=3,column=2,pady=5)
        self.add_actual_dates_button = tkinter.Button(frame, text = "Add dates", command=self.add_real_dates)
        self.add_actual_dates_button.grid(row=4,column=2,pady=5)

        self.columns = ('pers_id', 'org', 'start_date', 'finish_date', 'equipment','actual_come','actual_go')

        self.tree = ttk.Treeview(frame,columns=self.columns,show="headings")
        self.tree.heading('pers_id',text='Person')
        self.tree.heading('org',text='Organization')
        self.tree.heading('start_date',text='Start date')
        self.tree.heading('finish_date',text='Finish date')
        self.tree.heading('equipment',text='Laptop')
        self.tree.heading('actual_come',text='Actual come')
        self.tree.heading('actual_go',text='Actual go')
        self.tree.grid(row=5,column=0,columnspan=3,padx=20,pady=10)

     
    
    #===============================================


        self.delete_entity_button = tkinter.Button(frame, text = "Delete entity",command=self.delete_entity_from_visiting_table)
   
        self.delete_entity_button.grid(row=7,column=0,columnspan=4,sticky="news",padx=20,pady=5)

        self.add_to_history_button = tkinter.Button(frame, text = "Add to history",command=self.add_to_history)
        self.add_to_history_button.grid(row=8,column=0,columnspan=4,sticky="news",padx=20,pady=5)

        self.print_documents_button = tkinter.Button(frame, text = "Print documents",command=self.print_documents)
        self.print_documents_button.grid(row=9,column=0,columnspan=4,sticky="news",padx=20,pady=5)
        
        self.multiple_visit = tkinter.Button(frame, text = "Multiple visit",command=self.multiple_visit)
        self.multiple_visit.grid(row=10,column=0,columnspan=4,sticky="news",padx=20,pady=5)
        
        self.show_entities_visitng()
        self.window.mainloop()


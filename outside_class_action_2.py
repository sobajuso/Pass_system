from tkinter import ttk
import tkinter
import copy

class listbox_set(tkinter.Listbox):

    
    def __init__(self,*args,**kwargs):
        self.list_1=kwargs.pop('list_1')
        self.entry=kwargs.pop('entry')
        super(listbox_set,self).__init__(*args,**kwargs)

    def Scankey(self,event):

        val = event.widget.get()
     

        if val == '':
            data = self.list_1
        else:
            data = []
            for item in self.list_1:
                if val.lower() in item.lower():
                    data.append(item)
        self.Update(data)

    def Update(self,data):
        self.delete(0,'end')

        for item in data:
            self.insert('end',item)

    def focused_stuff(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection)
        self.entry.delete(0,tkinter.END)
        self.entry.insert(0,str(value))
     
        
    def delete_delete(self,event):
        widget = event.widget()
        selection = widget.curselection()
        value = widget.get(selection)
        self.list_1.remove(value)

    def without_event_update(self):
        self.delete(0,'end')
        for item in self.list_1:
            self.insert('end',item)
      

    def without_event_update_another(self):
        value_lue = self.entry.get()
        
        if value_lue == '':
            print_massive = self.list_1
        else:
            print_massive = []
            for objectus in self.list_1:
                if value_lue.lower() in objectus.lower():
                    print_massive.append(objectus)
        self.Update(print_massive)
    
    

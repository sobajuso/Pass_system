import mariadb
import copy

class sql_driver():

#===================rewrite========================
    conn = mariadb.connect(
        user="admin@localhost",
        password="myawesomepass",
        host="localhost",
        port=3306,
        database="peop_base_two"
        )
#====================this===========================
    def __init__(self,input_pers='1',input_org='1',input_laptop='1',new_data_enter='1'):
        self.input_pers = input_pers
        self.input_org = input_org
        self.input_laptop = input_laptop
        self.new_data_enter = new_data_enter


    def __del__(self):
        class_name = self.__class__.__name__
        print(f" {class_name} object have been destored")

    #========= Cast data ================
    def cast_data_pers(self):
        cursor = self.conn.cursor()
        #cursor.execute('SELECT * FROM [peop_base_two].[dbo].[peoples]')
        #===new
        cursor.execute('SELECT * FROM peop_base_two.peoples')
        rows = cursor.fetchall()
        
        apt = []
        for row in rows:
            ahhh = str(row[0]) + ' ' + str(row[1])+' '+str(row[2])+' '+str(row[3])
            apt.append(ahhh)
        return apt

    def cast_data_org(self):
        cursor = self.conn.cursor()
        #cursor.execute('SELECT * FROM [peop_base_two].[dbo].[organization]')
        #===new
        cursor.execute('SELECT * FROM peop_base_two.organization')
        rows = cursor.fetchall()
      
        apt = []
        for row in rows:
            ahhh = str(row[0]) + ' ' + ' ' + str(row[1])
            apt.append(ahhh)
        return apt

    def cast_data_laptops(self):
        cursor = self.conn.cursor()
        #cursor.execute('SELECT * FROM [peop_base_two].[dbo].[laptops]')
        #===new
        cursor.execute('SELECT * FROM peop_base_two.laptops')
        rows = cursor.fetchall()
      
        apt = []
        for row in rows:
            ahhh = str(row[0]) + ' ' + ' ' + str(row[1])
            apt.append(ahhh)
        return apt
    #==============================================


    #============= Insert Data ====================
    def insert_data_pers(self):
        inserting = list(self.input_pers.split(" "))
        name = str(inserting[0])
        secondname = str(inserting[1])
        surname = str(inserting[2])
        cursor = self.conn.cursor()
        #cursor.execute("INSERT INTO [peop_base_two].[dbo].[peoples](name,second_name,surname) VALUES (?,?,?)",(name,secondname,surname))
        #cursor.commit()
        cursor.execute("INSERT INTO peop_base_two.peoples(name,second_name,surname) VALUES (?,?,?)",(name,secondname,surname))
        self.conn.commit()
 


    def insert_data_org(self):
        org = self.input_org
        cursor = self.conn.cursor()
        #cursor.execute("INSERT INTO [peop_base_two].[dbo].[organization](organization_name) VALUES (?)",(org))
        #cursor.commit()
        cursor.execute("INSERT INTO peop_base_two.organization(organization_name) VALUES (?)",(org,))
        self.conn.commit()

    def insert_data_laptop(self):
        laptop = self.input_laptop
        cursor = self.conn.cursor()
        #cursor.execute("INSERT INTO [peop_base_two].[dbo].[laptops](laptop_info) VALUES (?)",(laptop))
        #cursor.commit()
        cursor.execute("INSERT INTO peop_base_two.laptops(laptop_info) VALUES (?)",(laptop,))
        self.conn.commit()
    #===============================================

    #========== Cast data bindings =================
    def cast_data_org_show(self):
        
        inserting = list(self.input_pers.split(" "))
        ID = int(inserting[0])
        
        
        cursor = self.conn.cursor()
        '''
        cursor.execute("""
                        SELECT [peop_base_two].[dbo].[organization].[org_ID],
                        [peop_base_two].[dbo].[organization].[organization_name] 
                        FROM [peop_base_two].[dbo].[org_bind] 
                        INNER JOIN [peop_base_two].[dbo].[organization] 
                        ON [peop_base_two].[dbo].[organization].[org_ID] = [peop_base_two].[dbo].[org_bind].[org_ID] 
                        WHERE [peop_base_two].[dbo].[org_bind].[pers_ID] = ?
                """,(ID))
        '''
        cursor.execute("""
                        SELECT peop_base_two.organization.org_ID,
                        peop_base_two.organization.organization_name
                        FROM peop_base_two.org_bind
                        INNER JOIN peop_base_two.organization
                        ON peop_base_two.organization.org_ID = peop_base_two.org_bind.org_ID
                        WHERE peop_base_two.org_bind.pers_ID = ?
                """,(ID,))
        
        rows = cursor.fetchall()
      
        apt = []
        for row in rows:
            ahhh = str(row[0])+' '+str(row[1])
            apt.append(ahhh)
        return apt


    def cast_data_laptops_show(self):
        
        inserting = list(self.input_pers.split(" "))
        ID = int(inserting[0])
        
        
        cursor = self.conn.cursor()
        '''
        cursor.execute("""
                        SELECT [peop_base_two].[dbo].[laptops].[laptop_ID],
                        [peop_base_two].[dbo].[laptops].[laptop_info]
                        FROM [peop_base_two].[dbo].[laptop_bind] 
                        INNER JOIN [peop_base_two].[dbo].[laptops] 
                        ON [peop_base_two].[dbo].[laptops].[laptop_ID] = [peop_base_two].[dbo].[laptop_bind].[laptop_ID] 
                        WHERE [peop_base_two].[dbo].[laptop_bind].[pers_ID] =  ?
                """,(ID))
        '''

        cursor.execute("""
                        SELECT peop_base_two.laptops.laptop_ID,
                        peop_base_two.laptops.laptop_info
                        FROM peop_base_two.laptop_bind
                        INNER JOIN peop_base_two.laptops
                        ON peop_base_two.laptops.laptop_ID = peop_base_two.laptop_bind.laptop_ID
                        WHERE peop_base_two.laptop_bind.pers_ID =  ?
                """,(ID,))
        
        rows = cursor.fetchall()
      
        apt = []
        for row in rows:
            ahhh = str(row[0])+' '+str(row[1])
            apt.append(ahhh)
        return apt

    #===============================================        
    #====== Tie laptops and organization ======

    def tie_org_to_person(self):
        inserting_pers = list(self.input_pers.split(" "))
        inserting_org = list(self.input_org.split(" "))
        pers = int(inserting_pers[0])
        org = int(inserting_org[0])
        cursor = self.conn.cursor()
        #cursor.execute("INSERT INTO [peop_base_two].[dbo].[org_bind](pers_ID,org_ID) VALUES (?,?)",(pers,org))
        #cursor.commit()
        cursor.execute("INSERT INTO peop_base_two.org_bind(pers_ID,org_ID) VALUES (?,?)",(pers,org))
        self.conn.commit()

    def tie_laptop_to_person(self):
        inserting_pers = list(self.input_pers.split(" "))
        inserting_laptop = list(self.input_laptop.split(" "))
        pers = int(inserting_pers[0])
        laptop = int(inserting_laptop[0])
        cursor = self.conn.cursor()
        #cursor.execute("INSERT INTO [peop_base_two].[dbo].[laptop_bind](pers_ID,laptop_ID) VALUES (?,?)",(pers,laptop))
        #cursor.commit()
        cursor.execute("INSERT INTO peop_base_two.laptop_bind(pers_ID,laptop_ID) VALUES (?,?)",(pers,laptop))
        self.conn.commit()
        
    #============= Delte laptops and organization ties =========
    def delete_tie_org_to_person(self):
        inserting_pers = list(self.input_pers.split(" "))
        inserting_org = list(self.input_org.split(" "))
        pers = int(inserting_pers[0])
        org = int(inserting_org[0])
        cursor = self.conn.cursor()
        #cursor.execute("DELETE FROM [peop_base_two].[dbo].[org_bind]WHERE pers_ID = ? AND org_ID = ?",(pers,org))
        #cursor.commit()
        cursor.execute("DELETE FROM peop_base_two.org_bind WHERE pers_ID = ? AND org_ID = ?",(pers,org))
        self.conn.commit()

    def delete_tie_laptop_to_person(self):
        inserting_pers = list(self.input_pers.split(" "))
        inserting_laptop = list(self.input_laptop.split(" "))
        pers = int(inserting_pers[0])
        laptop = int(inserting_laptop[0])
        cursor = self.conn.cursor()
        #cursor.execute("DELETE FROM [peop_base_two].[dbo].[laptop_bind]WHERE pers_ID = ? AND laptop_ID = ?",(pers,laptop))
        #cursor.commit()
        cursor.execute("DELETE FROM peop_base_two.laptop_bind WHERE pers_ID = ? AND laptop_ID = ?",(pers,laptop))
        self.conn.commit()

    #============== update entity =================
    def update_entity_person(self):
        changing_object = list(self.input_pers.split(" "))
        new_data = list(self.new_data_enter.split(" "))
        ID_changing_object = str(changing_object[0])
        name = str(new_data[0])
        secondname = str(new_data[1])
        surname = str(new_data[2])
        cursor = self.conn.cursor()
        #cursor.execute("UPDATE [peop_base_two].[dbo].[peoples] SET [name] = ?, [second_name] = ?, [surname] = ? WHERE pers_ID = ?",(name,secondname,surname,ID_changing_object))
        #cursor.commit()
        cursor.execute("UPDATE peop_base_two.peoples SET name = ?, second_name = ?, surname = ? WHERE pers_ID = ?",(name,secondname,surname,ID_changing_object))
        self.conn.commit()
        
    def update_entity_organization(self):
        changing_object = list(self.input_org.split(" "))
        new_data = str(self.new_data_enter)
        ID_changing_object = str(changing_object[0])
        org_data = str(new_data)
        cursor = self.conn.cursor()
        #cursor.execute("UPDATE [peop_base_two].[dbo].[organization] SET [organization_name] = ? WHERE org_ID = ?",(org_data,int(ID_changing_object)))
        #cursor.commit()
        cursor.execute("UPDATE peop_base_two.organization SET organization_name = ? WHERE org_ID = ?",(org_data,int(ID_changing_object)))
        self.conn.commit()

    def update_entity_laptops(self):
        changing_object = list(self.input_laptop.split(" "))
        new_data = str(self.new_data_enter)
        ID_changing_object = str(changing_object[0])
        laptop_data = str(new_data)
        cursor = self.conn.cursor()
        #cursor.execute("UPDATE [peop_base_two].[dbo].[laptops] SET [laptop_info] = ? WHERE laptop_ID = ?",(laptop_data,int(ID_changing_object)))
        #cursor.commit()
        cursor.execute("UPDATE peop_base_two.laptops SET laptop_info = ? WHERE laptop_ID = ?",(laptop_data,int(ID_changing_object)))
        self.conn.commit()

    #======= reports =================
    
    def people_book_reference(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        WITH conn_tab AS (
        SELECT peoples.pers_ID,
        laptop_bind.laptop_ID,
        org_bind.org_ID
        FROM peoples
        LEFT JOIN laptop_bind ON laptop_bind.pers_ID  = peoples.pers_ID
        LEFT JOIN org_bind ON org_bind.pers_ID = peoples.pers_ID 
        )
        SELECT peoples.surname,
        peoples.name,
        peoples.second_name,
        laptops.laptop_info,
        organization.organization_name
        FROM conn_tab
        LEFT JOIN peoples ON peoples.pers_ID = conn_tab.pers_ID
        LEFT JOIN laptops ON laptops.laptop_ID = conn_tab.laptop_ID
        LEFT JOIN organization ON organization.org_ID  = conn_tab.org_ID
        GROUP BY organization_name,
        peoples.surname,
        peoples.name,
        peoples.second_name,
        laptops.laptop_info,
        organization.organization_name 
        """)
        rows = cursor.fetchall()
        #print(rows)
        apt_1 = []
        for row in rows:
            name_f = str(row[1]+' '+row[2]+' '+row[0])
            laptop_f = str(row[3])
            org_f = str(row[4])
            apt_1.append((name_f,laptop_f,org_f))
        return apt_1
        
    def people_history_visits(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM history_table; 
        """)
        rows = cursor.fetchall()
        #print(rows)
        apt_1 = []
        for row in rows:
            apt_1.append((row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        return apt_1
    

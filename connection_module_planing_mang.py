import mariadb
import copy
import connection_module

class sql_driver_visit_handler(connection_module.sql_driver):

     def __init__(self,*args,**kwargs):
          self.persname=kwargs.pop('persname','1')
          self.orgname=kwargs.pop('orgname','1')
          self.startdateplaning=kwargs.pop('startdateplaning','1')
          self.finishdateplaning=kwargs.pop('finishdateplaning','1')
          self.startdateactual=kwargs.pop('startdateactual','1')
          self.finishdateactual=kwargs.pop('finishdateactual','1')
          self.laptopID=kwargs.pop('laptopID','1')
          super(sql_driver_visit_handler,self).__init__(*args,**kwargs)
        
    
     def add_entity_planing_visit(self):
          pers_name = str(self.persname)
          org_name = str(self.orgname)
          start_date_planing = str(self.startdateplaning)
          finish_date_planing = str(self.finishdateplaning)
        
          laptop_ID = str(self.laptopID)
        
          cursor = self.conn.cursor()
          '''
          cursor.execute("""INSERT INTO [peop_base_two].[dbo].[planning_entity](pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID)
                        VALUES (?,?,?,?,?)""",(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID))
          cursor.commit()
          '''
          cursor.execute("""INSERT INTO peop_base_two.planning_entity(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID)
                        VALUES (?,?,?,?,?)""",(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID))
          self.conn.commit()
         


     def ShowDataFromPlaningVisits(self):
        
          cursor = self.conn.cursor()
          ''' 
          cursor.execute("""
                        SELECT [peop_base_two].[dbo].[planning_entity].[pers_name],
                        [peop_base_two].[dbo].[planning_entity].[org_name],
                        [peop_base_two].[dbo].[planning_entity].[start_date_planing],
                        [peop_base_two].[dbo].[planning_entity].[finish_date_planing],
                        [peop_base_two].[dbo].[planning_entity].[laptop_ID],
                        [peop_base_two].[dbo].[planning_entity].[start_date_actual],
                        [peop_base_two].[dbo].[planning_entity].[finish_date_actual]
                        FROM [peop_base_two].[dbo].[planning_entity] 
                        """)
          '''

          cursor.execute("""
                        SELECT peop_base_two.planning_entity.pers_name,
                        peop_base_two.planning_entity.org_name,
                        peop_base_two.planning_entity.start_date_planing,
                        peop_base_two.planning_entity.finish_date_planing,
                        peop_base_two.planning_entity.laptop_ID,
                        peop_base_two.planning_entity.start_date_actual,
                        peop_base_two.planning_entity.finish_date_actual
                        FROM peop_base_two.planning_entity
                        """)
          rows = cursor.fetchall()
        
        
          apt = []
          for row in rows:
               ahhh = [str(row[0]),str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])]
               ahhh = row
               apt.append(ahhh)
          return apt

     def Delete_Entity_From_VisitTable(self):
          pers_name = str(self.persname)
          org_name = str(self.orgname)
          start_date_planing = str(self.startdateplaning)
          finish_date_planing = str(self.finishdateplaning)
          laptop_ID = str(self.laptopID)
          cursor = self.conn.cursor()
          '''
          cursor.execute("""
                        DELETE FROM [peop_base_two].[dbo].[planning_entity]
                        WHERE pers_name = ? AND org_name = ? AND start_date_planing = ? AND finish_date_planing = ? AND laptop_ID = ?
                        """
                       ,(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID))
          cursor.commit()
          '''
          cursor.execute("""
                        DELETE FROM peop_base_two.planning_entity
                        WHERE pers_name = ? AND org_name = ? AND start_date_planing = ? AND finish_date_planing = ? AND laptop_ID = ?
                        """
                       ,(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID))
          
          self.conn.commit()

     def Add_real_vist_date(self):
          pers_name = str(self.persname)
          org_name = str(self.orgname)
          start_date_planing = str(self.startdateplaning)
          finish_date_planing = str(self.finishdateplaning)
          start_date_actual = str(self.startdateactual)
          finish_date_actual = str(self.finishdateactual)
        
          laptop_ID = str(self.laptopID)
        
          cursor = self.conn.cursor()
          '''
          cursor.execute("""UPDATE [peop_base_two].[dbo].[planning_entity] SET [start_date_actual] = ?, [finish_date_actual] = ?
                        WHERE pers_name = ? AND org_name = ? AND start_date_planing = ? AND finish_date_planing = ? AND laptop_ID = ?"""
                       ,(start_date_actual,finish_date_actual,pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID))
          cursor.commit()
          '''
          cursor.execute("""UPDATE peop_base_two.planning_entity SET start_date_actual = ?, finish_date_actual = ?
                        WHERE pers_name = ? AND org_name = ? AND start_date_planing = ? AND finish_date_planing = ? AND laptop_ID = ?"""
                       ,(start_date_actual,finish_date_actual,pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID))
          self.conn.commit()
        

     def Add_entity_to_history(self):
          pers_name = str(self.persname)
          org_name = str(self.orgname)
          start_date_planing = str(self.startdateplaning)
          finish_date_planing = str(self.finishdateplaning)
          start_date_actual = str(self.startdateactual)
          finish_date_actual = str(self.finishdateactual)
          laptop_ID = str(self.laptopID)
          cursor = self.conn.cursor()
          '''
          cursor.execute("""
                        INSERT INTO [peop_base_two].[dbo].[history_table](pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID,start_date_actual,finish_date_actual)
                        VALUES (?,?,?,?,?,?,?)
                        """,(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID,start_date_actual,finish_date_actual))
          cursor.commit()
          '''
          cursor.execute("""
                        INSERT INTO peop_base_two.history_table(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID,start_date_actual,finish_date_actual)
                        VALUES (?,?,?,?,?,?,?)
                        """,(pers_name,org_name,start_date_planing,finish_date_planing,laptop_ID,start_date_actual,finish_date_actual))
          self.conn.commit()

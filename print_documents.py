from fpdf import FPDF, HTMLMixin
from docxtpl import DocxTemplate
import copy

class document_printer():
    
	def __init__(self,guest_name='1',dates_doc='1',laptop_a='1',mult_vis='1',reports='1'):
		self.guest_name = guest_name
		self.dates_doc = dates_doc
		self.laptop_a = laptop_a
		self.mult_vis = mult_vis
		self.reports = reports
	def __del__(self):
		class_name = self.__class__.__name__
		print(f" {class_name} object have been destored")
        
	def __doc_pattern(self,visiting_dates,owner,laptop_doc):
		pdf = FPDF('P','mm','Letter')
		FPDF_FONTPATH = "/home/myname/.local/lib/python3.10/site-packages/fpdf/font"
		#pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
		pdf.add_font('DejaVu', '',FPDF_FONTPATH+'/DejaVuSansCondensed.ttf', uni=True)
		pdf.add_font('DejaVu', 'B',FPDF_FONTPATH+'/DejaVuSansCondensed-Bold.ttf', uni=True)
		pdf.add_font('DejaVu', '',FPDF_FONTPATH+'/DejaVuSansCondensed-Oblique.ttf', uni=True)
		pdf.add_font('DejaVu', '',FPDF_FONTPATH+'/DejaVuSansCondensed-BoldOblique.ttf', uni=True)

		pdf.set_font('DejaVu','',16)
		
		for iterat in visiting_dates:
			pdf.add_page()
			pdf.cell(130,10,'Служебная записка')
			pdf.cell(80,10,'Начальнику охраны',ln=True)
			pdf.cell(80,10,' ',ln=True)
			pdf.cell(80,10,'Прошу разрешить внос на территортю предприятия ',ln=True)
			date = iterat
	#pdf.multi_cell(0, 5, txt = date[0] + ' ' +date[1] + ' ' + date[2], border=1)
			pdf.set_line_width(0.4)
			pdf.cell(9, 7, txt = 'На')
			pdf.cell(15, 7, txt = "«"+date[0]+"»")
			pdf.cell(20, 7, txt = date[1],border="B")
			pdf.cell(12, 7, txt = date[2],ln=True)
			pdf.cell(12, 2, txt = '',ln=True)
			pdf.cell(53, 7, txt = "В сопровождении:")
			pdf.cell(20, 7, txt = owner)
			pdf.cell(80,10,'',ln=True)
			pdf.set_line_width(0.2)
			'''
			TABLE_DATA = [
    			("№ Позиции", "Название ноутбука"),
    			("1", "Toshiba"),
			]
			'''
			TABLE_DATA = [
    			("№ Позиции", "Название ноутбука")
			]
			iterator_count = 0
			for j in laptop_doc:
				iterator_count += 1
				TABLE_DATA.append((str(iterator_count),str(j)))
			
			with pdf.table(first_row_as_headings=False,col_widths=(1, 2),text_align=("CENTER", "CENTER")) as table:
				for data_row in TABLE_DATA:
					row = table.row()
					for datum in data_row:
						row.cell(datum)

			pdf.set_line_width(0.4)
			pdf.cell(100, 10, txt = '',ln=True,border="B")
			pdf.cell(100, 4, txt = '',ln=True)
			pdf.cell(55, 10, txt = 'Начальник отдела:')
			pdf.cell(70, 8, txt = '',ln=True,border="B")
			pdf.cell(100, 4, txt = '',ln=True)
			pdf.cell(25, 10, txt = 'Сторож:')
			pdf.cell(70, 8, txt = '',ln=True,border="B")
		pdf.output("documents/pdf_1.pdf")	

	def __doc_pattern_pers_pass(self):
		doc = DocxTemplate("test3_template .docx")
		name_org_data = self.mult_vis
		starting_date = self.__date_converting(self.dates_doc[0])
		finish_date = self.__date_converting(self.dates_doc[1])
		date_1 = starting_date['day'] +' '+ starting_date['month'] +' '+ starting_date['year']
		date_2 = finish_date['day'] +' '+finish_date['month'] +' '+ finish_date['year']
		people_info = self.__org_pers_sort(name_org_data)
		content = {"start_date":date_1, "finish_date":date_2, "invoice_list":people_info}
		doc.render(content)
		doc.save("documents/new_invoice.docx")

		
		
	
	def __org_pers_sort(self,mult_vis):
	
		string_two_two = mult_vis
		name_dict = {}

		for j in range(len(string_two_two)):
			string_middle = string_two_two[j]
			name_dict[j] = {"name": string_middle[0],
					"org": string_middle[1]
							}
					
		string_temp_org_2 = []

		for i in name_dict:
			string_temp_org_2.append(name_dict[i]["org"])



		sting_temp_org_uni = list(set(string_temp_org_2))
		sting_temp_org_uni.sort(key = lambda k : k.lower())


		organiz_plus_peop_order = []
		tempr_var_for_pers = []
		for string in sting_temp_org_uni:
			for i in name_dict:
				if name_dict[i]["org"] == string:
					tempr_var_for_pers.append(i)
			tempere = copy.copy(tempr_var_for_pers)
			organiz_plus_peop_order.append([string,tempere])
			tempr_var_for_pers[:] = []


		pass_people_org_list = []
		middle_string_c = []
		for i in organiz_plus_peop_order:
			middle_item = i
			middle_item_a = middle_item[1]
			middle_item_b = middle_item[0]
			for j in middle_item_a:
				middle_string_c.append(name_dict[j]["name"])
			middle_string_c.sort(key = lambda k : k.lower())
			tempere = copy.copy(middle_string_c)
			pass_people_org_list.append([middle_item_b,tempere])
			middle_string_c[:] = []
		return pass_people_org_list

		
    
	def __date_converting(self,date):
		date_convert = date
		month_list = {  '1': 'января',
						'2': 'февраля',
						'3': 'марта',
						'4': 'апреля',
						'5': 'мая',
						'6': 'июня',
						'7': 'июля',
						'8': 'августа',
						'9': 'сентября',
						'10': 'октября',
						'11': 'ноября',
						'12': 'декабря',
					}
		if int(date_convert[0]) < 10:
			day = '0' + str(date_convert[0])
		else:
			day = str(date_convert[0])

		month = month_list[str(date_convert[1])]
		year = str(date_convert[2])
		list_date_row = { 'day': day, 'month': month, 'year': year}
		return list_date_row
    
	def print_doc_laptops(self):
		name = str(self.guest_name)
		laptop = str(self.laptop_a)
		pass_dates_visit = []
		for focus_dates in self.dates_doc:
			print('guy with name: ' + str(self.guest_name) + '\n')
			dispo_var = self.__date_converting(focus_dates)
            #print('visit this cloack in: ' + dispo_var['day'] + ' ' + dispo_var['month'] +' '+ dispo_var['year'] +'\n')
			var = [dispo_var['day'],dispo_var['month'],dispo_var['year']]
			pass_dates_visit.append(var)
			#print(pass_dates_visit)
		
		laptop_pass_a = laptop[2:-3]
		laptop_pass_b = laptop_pass_a.split(';')
		
		self.__doc_pattern(pass_dates_visit,name,laptop_pass_b)
		
		
		
		 
            
	def print_person_pass_doc(self):
		name = str(self.guest_name)
		date_dis_start = self.__date_converting(self.dates_doc[0])
		date_dis_finish = self.__date_converting(self.dates_doc[-1])
        
		date_start = date_dis_start['day'] + ' ' + date_dis_start['month'] +' '+ date_dis_start['year']
		date_finish = date_dis_finish['day'] + ' ' + date_dis_finish['month'] +' '+ date_dis_finish['year']
		print(f'Прошу пропустить {name} в офис с {date_start} по {date_finish}')
		
	def print_person_mult_visit(self):
		self.__doc_pattern_pers_pass()
		
	def print_report_book(self):
		doc = DocxTemplate("template_ref_book.docx")
		data_list = self.reports
		content = {"ref_book_list":data_list}
		doc.render(content)
		doc.save("documents/ref_book_visit.docx")
		
	def print_history_report(self):
		doc = DocxTemplate("template_history_report.docx")
		data_list = self.reports
		print(data_list)
		content = {"history_list":data_list}
		doc.render(content)
		doc.save("documents/history_report.docx")
		
		
        

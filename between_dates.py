from datetime import timedelta, date

class Dateline:
    
    def __init__ (self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __del__(self):
        class_name = self.__class__.__name__
        print(f" {class_name} object have been destored")

    def printing (self):
        rewrite_mass_mass = self.__rewrite_mass()
        for ups in range(len(rewrite_mass_mass)):
            print(str(rewrite_mass_mass[ups]['day']) + '.' + str(rewrite_mass_mass[ups]['month']) + '.' + str(rewrite_mass_mass[ups]['year']))


    def show_dates(self):
        rewrite_mass_mass = self.__rewrite_mass()
        dates_for_print_doc = []
        for ups in range(len(rewrite_mass_mass)):
            day = int(rewrite_mass_mass[ups]['day'])
            month = int(rewrite_mass_mass[ups]['month'])
            year = int(rewrite_mass_mass[ups]['year'])
            dates_for_print_doc.append((day,month,year))
        return dates_for_print_doc
    
    

    def __rewrite_mass(self):
        dates_between = self.__get_between_dates()
        for ups in range(len(dates_between)):
            if dates_between[ups]['day'] < 10:
                dates_between[ups]['day'] = '0' + str(dates_between[ups]['day'])
            else:
                dates_between[ups]['day'] = str(dates_between[ups]['day'])

            if dates_between[ups]['month'] < 10:
                dates_between[ups]['month'] = '0' + str(dates_between[ups]['month'])
            else:
                dates_between[ups]['month'] = str(dates_between[ups]['month'])
        
            dates_between[ups]['year'] = str(dates_between[ups]['year'])
        return dates_between

    def __get_between_dates(self):
        test_test = {}
        for i in range((self.end_date - self.start_date).days + 1):
            temp = self.start_date + timedelta(days=i)
            test_test[i] = {'day': temp.day,
                            'month': temp.month,
                            'year': temp.year}
        return test_test


import record
import view
import export_info
import import_info


def run():
    option = view.choise_option()
    
    if option == '*':
        print('Запись нового контакта.\n')
        format = view.choise_format()
        if format == 's':         

            import_info.input_format1(record.record())

        if format == 'p':            

            import_info.input_format2(record.record())


    if option == '#':
        print('Вывод телефонной книги.\n')
        see = view.choise_see()
        if see == 's':        

            export_info.see_file_sim()


        if see == 'p':            

            export_info.see_file_phone()


       
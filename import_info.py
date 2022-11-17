import datetime
import record

def input_format1(enter):

    with open('telephone_book.csv', 'a') as file:
        file.write(f'{enter[0]}\n{enter[1]}\n{enter[2]}\n{enter[3]}\n{enter[4]}\n\n')        

def input_format2(enter):

    with open('telephone_book.txt', 'a') as file:
        file.write(f'{enter[0]} {enter[1]} {enter[2]} {enter[3]} {enter[4]}\n\n')
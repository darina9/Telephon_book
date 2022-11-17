def see_file_sim():
    with open('telephone_book.csv', 'r') as file:
        for line in file:
            print(line)


def see_file_phone():
    with open('telephone_book.txt', 'r') as file:
        for line in file:
            print(line)
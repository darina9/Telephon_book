def record():
    enter = []
    surname = input('Фамилию: ')
    enter.append(surname)
    name = input('Имя: ')
    enter.append(name)
    middle = input('Отчество: ')
    enter.append(middle)
    description = input('Дополнительная информация: ')
    enter.append(description)
    phone = input('Номер телефона: ')
    enter.append(phone)
    
    print('Добавлен новый контакт: ',*enter, sep=' ')
    return enter
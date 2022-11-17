def choise_option():
    print('Вы вошли в телефонную книгу.')
    option = (input('Какое действие хотите сделать?: \n \
        * - Добавить контакт. \n \
        # - Получить список контактов.\n'))
    return option

def choise_format():
    format = (input('Выберите вариант записи контакта: \n \
        s - Запись на sim card. \n \
        p - Запись в память телефона.\n'))
    return format


def choise_see():
    see = (input('Просмотреть контакты с : \n \
        s - Sim card. \n \
        p - Память телефона.\n'))
    return see
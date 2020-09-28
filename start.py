

id_list = [] id зареганных людей
persons = {
    id: class
}

if message.id not in id_list:
    # Нет в зареганных людях
    pass
else:
    persons[id] = DataBase.select()
'''
программа работы со словарем
меню: 
1. Посмотреь все записи
2. Добавить запись
3. Изменить
4. Удалить
5. Импорт
6. Экспорт
7. Выход из программы
'''
# import math
from os import path
# import pyperclip

file_base = "base.txt"
# file_exp = ''
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, 'w', encoding="utf-8") as _:
        pass

def read_records():
    global last_id, all_data
    # if last_id:
    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        last_id = len(all_data)
    return all_data, last_id
    # return[]
    f.close()

 
def show_all(): # 1 Show all records
    read_records()
    print(f"Всего записей: {last_id}")
    if all_data:
        print(*all_data, sep="\n")
        # print(all_data)
    else:
        print("Данных нет")

def add_new_contact(): # 2. Add a record
    # print(last_id)
    array = ['фамилия', 'имя', 'отчество', 'номер телефона']
    string = ""
    for i in array:
        string += input(f"Вводите данные клавишей Enter {i} ") + " "
    last_id +=1

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")
        
def search_rec(): #3. Search a record
    user_input = input("Введите имя/фамилию/телефон: ")
    # user_input = "Иванов"
    part_list =[all_data[i] for i in range(len(all_data)) if user_input in all_data[i]]
    if part_list:
        print('\n'.join(part_list))
    else:
        print('Таких записей нет')
    # pass

def change_rec(): # 4. Change
    print(f'Всего записей {last_id}')
    print(*all_data, sep="\n")
    user_input = int(input("Введите номер записи для изменения: "))
    print(f"выделите мышью и скопируйте запись:\n{all_data[user_input-1]}\nи вставьте в поле ввода правой клавишей мыши")
    # data = all_data[user_input+1]
    # pyperclip.copy(data)
    change_record = input('')
    # print(change_record)
    all_data[user_input-1] = change_record
    with open(file_base, 'w', encoding="utf-8") as f:
        for i in all_data:
            f.write("%s\n" % i)

def delete_rec(): # 5. Delete
    user_input = int(input("Введите номер записи для удаления: "))
    answer = input(f"подтверждаете удаление записи:\n{all_data[user_input-1]}?\nyes/no\n")
    if answer == "no":
        print("...отмена")
        pass
    else:
        # new_data = []
        del all_data[user_input-1]
        for k in range(len(all_data)):
            all_data[k] = f"{k+1} {all_data[k][2:]}"
            # print(all_data[k])
        with open(file_base, 'w', encoding="utf-8") as f:
            for i in all_data:
                f.write("%s\n" % i)
        print("...запись удалена")

def export_recs(): # 6. Export records
    file_exp = input('Введите имя файла для экспорта: ') + '.txt'
    with open(file_exp, 'w', encoding="utf-8") as f:
        for i in all_data:
            f.write("%s\n" % i)
    print(f'Данные успешно экcпортированы в файл "{file_exp}"')

def import_recs(): # 7. Import records
     file_imp = input('Введите имя импортируемого файла: ') + '.txt'
    #  file_imp = 'mImport.txt'
     with open(file_imp, 'r', encoding="utf-8") as f1:
        with open(file_base, 'w', encoding="utf-8") as f2:
            f2.write(f1.read())
            
     print(f'Данные файла" {file_imp}" успешно импортированы')

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n" #+
                       "2. Add a record\n" #+
                       "3. Search a record\n" #+
                       "4. Change\n" #+
                       "5. Delete\n"
                       "6. Exp\n"
                       "7. Imp\n"
                       "8. Exit\n") #+
        match answer:
            case "1":
                show_all()
                play = False
                
            case "2": # Add new record
                add_new_contact()
                print("...запись внесена")
                play = False
            case "3": # Search a record
                search_rec()
                play = False
            case "4": # Change
                change_rec()
                print("...запись изменена")
                play = False
            case "5": # Delete
                delete_rec()
                # print('обновленный список', *all_data, sep="\n")
                play = False
            case "6": # Exp
                export_recs()
                play = False
            case "7": # Imp
                import_recs()
                play = False
            case "8": # exit
                print("...программа закрыта")
                play = False
            case _:
                print("Try again!\n")


main_menu()
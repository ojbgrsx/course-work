from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
id = '1cTg4QyIFSBJeQjuXk8dgJTTMpyGtzIPvkdz5Sd0wyhM'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
mains = sheet.values().get(spreadsheetId=id, range="mains!A1:C999").execute()
worker = sheet.values().get(spreadsheetId=id, range="worker!A1:C999").execute()
values_mains = mains.get('values', [])
values_worker = worker.get('values', [])
i = len(values_worker) + 1


def director_menu():
    print(' \n YOU ARE WELCOME BOSS !!! \n ')
    print('1) Show a list of all customer coverage areas by district ')
    # 1) Показывает список районов с количеством клиентов
    print('2) Show list of budget categories ')
    # 2) Показывает категорию бюджета: бюджет для маркетинга, бюджет для заработной платы
    print('3) Show dedicated budget for a specific category of marketing sites ')
    # 3) Показывает список зон для маркетинга, а затем в зависимости от выбора показывается бюджет для маркетинга
    print('4) Show current marketing funds ')
    # 4) Показывает общие средства для маркетинга, в случае если маркетолог
    # потратил определенные средства на маркетинг, то понижаются и средства
    print('5) Show total budget required for salary ')
    # 5) Показывает общий бюджет для зарплаты, в случае повышение
    # зарплаты, увеличивается и бюджет, который необходим, в случае
    # если зарплата понижается, то понижается и требования для бюджет
    print('6) Increase the salary of an employee: ')
    # 6) Повышает зарплату сотрудника
    print('7) Lower the salary of an employee')
    # 7) Понижает зарплату сотрудника
    print('8) Exit ')
    # 8) Выход
    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 8: '))
    if menu <= 0 or menu > 8:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        director_menu()
    elif menu == 8:
        print(' \nThe program is over, we look forward to your return! \n ')


def manager_menu():
    print(' \n YOU ARE WELCOME MANAGER !!! \n ')
    print('1) Show list of employees ')
    # 1) Показывает список всех сотрудников
    print('2) Show to-do list ')
    # 2) Показывает список всех дел, которую необходимо выполнить
    print('3) Show a list of instructions to employees ')
    # 3) Показывает список всех указаний по сотрудникам
    print('4) Show a list of all customer coverage areas by district ')
    # 4) Показывает количество людей - клиентов данной организации
    print('5) Calculate ')
    # 5) Тут есть подменю
    print('6) Give an assignment to employees ')
    # 6) Пишется в отдельный файл «tasks.txt» имя сотрудника и название задания,
    # где помимо всего прочего указывается и дата задания с помощью библиотеки datetime)
    print('7) Exit ')
    # 7) Выход
    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 7: '))
    if menu <= 0 or menu > 7:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        manager_menu()
    elif menu == 7:
        print(' \nThe program is over, we look forward to your return! \n ')


def marketer_menu():

    print('1) Show a list of all customer coverage areas by district ')
    # 1) Показывает количество людей - клиентов данной организации из файла «clients.txt»
    print('2) Show a list of categories for marketing')
    # 2) Показывает список мест для маркетинга, как пример это может быть Фейсбук, Инстаграм
    # и т.д. и количество пользователей того или иного приложения
    print('3) Show dedicated budget for a specific category of marketing sites ')
    # 3) Показывает список зон для маркетинга, а затем в зависимости от выбора показывается бюджет для маркетинга
    print('4) Show total budget for marketing ')
    # 4) Показывает общий бюджет маркетинга
    print('5) Spend your promotion budget ')
    # 5) Нужно выбрать название для продвижения: Instagram,Facebook,YouTube и т.д.
    print('6) Exit')
    # 6) Выход
    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 6: '))
    if menu <= 0 or menu > 6:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        marketer_menu()
    elif menu == 6:
        print(' \nThe program is over, we look forward to your return! \n ')


def worker_menu(name):
    print('1) Show a list of tasks assigned to me ')
    # 1) Показывает список порученных дел для этого сотрудника из файла “tasks.txt”
    print('2) Complete the case:')
    # 2) Здесь пишется название дела, которую собирается выполнить сотрудник.
    # После того, как сотрудник ввел название дело, которую сотрудник хочет выполнить,
    # то это дело автоматически удаляется из файла “tasks.txt” и одновременно записывается в файл
    # “completed-tasks.txt” с указанием имени сотрудника и название дела
    print('3) Show list of completed instructions ')
    # 3) Показывает список завершенных дел для этого сотрудника из файла “completed-tasks.txt”
    print('4) Show salary ')
    # 4) Показывается текущая зарплата для этого сотрудника из файла “salary.txt”
    print('5) Exit')
    # 5) Выход
    print(name.upper())
    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 5: '))
    if menu == 1:
        print()
        f = open('tasks.txt', 'r')
        print(f.read())
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu()
    elif menu == 2:
        task = open('tasks.txt')
        print()
        print(task.read().strip())
        task.close()
        print('Please type the FIRST WORD of the work to COMPLETE\n')
        q = input()
        uncompleted = []
        completed = ['Done by {}: '.format(name.upper())]
        task = open('tasks.txt')
        for i in task:
            if i.split()[0] == q:
                completed.append(i)
            else:
                uncompleted.append(i)
        task.close()
        task = open("tasks.txt", 'w')
        task.writelines(uncompleted[:])
        task.close()
        complete = open('completed.txt', 'a')
        complete.writelines(completed[:])
        complete.close()

        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu == 3:
        complete = open('completed.txt')
        print()
        for f in complete:
            if name.upper() in f:
                print(f, end='')
        print()
        complete.close()
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu == 4:
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu <= 0 or menu > 5:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        worker_menu(name)
    elif menu == 5:
        print(' \nThe program is over, we look forward to your return! \n ')
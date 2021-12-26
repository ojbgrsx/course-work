from google_api import *
from menus import *
print('\n')
print('   >>> WELCOME  TO OUR COMPANY !!! <<<   ')
print('\n')
i = len(values_worker_with_username) + 1

# Adding to "workers.txt" refreshed list of workers

with open('workers.csv', mode='w') as f:
    wl = csv.writer(f, delimiter=',')
    wl.writerows(values_worker_with_username)

# Registration


def sign_up():
    c = 0
    l = []
    n = input('Username >>> ').strip().lower()
    for exist in sheet.values().get(spreadsheetId=id, range="worker!A2:A999").execute().get('values', []):
        if n in exist:
            c += 1
    if c == 0:
        l.append(n)
        s = input('Password >>> ').strip().lower()
        l.append(s)
        sheet.values().update(spreadsheetId=id, range="worker!A{}".format(
            i), valueInputOption="USER_ENTERED", body={'values': [l]}).execute()
        print('Congratulations. You have successfully signed up !!! \n')
        print('Your USERNAME is: ', l[0], '\nYour PASSWORD is: ', l[1], '\n')
    else:
        print('\nThis username is already EXIST, please try another USERNAME\n')
        sign_up()

# Choosing type of account and signing in


def account():

    have = input('Do you have an account ? (yes/no) >>> ').lower().strip()
    print()
    if have == 'yes':
        print('Please choose type of your account: \n\n 1)Director \n 2)Manager \n 3)Marketing \n 4)Worker \n')
        a = int(input('Please enter a number (1-4) to log in, (0) to exit >>> '))
        print('')
        if a == 1:
            print(' YOU ARE IN DIRECTOR ACCOUNT! \n')
            for z in range(3):
                direc_login = input('Enter username >>> ').lower().strip()
                if direc_login in sheet.values().get(spreadsheetId=id, range="mains!A2").execute().get('values', [])[0]:
                    for j in range(3):
                        direc_password = input(
                            'Enter password >>> ').lower().strip()
                        if direc_password in sheet.values().get(spreadsheetId=id, range="mains!B2").execute().get('values', [])[0]:
                            director_menu()
                            break
                        else:
                            if j != 2:
                                print('Try again!!!')
                            else:
                                print('You have wasted all password attempts!!!')
                    break
                else:
                    if z != 2:
                        print('Try again!!!')
                    else:
                        print('You have wasted all username attempts!!!')
        elif a == 2:
            print(' YOU ARE IN MANAGER ACCOUNT! \n')
            for z in range(3):
                manager_login = input('Enter username >>> ').lower().strip()
                if manager_login in sheet.values().get(spreadsheetId=id, range="mains!A3").execute().get('values', [])[0]:
                    for j in range(3):
                        mana_password = input(
                            'Enter password >>> ').lower().strip()
                        if mana_password in sheet.values().get(spreadsheetId=id, range="mains!B3").execute().get('values', [])[0]:
                            manager_menu()
                            break
                        else:
                            if j != 2:
                                print('Try again!!!')
                            else:
                                print('You have wasted all password attempts!!!')
                    break
                else:
                    if z != 2:
                        print('Try again!!!')
                    else:
                        print('You have wasted all username attempts!!!')
        elif a == 3:
            print(' YOU ARE IN MARKETER ACCOUNT TYPE! \n')
            for z in range(3):
                market_login = input('Enter username >>> ').lower().strip()
                if market_login in sheet.values().get(spreadsheetId=id, range="mains!A4").execute().get('values', [])[0]:
                    for j in range(3):
                        marketing_password = input(
                            'Enter password >>> ').lower().strip()
                        if marketing_password in sheet.values().get(spreadsheetId=id, range="mains!B4").execute().get('values', [])[0]:
                            marketer_menu()
                            break
                        else:
                            if j != 2:
                                print('Try again!!!')
                            else:
                                print('You have wasted all password attempts!!!')
                    break
                else:
                    if z != 2:
                        print('Try again!!!')
                    else:
                        print('You have wasted all username attempts!!!')
        elif a == 4:
            print('YOU ARE IN WORKER ACCOUNT! \n')
            for z in range(3):
                work_login = input('Enter username >>> ').lower().strip()
                if [work_login] in sheet.values().get(spreadsheetId=id, range="worker!A2:A999").execute().get('values', []):
                    for check in values_worker_with_username:
                        if work_login == check[0]:
                            for j in range(3):
                                worker_password = input(
                                    'Enter password >>> ').lower().strip()
                                if worker_password == check[1]:
                                    print(' \n YOU ARE WELCOME {} !!! \n '.format(
                                        work_login.upper()))
                                    worker_menu(work_login)
                                    break
                                else:
                                    if j != 2:
                                        print('\nWrong password')
                                        print('Try again!!!\n')
                                    else:
                                        print(
                                            '\nYou have wasted all password attempts!!!')
                            break
                    break
                else:
                    if z != 2:
                        print('\nWe have not find account with this username!!!')
                        print('Try again!!!\n')
                    else:
                        print('\nYou have wasted all username attempts!!!')
        else:
            if a != 0:
                print(
                    ' >>> SORRY, BUT WE DID NOT FIND THIS TYPE OF ACCOUNT, PLEASE TRY AGAIN. <<< \n')
                account()
    elif have == 'no':
        print('\nThen you should sign up as WORKER\n')
        sign_up()
    else:
        print('Please try again!!!')
        account()


account()

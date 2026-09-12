from getpass import win_getpass

waste = input("enter waste type: ")win_getpass()

if waste == "wet" :
    print('put it in the wet waste bin')
elif waste == "dry" :
    print('put it in the dry waste bin')
else :
    print('unknown waste type')



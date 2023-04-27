wifi = bool(input())
login = bool(input())
admin = bool(input())

if wifi==False:
    print('you must connect to wifi')
else:
    if login==False:
        print('you need to login first')
    else:
        if admin==False:
            print('you must to login as admin')
        else:
            print('done')
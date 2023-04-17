def menu_login():
    while True:
        print(f'''
             SELAMAT DATANG DI OREGEON RENT CAR


        +==========================================+
        |               1. Login                   |
        +==========================================+
        |               2. Daftar                  |
        +==========================================+
        ''')

        pilihan = input('\nPilihan > ')
        os.system('cls')
        if pilihan == '1':
            login()
        elif pilihan == '2':
            daftar()
# akhir menu login

def login():
    i  = 0
    while i < 3:
        print('===== Login =====')
        username = input('Username    : ')
        passw    = getpass.getpass('Password    : ')
        
        if i == 2:
            os.system('cls')
            break
        elif username == 'admin' and passw == '123':
            os.system('cls')
            menu_utama()
        elif username in data_username and passw in data_passw:
            os.system('cls')
            menu_utama()
        elif username not in data_username and passw not in data_passw:
            os.system('cls')
            print(Fore.RED + 'Akun tidak terdaftar!' + Style.RESET_ALL)
            break
        else:
            os.system('cls')
            print(Fore.RED + 'username atau password salah!' + Style.RESET_ALL)
            lagi = input('Coba Lagi? [y/n]> ')
            os.system('cls')
            if lagi == 'n':
                menu_login()
             
        i = i + 1
# akhir login
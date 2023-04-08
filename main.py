from colorama import Fore,Style
import os

def menu_utama():
    while True:
        print('\n+============================================================+')
        print('|                      Oregeon Rent Car                      |')
        print('|                   Ruko Casa Grande No. 17                  |')
        print('|           Jl. Ringroad Utara, 55283, Yogyakarta            |')
        print('+============================================================+')
        print('|    [1] Admin                                               |')                                          
        print('|    [2] Daftar Mobil                                        |')
        print('|    [3] Rental                                              |')
        print('|    [0] Keluar                                              |')
        print('+============================================================+')
        inp_menu = input('\nPilihan Menu> ')
        os.system('cls')
        if inp_menu == '1':
            login_admin()
        elif inp_menu == '2':
            menu_mobil()
        elif inp_menu == '3':
            rent()
        elif inp_menu == '0':
            exit()
        else:
            print(Fore.RED + 'Pilihan Salah!' + Style.RESET_ALL)
os.system('cls')
# akhir menu utama

def login_admin():
        ulang_dftr_menu = 'y'
        while ulang_dftr_menu == 'y':
            print('====== Login ======\n')
            password = input('Password: ')
            if password == '123':
                os.system('cls')
                print('Selamat Datang, Admin\n')
                menu_login_admin()
            else:
                os.system('cls')
                print(Fore.RED + 'Entry password invalid!' + Style.RESET_ALL)
                ulang_dftr_menu = input('\nKembali ke Menu Utama [y/n]: ')
                os.system('cls')
                if ulang_dftr_menu == 'y':
                    menu_utama()
                else:
                    login_admin()
# akhir menu 1 login

def menu_mobil():
    while True:
        menu_daftar_mobil()
        
        pil_mobil= input('Pilih Mobil> ')
        os.system('cls')
        if pil_mobil == '0':
            menu_utama()
        elif pil_mobil == '1':
            avanza()
            input('Kembali [enter]> ')
            os.system('cls')
        elif pil_mobil == '2':
            innova()
            input('Kembali [enter]> ')
            os.system('cls')
        elif pil_mobil == '3':
            hiace()
            input('Kembali [enter]> ')
            os.system('cls')
        elif pil_mobil == '4':
            elf()
            input('Kembali [enter]> ')
            os.system('cls')
        elif pil_mobil == '5':
            pajero()
            input('Kembali [enter]> ')
            os.system('cls')
        elif pil_mobil == '6':
            fortuner()
            input('Kembali [enter]> ')
            os.system('cls')
        elif pil_mobil == '7':
            alphard()
            input('Kembali [enter]> ')
            os.system('cls')
        else:
            print(Fore.RED + 'Pilihan Salah!' + Style.RESET_ALL)
            menu_mobil()
# akhir menu mobil

def rent():
    # os.system('cls')
    while True:
        print('='*65)
        print('Form Sewa Mobil'.center(65))
        print('='*65)
        try:
            nama      = input('Nama                : ',)
            no_hp     = input('No. Hp              : ')
            alamat    = input('Alamat              : ')
            list_mobil()
            armada    = input('\nJenis Mobil         : ')
            durasi    = input('Durasi Sewa (12/24) : ')
            if armada == 'Avanza' or armada == 'avanza' or  armada == 'Innova' or armada == 'innova':
                print(f'''Tipe Sewa:\nLepas Kunci\nPlus Sopir\nSopir + BBM
                    ''')
            else:
                print('-Sopir + BBM')
            tipe_sewa = input('Tipe Sewa           : ')
            if durasi == '24':
                inp_hari      = (input('Hari                : '))
                hari = int(inp_hari)

            if armada == 'Avanza' or armada == 'avanza':
                mobil = mobil_avanza[0][1]
                plat = mobil_avanza[0][8]
                mobil_avanza.pop(0)
                if durasi == '12' and tipe_sewa == 'Lepas Kunci' or tipe_sewa == 'lepas kunci':
                    harga = mobil_avanza[0][2]
                    total_harga = str(harga)
                elif durasi == '24' and tipe_sewa == 'Lepas Kunci' or tipe_sewa == 'lepas kunci':
                    harga = mobil_avanza[0][3] * hari
                    total_harga = str(harga)
                elif durasi == '12' and tipe_sewa == 'Plus Sopir' or tipe_sewa == 'plus sopir':
                    harga = mobil_avanza[0][4]
                    total_harga = str(harga)
                elif durasi == '24' and tipe_sewa == 'Plus Sopir'  or tipe_sewa == 'plus sopir':
                    harga = mobil_avanza[0][5] * hari
                    total_harga = str(harga)
                elif durasi == '12' and tipe_sewa == 'Sopir + BBM' or tipe_sewa == 'sopir + bbm':
                    harga = mobil_avanza[0][6]
                    total_harga = str(harga)
                else:
                    harga = mobil_avanza[0][7] * hari
                    total_harga = str(harga)
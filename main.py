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
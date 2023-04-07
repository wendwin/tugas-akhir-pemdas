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
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
                    
            elif armada == 'Innova' or armada == 'innova':
                mobil = mobil_innova[0][1]
                plat = mobil_innova[0][8]
                mobil_innova.pop(0)
                if durasi == '12' and tipe_sewa == 'Lepas Kunci' or tipe_sewa == 'lepas kunci':
                    harga = mobil_innova[0][2]
                    total_harga = str(harga)
                elif durasi == '24' and tipe_sewa == 'Lepas Kunci' or tipe_sewa == 'lepas kunci':
                    harga = mobil_innova[0][3] * hari
                    total_harga = str(harga)
                elif durasi == '12' and tipe_sewa == 'Plus Sopir' or tipe_sewa == 'plus sopir':
                    harga = mobil_innova[0][4]
                    total_harga = str(harga)
                elif durasi == '24' and tipe_sewa == 'Plus Sopir' or tipe_sewa == 'plus sopir':
                    harga = mobil_innova[0][5] * hari
                    total_harga = str(harga)
                elif durasi == '12' and tipe_sewa == 'Sopir + BBM' or tipe_sewa == 'sopir + bbm':
                    harga = mobil_innova[0][6]
                    total_harga = str(harga)
                else:
                    harga = mobil_innova[0][7] * hari
                    total_harga = str(harga~)

            elif armada == 'Hiace' or armada == 'hiace':
                mobil = mobil_hiace[0][1]
                plat = mobil_hiace[0][4]
                mobil_hiace.pop(0)
                if durasi == '12' and tipe_sewa == 'Sopir + BBM' or tipe_sewa == 'sopir + bbm':
                    harga = mobil_hiace[0][2]
                    total_harga = str(harga)
                else:             
                    harga = mobil_hiace[0][3] * hari
                    total_harga = str(harga)

            elif armada == 'Elf' or armada == 'elf':
                mobil = mobil_elf[0][1]
                plat = mobil_elf[0][4]
                mobil_elf.pop(0)
                if durasi == '12' and tipe_sewa == 'Sopir + BBM' or tipe_sewa == 'sopir + bbm':
                    harga = mobil_elf[0][2]
                    total_harga = str(harga)
                else:
                    harga = mobil_elf[0][3] * hari
                    total_harga = str(harga)

            elif armada == 'Pajero' or armada == 'pajero':
                mobil = mobil_pajero[0][1]
                plat = mobil_pajero[0][4]
                mobil_pajero.pop(0)
                if durasi == '12' and tipe_sewa == 'Sopir + BBM' or tipe_sewa == 'sopir + bbm':
                    harga = mobil_pajero[0][2]
                    total_harga = str(harga)
                else:
                    harga = mobil_pajero[0][3] * hari
                    total_harga = str(harga)

            elif armada == 'Fortuner' or armada == 'fortuner':
                mobil = mobil_fortuner[0][1]
                plat = mobil_fortuner[0][4]
                mobil_fortuner.pop(0)
                if durasi == '12' and tipe_sewa == 'Sopir + BBM' or tipe_sewa == 'sopir + bbm':
                    harga = mobil_fortuner[0][2]
                    total_harga = str(harga)
                else:
                    harga = mobil_fortuner[0][3] * hari
                    total_harga = str(harga)

            else:
                mobil = mobil_alphard[0][1]
                plat = mobil_alphard[0][4]
                mobil_alphard.pop(0)
                if durasi == '12' and tipe_sewa == 'Sopir + BBM' or tipe_sewa == 'sopir + bbm':
                    harga = mobil_alphard[0][2]
                    total_harga = str(harga)
                else:
                    harga = mobil_alphard[0][3] * hari
                    total_harga = str(harga)

            f = open("datarent.txt", "a")
            f.write(hari_ini.strftime('%a, %b %d %Y %X') + '\n')
            f.write('Nama           : '+ nama +'\n')
            f.write('No Hp          : '+ no_hp +'\n')
            f.write('Alamat         : '+ alamat +'\n\n')
            f.write('Jenis Mobil    : '+ mobil +'\n')
            f.write('Plat           : '+ plat +'\n')
            f.write('Tipe Sewa      : '+ tipe_sewa +'\n')
            f.write('Durasi         : '+ durasi +'\n')
            if durasi == '24':
                f.write('Hari           : '+ inp_hari +'\n')
            f.write('Harga          : Rp. '+ total_harga +'\n')
            f.write('----------------------------------------'+'\n\n')
            f.close()
            # f = open("datarent.txt", "r")
            
            yakin = input('\nYakin [y/n] > ')
            if yakin == 'y':
                os.system('cls')
                print(Fore.GREEN + 'Pesanan Berhasil' + Style.RESET_ALL)
                print(Fore.GREEN + 'TerimaKasih sudah menyewa di Oregeon Rent Car' + Style.RESET_ALL)

                if durasi == '24':
                    struk2(nama,alamat,armada,durasi,plat,tipe_sewa,inp_hari,harga)
                    kembali()
                else:
                    struk1(nama,alamat,armada,durasi,plat,tipe_sewa,harga)
                    kembali()
            else:
                continue
        except Exception:
            os.system('cls')
            print(Fore.YELLOW + 'Isikan data dengan benar!' + Style.RESET_ALL)
# akhir rent   
        
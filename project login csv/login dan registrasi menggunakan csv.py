import os #memanggil library os
import csv #memanggil library csv
import termcolor #memanggil library termcolor

def clear ():  #membuat fungsi dengan nama clear
    os.system("cls") #clear terminal

def garis (): #membuat fungsi dengan nama garis 
    print ("=" * 50) #mencetak "=" sebanyak 50 kali

def cover (): # membuat  fungsi dengan nama cover
    garis() #memanggil fungsi garis 
    print ("HALAMAN LOGIN".center(50)) #mencetak kalimat halaman login di tengah dari 50 karakter
    garis() #memanggil fungsi garis 

def enter (): #memanggil fungsi enter 
    enter = input ("tekan [ENTER] untuk melanjutkan ") #inputan sebagai pembatas 

def menu (): #membuat fungsi dengan nama menu
    clear() #memanggil fungsi clear
    cover () #memanggil fungsi cover 
    print ("""
                1. REGISTRASI
                2. LOGIN
""") #mencetak registrasi dan login 
    garis() #memanggil fungsi garis
    while True : #perulangan jika kondisi True
        try : #melakukan sebuah percobaan
            pilih = int (input ("Pilih Opsi yang tersrdia >> ")) #inputan opsi yang dipilih 
            if pilih == 1 : #jika inputan user 1 
                enter() #memanggil fungsi enter 
                registrasi() #memanggil fungsi registrasi
                break #menghentikan pengulangan
            elif pilih == 2 : #jika inputan user 2 
                enter() #memanggil fungsi enter
                login () #memanggil fungsi login
                break #menghentikan perulangan 
            else : #input selain 1 dan 2  
                print ("Opsi yang anda pilih tidak tersedia") #mencetak kalimat 
        except ValueError : #apabila terdapat error 
            termcolor.cprint ("masukkan input dalam bentuk angka", "red") #mencetak kalimat dengan warna merah
            enter() #memanggil fungsi enter
            menu () #memanggil fungsi menu 
            

def penampung (): #membuat fungsi dengan nama penampung 
    global datauser, list_password, list_username #menjadikan variabel lokal menjadi global
    datauser = [] #list penampung data user
    list_username = [] #list penampung username user
    list_password = [] #list penampung password
    with open ("datauser.csv", mode = "r") as file : #membuka file csv dengan nama datauser.csv
        csv_reader = csv.reader(file) #method csv untuk membaca file 
        for row in csv_reader:  #perulangan untuk membaca setiap baris pada file csv
            datauser.append(row)  #menambahkan data pada list datauser

    for i in range  (len (datauser)):  #perulangan untuk mengambil data pada list datauser
        list_username.append(datauser[i][2])  #menambahkan data pada list username
        list_password.append (datauser[i][3])   #menambahkan data pada list password
    return datauser, list_username, list_password  #mengembalikan data user, username, dan password

def registrasi (): #membuat fungsi dengan nama registrasi
    clear() # memanggil  fungsi clear
    cover() #memanggil fungsi cover 
    datauser , list_username, list_password = penampung () # mengambil data user, username, dan password dari fungsi penampung 

    while True : # perulangan jika kondisi benar 
        nama = input ("masukkan nama lengkap anda >> ") #input nama user 
        nomorhp = int (input ("masukkan nomor HP >> ")) #input nomor hp user 
        while True : # perulangan jika kondisi benar 
            try : #percobaan terhadap inputan
                username = input ("buat username baru >> ") #inputan username baru yang ingin di buat user 
                if username in list_username: #jika  username sudah ada pada list username 
                    raise ValueError ("Username sudah digunakan") #menandai bahwa erorr
                else : #selain kondisi diatas 
                    break #keluar dari perulangan
            except ValueError as erorr:  #apabila terdapat error
                termcolor.cprint (erorr, "red") #cetak kalimat error dengan warna merah 
        while True : #perulangan jika kondisi benar 
            try : #percobaan terhadap inputan 
                password = input ("buat password baru >> ") #inputan password baru dari user 
                if password == username or len(password) < 8 : #jika pasword sama dengan username atau panjang password kurang dari 8 karakter 
                    raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") #tandai bahwa error
                else : #jika tidak memenuhi
                    break #keluar dari pengulangan 
            except ValueError as error: # apabila terindikasi error
                termcolor.cprint (error, "red") #mencetak error dengan warna merah 

        while True :  #perulangan apabila kondisi terpenuhi
            try : #percobaan terhadap inputan 
                password2 = input ("konfirmasi password anda >> ")  #input konfirmasi password user 
                if password2 != password : #jika konfirmasi password tidak sama dengan password yang dimasukkan 
                    raise  ValueError ("password yang anda masukkan tidak sama") #tandai bahwa error
                else : #jika tidak memenuhi
                    break # keluar dari perulangan 
            except ValueError as error: #apabila ada error
                termcolor.cprint (error, "red") #mencetak error dengan warna merah 

        garis() #memanggil fungsi garis 
        with open ("datauser.csv", mode = "a", newline = "\n") as file : # membuka file csv dengan nama datauser.csv dalam mode menulis 
            border = ["nama lengkap", "nomor hp", "username", "password"] #borderr dari file csv 
            writer = csv.DictWriter (file, fieldnames=border) #method  csv untuk menulis file csv 
            writer.writerow ( {"nama lengkap" : nama, "nomor hp" :  nomorhp, "username" : username, "password" : password2} ) #memasukkan  data user ke dalam file csv 
        termcolor.cprint ("registrasi berhasil, silahkan login", "green") #mencetak  kalimat registrasi berhasil dengan warna hijau 
        enter() #memanggil fungsi enter
        menu() #memanggil fungsi menu 
        
def login (): #membuat fungsi dengan nama login 
    clear () #memanggil fungsi clear
    cover () #memanggil  fungsi cover
    datauser,list_username, list_password = penampung () #mengambil nilai dari fungsi penampung 
    username = input ("masukkan username anda >> ") #inputan username user 
    password = input ("masukkan password anda >> ") #inputan password user 
    a = 0 #penanda
    for i in range (len(datauser)): #perulangan sebagai index
        if username in list_username[i] and password in list_password[i] : #jika username dan password terdapat pada indeks yang sama 
            a += 1 #penanda menjadi 1 
    if a == 1 : #jika penanda 1 
        termcolor.cprint ("login berhasil", "green") #mencetak login berhasil berwarna hijau 
        enter() #memanggil fungsi enter
        main() #memanggil fungsi main
    else : #jika kondisi tidak terpenuhi
        termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") #mencetak login tidak berhasil berwarna merah 
        enter () #memanggil fungsi enter
        login() #memanggil fungsi login 

def main(): #membuat fungsi dengan nama main 
    clear () #memanggil fungsi clear 
    garis() #memanggil fungsi garis 
    print ("halaman utama".center(50)) #mencetak kalimat halaman utama tepat pada tengah 50 karakter 
    garis() #memanggil fungsi garis 
    enter() #memanggil fungsi enter 


if __name__ == "__main__": #pembatas antar fungsi dengan program utama 
    menu() #memanggil fungsi menu sebagai awal program 


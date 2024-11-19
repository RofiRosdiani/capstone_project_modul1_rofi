#Master Data Karyawan
#data_karyawan =[] #In case data karyawan tidak tersedia
data_karyawan = [
    {  
        'NIP' : '101250',
        'Nama Lengkap' : 'Ramadhan Edison',
        'Jenis Kelamin' : 'Laki-laki',
        'Jabatan' : 'Video Editor',
        'Divisi': 'Kreatif',
        'Alamat Rumah': 'Jalan Anggrek, Bekasi Utara',
    },
    {  
        'NIP' : '102350',
        'Nama Lengkap' : 'Naufal Vincenzo',
        'Jenis Kelamin': 'Laki-laki',
        'Jabatan' : 'Akuntan',
        'Divisi': 'Keuangan',
        'Alamat Rumah': 'Jalan Dipenogoro, Jakarta Selatan',
    },
    {  
        'NIP' : '103619',
        'Nama Lengkap' : 'Aurora Carrisa',
        'Jenis Kelamin': 'Perempuan',
        'Jabatan' : 'Copywriter',
        'Divisi': 'Pemasaran',
        'Alamat Rumah': 'Jalan Melon, Depok',
    },   
    {  
        'NIP' : '104415',
        'Nama Lengkap' : 'Devara Agastha',
        'Jenis Kelamin': 'Perempuan',
        'Jabatan' : 'Animator',
        'Divisi': 'Kreatif',
        'Alamat Rumah': 'Jalan Ir. Soekarno, Jakarta Timur',
    },
    {  
        'NIP' : '105376',
        'Nama Lengkap' : 'Freya Ghalisa',
        'Jenis Kelamin': 'Perempuan',
        'Jabatan' : 'Produser',
        'Divisi': 'Produksi',
        'Alamat Rumah': 'Jalan Melati, Bekasi Selatan',
    },
]
    
#Fungsi untuk membuat tampilan data karyawan - Pilihan menu No.1
def tampilan_data_karyawan():        
    if not data_karyawan: #Periksa dan tampilkan notifikasi jika data karyawan kosong
         print('\nMohon maaf, Data tidak tersedia')
         return menu_awal()

    #Tampilkan data karyawan jika tersedia
    print(''' 
----------------------------------------------------------------------------------------------------------------------------  
| No. |  NIP   |     Nama Lengkap    | Jenis Kelamin |    Jabatan     |    Divisi    |             Alamat rumah            |
---------------------------------------------------------------------------------------------------------------------------- ''')
    for nomor, data in enumerate(data_karyawan, start=1): #enumerate() digunakan untuk mendapatkan indeks dan elemen dari data_karyawan sekaligus
        nip_pegawai = data['NIP']
        nama_lengkap = data['Nama Lengkap'].title()
        jenis_kelamin = data['Jenis Kelamin'].title()
        jabatan = data['Jabatan'].title()
        divisi = data['Divisi'].title()
        alamat_rumah = data['Alamat Rumah'].title()
        print(f'|  {nomor:<3}| {nip_pegawai:<4} | {nama_lengkap:<20}| {jenis_kelamin:<13} | {jabatan:<14} | {divisi:<12} | {alamat_rumah:<35} |')
    print('-' * 124) #untuk menghasilkan header bawah tabel

########################################################################################

#Fungsi untuk Konfirmasi 
def konfirmasi():
    while True:
          respon = input('Apakah Anda yakin? Y/T = ').upper()
          if respon in ('Y', 'T'):
               return respon
          else:
               print(f'Data yg Anda masukan {respon} salah. Hanya perlu masukkan Y/T')  
  
#Fungsi untuk kembali ke Menu Utama
def kembali_menu_utama():
     while True:
          kembali_menu = input('\nApakah Anda ingin kembali ke Menu Awal? (Y:Ya / T:Tidak) : ').upper()
          if kembali_menu == 'Y':
               menu_awal()
          elif kembali_menu == 'T':
               print('Program telah selesai. Thank you! Have a nice day :)\n')
               exit()
          else:
               print('Masukkan jawaban yang valid, hanya diperbolehkan input Y atau T.')

########################################################################################

#Fungsi untuk menambahkan data pada field NIP
def nip_karyawan():
    while True:
        input_tambah_nip = input('\nMasukkan NIP Pegawai: ')
        if input_tambah_nip.isdigit() and len(input_tambah_nip) == 6: #Cek apakah data yg diinput berupa angka dan berjumlah 6 angka
            for cek_nip in data_karyawan:
                if any(cek_nip['NIP'] == input_tambah_nip for cek_nip in data_karyawan):
                    print('Data sudah ada. Maaf, data tidak dapat diduplikasi') 
                    break
                else:
                    print('NIP berhasil ditambahkan.')
                    return input_tambah_nip
        elif not input_tambah_nip.strip(): #Cek apakah data yg diinput hanya berupa spasi
            print('Data yang dimasukkan hanya berisi spasi atau kosong.\nSilakan masukkan NIP yang terdiri dari 6 angka')
        elif not (input_tambah_nip.isdigit() or input_tambah_nip.isalpha()): #Cek apakah data yg diinput berupa karakter dan angka
            print('Data yang dimasukkan hanya berisi karakter dan angka.\nSilakan masukkan NIP yang terdiri dari 6 angka')
        elif input_tambah_nip.isalpha(): #Cek apakah data yg diinput hanya berupa karakter
            print('Data yang dimasukkan hanya berisi karakter.\nSilakan masukkan NIP yang terdiri dari 6 angka')
        else:
            print(f'NIP yang Anda masukkan kurang dari 6 digit. Silakan masukkan NIP yang terdiri dari 6 angka')

#Fungsi untuk menambahkan data pada field Nama
def nama_karyawan():
     while True:
          input_tambah_nama = input('\nMasukan Nama Pegawai: ').title()
          if not input_tambah_nama.strip(): #Cek apakah data yg diinput hanya berupa spasi
                print('Data yang dimasukkan salah, hanya berisi spasi atau kosong.\nSilakan masukkan nama pegawai yang sesuai.')    
          elif input_tambah_nama.isdigit(): #Cek apakah data yg diinput berupa angka
                print('Data yang dimasukkan salah karena berisi angka.\nSilakan masukkan nama pegawai yang sesuai.') 
          elif all(i.isalpha() or i.isspace() for i in input_tambah_nama): 
                if len(input_tambah_nama) > 18:
                    print('Data yang dimasukkan melebihi 18 karakter.\nSilakan masukkan nama pegawai yang sesuai dgn ketentuan.')  
                else:  
                    return input_tambah_nama
          elif all(a.isdigit() or a.isalpha() for a in input_tambah_nama):
               print('Data yang dimasukkan salah karena berisi angka dan karakter.\nSilakan masukkan nama pegawai yang sesuai.')
          elif all(a.isdigit() or a.isalpha() or a.isspace() for a in input_tambah_nama):
               print('Data yang dimasukkan salah karena berisi angka, karakter, dan spasi.\nSilakan masukkan nama pegawai yang sesuai.')
          else:
                print('Data yang dimasukkan salah.\nSilakan masukkan nama pegawai yang sesuai.') 
# nama_karyawan()

#Fungsi untuk menambahkan data pada field Jenis Kelamin
def jenis_kelamin():
    while True:
        input_tambah_jenis_kelamin = input(f'\nMasukkan Jenis Kelamin (P/L) = ').title()
        if input_tambah_jenis_kelamin == 'P':
            return 'Perempuan'
        elif input_tambah_jenis_kelamin == 'L':
            return 'Laki-laki'
        else:
            print(f'Input yang Anda masukkan tidak valid.\nSilakan masukkan "P" untuk Perempuan dan "L" untuk Laki-laki')

#Fungsi untuk menambahkan data pada field Jabatan
def jabatan():
    while True:
          input_tambah_jabatan = input(f'\nMasukkan Jabatan Pegawai = ').title()
          if not input_tambah_jabatan.strip(): #Cek apakah data yg diinput hanya berupa spasi
                print('Data yang dimasukkan salah, hanya berisi spasi atau kosong.\nSilakan masukkan jabatan pegawai yang sesuai.')    
          elif input_tambah_jabatan.isdigit(): #Cek apakah data yg diinput berupa angka
                print('Data yang dimasukkan salah karena berisi angka.\nSilakan masukkan jabatan pegawai yang sesuai.') 
          elif all(i.isalpha() or i.isspace() for i in input_tambah_jabatan): 
                if len(input_tambah_jabatan) > 12:
                    print('Data yang dimasukkan melebihi 12 karakter.\nSilakan masukkan jabatan pegawai yang sesuai dgn ketentuan.')  
                else:   
                    return input_tambah_jabatan
          elif all(a.isdigit() or a.isalpha() for a in input_tambah_jabatan):
               print('Data yang dimasukkan salah karena berisi angka dan karakter.\nSilakan masukkan jabatan pegawai yang sesuai.')
          elif all(a.isdigit() or a.isalpha() or a.isspace() for a in input_tambah_jabatan):
               print('Data yang dimasukkan salah karena berisi angka, karakter, dan spasi.\nSilakan masukkan jabatan pegawai yang sesuai.')
          else:
                print('Data yang dimasukkan salah.\nSilakan masukkan jabatan pegawai yang sesuai.') 

#Fungsi untuk menambahkan data pada field Divisi
def divisi():
    while True:
          input_tambah_divisi = input(f'\nMasukkan Divisi Pegawai = ').title()
          if not input_tambah_divisi.strip(): #Cek apakah data yg diinput hanya berupa spasi
                print('Data yang dimasukkan salah, hanya berisi spasi atau kosong.\nSilakan masukkan divisi pegawai yang sesuai.')    
          elif input_tambah_divisi.isdigit(): #Cek apakah data yg diinput berupa angka
                print('Data yang dimasukkan salah karena berisi angka.\nSilakan masukkan divisi pegawai yang sesuai.') 
          elif all(i.isalpha() or i.isspace() for i in input_tambah_divisi): 
                if len(input_tambah_divisi) > 11:
                    print('Data yang dimasukkan melebihi 11 karakter.\nSilakan masukkan divisi pegawai yang sesuai dgn ketentuan.')  
                else:
                    return input_tambah_divisi
          elif all(a.isdigit() or a.isalpha() for a in input_tambah_divisi):
               print('Data yang dimasukkan salah karena berisi angka dan karakter.\nSilakan masukkan divisi pegawai yang sesuai.')
          elif all(a.isdigit() or a.isalpha() or a.isspace() for a in input_tambah_divisi):
               print('Data yang dimasukkan salah karena berisi angka, karakter, dan spasi.\nSilakan masukkan divisi pegawai yang sesuai.')
          else:
                print('Data yang dimasukkan salah.\nSilakan masukkan divisi pegawai yang sesuai.') 

#Fungsi untuk menambahkan data pada field Alamat rumah
def alamat_rumah():
    while True:
          input_tambah_alamat = input(f'\nMasukkan Alamat Rumah Pegawai (Nama Jalan, Kota) = ').title()
          if not input_tambah_alamat.strip(): #Cek apakah data yg diinput hanya berupa spasi
                print('Data yang dimasukkan salah, hanya berisi spasi atau kosong.\nSilakan masukkan alamat rumah pegawai yang sesuai.')    
          elif input_tambah_alamat.isdigit(): #Cek apakah data yg diinput berupa angka
                print('Data yang dimasukkan salah karena berisi angka.\nSilakan masukkan alamat rumah pegawai yang sesuai.') 
          elif all(i.isalpha() or i.isspace() or i.isdigit() or (i == '.', ',') for i in input_tambah_alamat): 
                if len(input_tambah_alamat) >= 33:
                    print('Data yang dimasukkan melebihi 33 karakter.\nSilakan masukkan alamat rumah pegawai yang sesuai dgn ketentuan.')  
                else:
                    return input_tambah_alamat
          else:
                print('Data yang dimasukkan salah.\nSilakan masukkan alamat rumah pegawai yang sesuai.') 

#Fungsi untuk menambahkan data karyawan - Pilihan menu No. 2
def tambah_data_karyawan():
    #Membuat fungsi untuk tiap field dalam data karyawan
    input_tambah_nip = nip_karyawan()
    input_tambah_nama = nama_karyawan()
    input_tambah_jenis_kelamin = jenis_kelamin()
    input_tambah_jabatan = jabatan()
    input_tambah_divisi = divisi()
    input_tambah_alamat = alamat_rumah()

    print(f'''
Anda akan menambahkan data karyawan dengan detail, sbb:
NIP           : {input_tambah_nip}
Nama Lengkap  : {input_tambah_nama}
Jenis Kelamin : {input_tambah_jenis_kelamin}
Jabatan       : {input_tambah_jabatan}
Divisi        : {input_tambah_divisi}
Alamat Rumah  : {input_tambah_alamat}
      ''')
    
    if konfirmasi() == 'Y':
         data_karyawan.append({'NIP' : input_tambah_nip,
                               'Nama Lengkap' : input_tambah_nama,
                               'Jenis Kelamin' : input_tambah_jenis_kelamin,
                               'Jabatan' : input_tambah_jabatan,
                               'Divisi'  : input_tambah_divisi,
                               'Alamat Rumah' : input_tambah_alamat})
         print('Penambahan data karyawan berhasil ditambahkan')
         while True:
            pilihan = input('\nApakah ingin menambah data lainnya? (Y:Ya / T:Tidak) : ').upper()
            if pilihan == 'Y':
                print('Anda kembali pada menu pilihan 4. Menambahkan Data Karyawan')
                tambah_data_karyawan()
            else:
                print('Anda kembali pada menu awal')
                menu_awal()
    
    else:
        print('Penambahan data karyawan dibatalkan')
        while True:
            pilihan = input('\nApakah Anda ingin kembali ke Menu Awal? (Y:Ya / T:Tidak) : ').upper()
            if pilihan == 'T':
                print('Anda kembali pada menu pilihan 4. Menambahkan Data Karyawan')
                tambah_data_karyawan()
            
            return menu_awal()

#########################################################################################

#Fungsi untuk Menu Update Data Pegawai
def menu_ubah_data():
     print('''
------------------------
Menu Update Data Pegawai
------------------------
1. NIP
2. Nama Lengkap
3. Jenis Kelamin
4. Jabatan
5. Divisi
6. Alamat Rumah
0. Kembali ke Menu Awal''')

#Fungsi untuk menanyakan apakah pengguna ingin mengubah data lainnya
def ubah_lagi():
    input_ubah_lagi = input('\nApakah Anda ingin mengubah data lainnya? Y/T: ')
    if input_ubah_lagi.upper() == 'Y':
        ubah_data()  # Memanggil ulang fungsi ubah_data jika ingin mengubah data lainnya
    elif input_ubah_lagi.upper() == 'T':
        print('Update data lainnya dibatalkan. Anda kembali ke Menu Awal.')
        menu_awal()  # Mengembalikan ke menu awal jika tidak ingin mengubah data lainnya
    else:
        print('Input tidak valid. Silakan masukkan Y untuk Ya atau T untuk Tidak.')
        ubah_lagi()  # Memanggil kembali fungsi ini jika input tidak valid

#Fungsi untuk mengubah data karyawan - Pilihan menu No.3
def ubah_data():
    if not data_karyawan: #Periksa dan tampilkan notifikasi jika data karyawan kosong
         print('\nMohon maaf, Data tidak tersedia')
         return menu_awal()

    while True:
        tampilan_data_karyawan()
        input_ubah_data = input('Masukkan NIP pegawai yang ingin Anda ubah: ').strip()
        
        #Cari data pegawai berdasarkan NIP
        for cek_data in data_karyawan:
            input_ubah_data = str(input_ubah_data)
            if cek_data['NIP'].strip() == input_ubah_data:
                print(f'''
Anda akan mengubah data pegawai dengan detail, sbb:
Nama Lengkap  : {cek_data['Nama Lengkap']}
Jenis Kelamin : {cek_data['Jenis Kelamin']}
Jabatan       : {cek_data['Jabatan']}
Divisi        : {cek_data['Divisi']}
Alamat Rumah  : {cek_data['Alamat Rumah']}
''')      
                #Mengubah data pegawai pada field yang dipilih user
                if konfirmasi().upper() == 'Y':
                    menu_ubah_data()

                    while True:
                        inputan_user_ubahdata = input('\nMasukkan data yang ingin diubah (0-6): ')

                        if not inputan_user_ubahdata.isnumeric():
                            print('Data yang Anda masukkan tidak valid. Input harus angka antara 0-6')
                            continue

                        elif inputan_user_ubahdata.isnumeric():
                            inputan_user_ubahdata = int(inputan_user_ubahdata) 
                        
                            if inputan_user_ubahdata >= 0 and inputan_user_ubahdata <=6:
                                if inputan_user_ubahdata == 1:
                                    while True:
                                        cek_data['NIP'] = input('\nMasukkan NIP baru: ').strip()
                                        inputan_ubah_nip = (cek_data['NIP'])
                                        if not inputan_ubah_nip.isdigit():
                                            print('NIP pegawai harus berupa angka, terdiri dari 6 digit.')
                                        elif len(inputan_ubah_nip) != 6:
                                            print('NIP pegawai harus tepat 6 digit. Silakan coba kembali.')
                                        else:
                                            print(f'NIP pegawai berhasil diubah menjadi {cek_data['NIP']}')
                                            break

                                elif inputan_user_ubahdata == 2:
                                    while True:
                                        cek_data['Nama Lengkap'] = input('\nMasukkan Nama Lengkap baru: ').title().strip()
                                        inputan_ubah_nama = cek_data['Nama Lengkap']
                                        if all(a.isalpha() or a.isspace() for a in inputan_ubah_nama) and len(inputan_ubah_nama) <= 18:
                                            print(f'Nama Lengkap pegawai berhasil diubah menjadi {cek_data['Nama Lengkap']}')
                                            break
                                        elif all(a.isalpha() or a.isspace() for a in inputan_ubah_nama) and len(inputan_ubah_nama) > 18:
                                            print('Data yang Anda masukkan melebihi 18 karakter. Silakan coba kembali')
                                        elif all(a.isdigit() or a.isspace() or a.isalpha() for a in inputan_ubah_nama) :
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')
                                        else:
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')
                                        
                                elif inputan_user_ubahdata == 3:
                                    while True:
                                        cek_data['Jenis Kelamin'] = input('\nMasukkan Jenis Kelamin baru (P/L) : ').upper()
                                        inputan_ubah_jeniskelamin = cek_data['Jenis Kelamin']
                                        if inputan_ubah_jeniskelamin == 'P':
                                            print('Jenis Kelamin pegawai berhasil diubah menjadi Perempuan')
                                            cek_data['Jenis Kelamin'] = 'Perempuan'
                                            ubah_lagi()
                                        
                                        elif inputan_ubah_jeniskelamin == 'L':
                                            print('Jenis Kelamin pegawai berhasil diubah menjadi Laki-laki')
                                            cek_data['Jenis Kelamin'] = 'Laki-laki'
                                            ubah_lagi()

                                        else:
                                            print(f'Input yang Anda masukkan tidak valid.\nSilakan masukkan "P" untuk Perempuan dan "L" untuk Laki-laki')

                                elif inputan_user_ubahdata == 4:
                                    while True:
                                        cek_data['Jabatan'] = input('\nMasukkan Jabatan baru: ').title().strip()
                                        inputan_ubah_jabatan = cek_data['Jabatan']
                                        if inputan_ubah_jabatan.isalpha() and len(inputan_ubah_jabatan) <= 12:
                                            print(f'Jabatan pegawai berhasil diubah menjadi {cek_data['Jabatan']}')
                                            break
                                        elif inputan_ubah_jabatan.isalpha() and len(inputan_ubah_jabatan) > 12:
                                            print('Data yang Anda masukkan melebihi 12 karakter. Silakan coba kembali')
                                        elif all(a.isdigit() or a.isspace() or a.isalpha() for a in inputan_ubah_jabatan) :
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')
                                        else:
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')

                                elif inputan_user_ubahdata == 5:
                                    while True:
                                        cek_data['Divisi'] = input('\nMasukkan Divisi baru: ').title().strip()
                                        inputan_ubah_divisi = cek_data['Divisi']
                                        if inputan_ubah_divisi.isalpha() and len(inputan_ubah_divisi) <= 11:
                                            print(f'Divisi pegawai berhasil diubah menjadi {cek_data['Divisi']}')
                                            break
                                        elif inputan_ubah_divisi.isalpha() and len(inputan_ubah_divisi) > 11:
                                            print('Data yang Anda masukkan melebihi 11 karakter. Silakan coba kembali')
                                        elif all(a.isdigit() or a.isspace() or a.isalpha() for a in inputan_ubah_divisi) :
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')
                                        else:
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')

                                elif inputan_user_ubahdata == 6:
                                    while True:
                                        cek_data['Alamat Rumah'] = input('\nMasukkan Alamat Rumah baru: ').title().strip()
                                        inputan_ubah_alamat = cek_data['Alamat Rumah']
                                        if all(a.isalpha() or a.isspace() for a in inputan_ubah_alamat)  and len(inputan_ubah_alamat) <= 33:
                                            print(f'Alamat rumah pegawai berhasil diubah menjadi {cek_data['Alamat Rumah']}')
                                            break
                                        elif all(a.isalpha() or a.isspace() for a in inputan_ubah_alamat)  and len(inputan_ubah_alamat) > 33:
                                            print('Data yang Anda masukkan melebihi 33 karakter. Silakan coba kembali')
                                        elif all(a.isdigit() or a.isspace() or a.isalpha() for a in inputan_ubah_alamat ) :
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')
                                        else:
                                            print('Data yang Anda masukkan tidak valid. Silakan coba kembali.')
                                
                                elif inputan_user_ubahdata == 0:
                                    print('Anda kembali ke Menu Awal')
                                    menu_awal()

                                break
                            
                            else:
                                print('Data yang Anda masukkan tidak valid. Input harus angka antara 0-6')
                                continue                        
               
                    #Menjalankan fungsi untuk memastikan user ingin mengubah data lagi atau tidak
                    ubah_lagi()  
                    return
                    
                else:
                     print('Perubahan dibatalkan. Anda akan kembali ke Menu Awal')
                     return menu_awal()
                              
        else:
            print('NIP pegawai tidak ditemukan.')
            while True:
                pilihan = input('\nApakah Anda ingin kembali ke Menu Awal? (Y:Ya / T:Tidak) : ').upper()
                if pilihan == 'T':
                    print('Anda kembali pada menu pilihan 3. Mengubah Data Karyawan')
                    return ubah_data()
                
                else:
                    return menu_awal()

#########################################################################################

#Fungsi untuk menanyakan apakah pengguna ingin menghapus data lainnya
def hapus_lagi():
    input_hapus_lagi = input('\nApakah Anda ingin menghapus data lainnya? Y/T: ')

    if input_hapus_lagi.upper() == 'Y':
       hapus_data()  # Memanggil ulang fungsi hapus_data jika ingin menghapus data lainnya

    elif input_hapus_lagi.upper() == 'T':
        print('Hapus data lainnya dibatalkan. Anda kembali ke Menu Awal.')
        menu_awal()  # Mengembalikan ke menu awal jika tidak ingin mengubah data lainnya

    else:
        print('Input tidak valid. Silakan masukkan Y untuk Ya atau T untuk Tidak.')
        hapus_lagi()  # Memanggil kembali fungsi ini jika input tidak valid

#Fungsi untuk menghapus data karyawan - Pilihan menu No.4
def hapus_data():
    if not data_karyawan: #Periksa dan tampilkan notifikasi jika data karyawan kosong
         print('\nMohon maaf, Data tidak tersedia')
         menu_awal()

    while True:
        tampilan_data_karyawan()
        input_hapus_data = input('Masukkan NIP pegawai yang ingin Anda hapus: ').strip()

        #Cari data berdasarkan NIP
        for cek_data2 in data_karyawan:
            input_hapus_data = str(input_hapus_data)
            if cek_data2['NIP'].strip() == input_hapus_data:
                print(f'''
Anda akan menghapus data pegawai dengan detail, sbb:
Nama Lengkap  : {cek_data2['Nama Lengkap']}
Jenis Kelamin : {cek_data2['Jenis Kelamin']}
Jabatan       : {cek_data2['Jabatan']}
Divisi        : {cek_data2['Divisi']}
Alamat Rumah  : {cek_data2['Alamat Rumah']}
''')      
                #Mengubah data pegawai pada field yang dipilih user
                if konfirmasi().upper() == 'Y':
                    data_karyawan.remove(cek_data2)
                    print(f'Data pegawai dengan NIP {input_hapus_data} berhasil dihapus.')
                    kembali_menu_utama()

                else:
                     print(f'Delete data pegawai dengan NIP {input_hapus_data} dibatalkan')
    
                    #Menjalankan fungsi untuk memastikan user ingin mengubah data lagi atau tidak
                     hapus_lagi()  

        else:
            print('Maaf, NIP tidak temukan')
            while True:
                pilihan2 = input('\nApakah Anda ingin kembali ke Menu Awal? (Y:Ya / T:Tidak) : ').upper()
                if pilihan2 == 'T':
                    print('Anda kembali pada menu pilihan 4. Menghapus Data Karyawan')
                    return hapus_data()
                
                return menu_awal()

#########################################################################################

#Fungsi untuk user menginput data pada menu awal
def inputan_user():      
    while True:
        inputan_user = input('\nSilakan pilih menu diatas (1-5): ')
        if inputan_user.isnumeric():
            inputan_user = int(inputan_user) 

            if inputan_user >= 1 and inputan_user <=5:
                if inputan_user == 1:
                    print(f'\nAnda memilih Pilihan 1. Daftar Karyawan')
                    print('*' * 39, end=' ')
                    tampilan_data_karyawan()
                    kembali_menu_utama()

                elif inputan_user == 2:
                     print(f'\nAnda memilih Pilihan 2. Menambahkan Data Karyawan')
                     print('*' * 49, end=' ')
                     tambah_data_karyawan()
                     kembali_menu_utama()

                elif inputan_user == 3:
                     print(f'\nAnda memilih Pilihan 3. Mengubah Data Karyawan')
                     print('*' * 46, end=' ')
                     ubah_data()

                elif inputan_user == 4:
                     print(f'\nAnda memilih Pilihan 4. Menghapus Data Karyawan')
                     print('*' * 47, end=' ')
                     hapus_data()

                elif inputan_user == 5:
                     print(f'Terima kasih. Sampai berjumpa kembali!\n')
                     exit()
            else:
                print(f'Data yang Anda masukkan salah. Pilihan harus angka antara 1-5')
                kembali_menu_utama
                menu_awal()
        else:        
            print(f'Data yang Anda masukkan salah. Pilihan harus angka antara 1-5')
            continue

#Fungsi untuk membuat Menu Utama
def menu_awal():
    print('''
------------------------------
ROFI Entertainment Corporation
------------------------------
        
Pilihan menu:
1. Daftar Karyawan 
2. Menambahkan Data Karyawan
3. Mengubah Data Karyawan
4. Menghapus Data Karyawan
5. Exit''')
    
    inputan_user()

##Menjalankan program saat pertama kali digunakan
menu_awal()
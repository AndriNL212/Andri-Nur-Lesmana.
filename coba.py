pilihan="ya"
while pilihan=="ya":
    print('''
    ===================================
             Serba 5 ribu
    Dapat Diskon Jika Membeli Pada Hari:
    kamis = 10 %
    selasa = 25 %
    ===================================''')
    def total(harga,jumlah):
        return(harga*jumlah) 
    print ("1. gayung")
    print ("2. ember")
    print ("3. sapu")
    print ("4. gelas")
    menu  = int(input("pilih barang yang diinginkan: "))

    if    menu == 1 :
          print("gayung 5000")
          menu = 5000
    elif  menu == 2 :
          print ("ember 2000")
          menu = 2000
    elif  menu == 3 : 
          print ("sapu 10000")
          menu = 10000
    elif  menu == 4 :
          print ("gelas 8000")
          menu == 8000        
    
    Jumlah = int(input("masukan jumlah barang yang dibeli: "))
    Total = menu*Jumlah 
    Hari = input('masukan hari pembelian: ')

    if    Hari == 'senin':
          Total=int(Total-0.01*Total)
          print('-Diskon 10 %-')
    elif  Hari == 'jumat':
          Total=int(Total-0.025*Total)
          print('-Diskon 25 %-')
    else:
          print('Maaf,tidak dapat diskon')
    
    print("Total Harga = ", "Rp.",Total)
    Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
    Kembalian= (Bayar-Total)
    print("Uang Kembalian = ", "Rp.",Kembalian)
    pilihan=input("Apakah anda ingin Membeli lagi Ya/Tidak= ")
pilihan="tidak"
print("Terima Kasih Telah berbelanja di toko serba 5 ribu")

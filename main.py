#konversi mata uang
def konversi_mata_uang():
    IDR = int(input("Masukkan Nominal : "))
    USD = float(IDR/14100.70)
    SGD = float(IDR/10505.02)
    EUR = float(IDR/16435.71)
    JPY = float(IDR/123.30)
    print ("1.mata uang USD",USD)
    print ("2.mata uang SGD",SGD)
    print ("3.mata uang EUR",EUR)
    print ("4.mata uang JPY",JPY)   

konversi_mata_uang()
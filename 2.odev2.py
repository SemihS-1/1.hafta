sayi = int(input("değer giriniz:"))
toplam = 0

for i in range(1,sayi + 1):
    print(i)    
    toplam += i
print("Toplam: ",toplam)
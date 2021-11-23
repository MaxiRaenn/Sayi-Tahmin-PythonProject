#BarkınEgeDilek
from random import randint

sayi1 = randint(0,250)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("0 ile 250 arasında değer girin: "))
    if sayi < sayi1:
        print("Daha Yüksek Bir Sayı Giriniz")
        continue
    elif sayi > sayi1:
        print("Daha Düşük Bir Sayı Giriniz")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))

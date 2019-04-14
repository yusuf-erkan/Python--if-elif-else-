yas=int(input("Yaşınızı girin: "))
if yas>0 and yas<100:
    if yas<50:
        print("Yaşınız 50'den küçüktür.")
    elif yas>50:
        print("Yaşınız 50'den büyüktür.")
else:
    print("Lütfen 0 ile 100 arasında değer girin")

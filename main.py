import random
sifreuzunlugu = int(input("Şifre uzunluğunu giriniz: "))
rakamsayisi = int(input("En az kaç rakam olsun: "))
kucukh = int(input("Kaç küçük harf olsun: "))
buyukh = int(input("Kaç büyük harf olsun: "))
toplam= rakamsayisi + kucukh + buyukh

#uzunluk = sifreuzunlugu * "_"

bharfler = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
kharfler = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
rakam = ("0","1","2","3","4","5","6","7","8","9",)
sekiller = ("!","#","+","%","&","/","*",".")
sifreo = []


if sifreuzunlugu < toplam :
    print("Bunu yapamayız şifre uzunluğu {} ya da daha az olmak zorunda. ".format(sifreuzunlugu))
if sifreuzunlugu == toplam:
    for i in range(rakamsayisi):
        sifreo.append(random.choice(rakam))


    for x in range(kucukh):
        sifreo.append(random.choice(kharfler))


    for y in range(buyukh):
        sifreo.append((random.choice(bharfler)))
    random.shuffle(sifreo)
    print("Şifreniz budur:")
    print(*sifreo, sep="")


if sifreuzunlugu > toplam:
    eksi = sifreuzunlugu - toplam
    for i in range(rakamsayisi):
        sifreo.append(random.choice(rakam))


    for x in range(kucukh):
        sifreo.append(random.choice(kharfler))


    for y in range(buyukh):
        sifreo.append((random.choice(bharfler)))

    for u in range(eksi):
        sifreo.append((random.choice(sekiller)))
    random.shuffle(sifreo)
    print("Şifreniz budur:")
    print(*sifreo,sep="")




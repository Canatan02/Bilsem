#kullanıcıdan negatif bir sayı girmesini isteyin pozitif sayı girdikçe tekrar negatif sayı isteyin negatif sayı girene kadar bu devam etsin

sayi= int(input("Bir Negatif Sayı Giriniz:"))
while sayi<0:
    sayi= int(input("Bir Negatif Sayı Giriniz:"))

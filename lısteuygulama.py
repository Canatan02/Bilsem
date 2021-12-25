#kullanıcıdan 10 tane isim isteyerek bunu bir listeye atayan kod

liste=[]
for i in range(10):
    isim=input("İsim:")
    liste.append(isim)
print(liste)

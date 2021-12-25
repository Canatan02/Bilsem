#kullanıcıan 5 tane isim alarak kullanıcıya sorup z den a ya veya a dan z ye sıralayınız

liste=[]
for i in range(5):
    a=input("İsim:")
    liste.append(a)
b=input("A dan Z ye mı Z den A ya mı Sıralayalım:").upper()
if b=="A-Z":
    liste.sort()
    print(liste)
else:
    liste.sort(reverse=True)
    print(liste)




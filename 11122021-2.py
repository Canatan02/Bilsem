#kulanıcıdan 10 tane sayı alarak en büyük hariç hepsini listeye ekleyen kodu yaz

liste=[]
for i in range(10):
    a=int(input("Sayı Giriniz:"))
    liste.append(a)
liste.sort(reverse=False)
liste.pop()
print(liste)


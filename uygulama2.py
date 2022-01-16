#kullanıcıya adını ve kaç kere yazılması gerektiğini sorarak bir text dosyasına yazdırınız

dosya=open("İsim.txt","w",encoding="utf-8")
a=input("İsminiz:")
b=int(input("İsminiz Kaç Kere Yazılsın:"))
for i in range(b):
    dosya.write(a+ "\n")
dosya.close()



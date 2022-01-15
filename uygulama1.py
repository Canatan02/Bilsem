#0 dan 1000 e kadar sayıları text dosyasına yazdırınız

dosya=open("sayılar.txt","w",encoding="utf-8")
for i in range(1000):
    dosya.write(str(i)+"\n")
dosya.close()
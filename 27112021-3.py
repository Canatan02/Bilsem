#break komutu ile while döngüsünden çıkılır continue komutu ile 1 kerelik pas geçilir for döngüsünde de kullanılır
#1 den 100 e kadar 13 hariç tüm sayıları ekrana yazdırınız

for i in range(1,100):
    if i==13:
        continue
    else:
        print(i)

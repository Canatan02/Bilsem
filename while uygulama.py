#kullanıcı adı admin şifre 123456 girilince sisteme başarılı giriş yazsın kullanıcı adı veya şifre hatalı birşey girildiğinde
#ekrana kullanıcı adı veya şifre hatalı yazsın sisteme giriş yapana kadar kullanıcı adı ve şifre tekrar tekrar sorsun
#Sonsuz kere soracak
#doğru bilince break yapacak
#doğru,yanlışı if ile sorgulayacam
#break sonrası while bitiminden devam edecek
#sisteme girildi yapacak

while True:
    a=input("Kullanıcı Adı:").lower()
    b=input("Şifre:")
    if a=="admin" and b=="123456":
        print("Başarılı Giriş")
        break
    else:
        print("Kullanıcı Adı Veya Şifre Yanlış")





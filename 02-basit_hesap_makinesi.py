# Kullanıcıdan iki sayı ve işlem türü alarak toplama, çıkarma, çarpma veya bölme işlemleri yapar.

# Kullanıcıdan ilk sayıyı al
ilkSayi = int(input("İlk Sayıyı Giriniz "))

# kullabnıcıdan ikinci sayıyı al
ikinciSayi = int(input("İkinci Sayıyı Giriniz "))

# Kullanıcıdan yapılacak işlemi seçmesini iste
islem = input(""" Yapmak istediginiz işlemi giriniz 
              (Toplama: + ,  Cıkarma: - , Carpma: * , Bolme: /) """)

# İşlem türüne göre sonuç hesapla
if islem == "+" : # toplama işlemi
    print("Sonuç: " + str(ilkSayi + ikinciSayi))
    
elif islem == "-" : # cıkarma işlemi
    print("Sonuç: " + str(ilkSayi - ikinciSayi))
    
elif islem == "*" : # carpma işlemi
   print("Sonuç: " + str(ilkSayi * ikinciSayi))

elif islem == "/" : # bolme işlemi
     # Bölme işlemi, sıfıra bölme kontrolü yapılır
    if ikinciSayi != 0: 
       print("Sonuç: " + str(ilkSayi / ikinciSayi))
    else:
        print("Hata : Sıfıra bolme yapılmaz")
else:
     # Geçersiz işlem     
    print("Geçersiz işlem seçtiniz. Lütfen +, -, *, / seçeneklerinden birini girin.")   
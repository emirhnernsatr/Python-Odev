# Girilen bir sayının asal olup olmadığını kontrol eden program

# Kullanıcıdan sayı al
sayı = int(input("Bir sayı giriniz: "))

# Asal olup olmadığını kontrol etmek için başlangıç durumu
asalMıdır = True  # Sayı başlangıçta asal kabul edilir

# Özel durum: 1 ve negatif sayılar asal değildir
if sayı <= 1:
    asalMıdır = False
else:
    # 2'den başlayarak, sayının kareköküne kadar olan tüm sayıları kontrol et
    for i in range(2, int(sayı ** 0.5) + 1):
        if sayı % i == 0:  # Eğer sayı herhangi bir sayıya tam bölünüyorsa
            asalMıdır = False  # Asal değildir
            break  # Daha fazla kontrol yapmaya gerek yok, döngüden çık

# Sonucu ekrana yazdır
if asalMıdır:
    print(f"{sayı} bir asal sayıdır.")
else:
    print(f"{sayı} bir asal sayı değildir.")

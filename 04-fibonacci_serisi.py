# Fibonacci serisini hesaplayarak 100'e kadar olan sayıları ekrana yazdırır.

# Fibonacci serisi için başlangıç değerleri
fibonacciSerisi = [0, 1]  # İlk iki Fibonacci sayısı

# Fibonacci serisini 100'e kadar hesapla
while True:
    # Bir sonraki Fibonacci sayısını hesapla
    sonraki_sayi = fibonacciSerisi[-1] + fibonacciSerisi[-2]
    
    # Eğer hesaplanan sayı 100'ü geçerse, döngüyü sonlandır
    if sonraki_sayi > 100:
        break
    
    # Hesaplanan sayıyı seriye ekle
    fibonacciSerisi.append(sonraki_sayi)

# Seriyi ekrana yazdır
print("100'e kadar Fibonacci Serisi:")
print(fibonacciSerisi)

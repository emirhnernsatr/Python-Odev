# 20 öğrencinin sınav notlarını alarak ortalama hesaplayan program

# Öğrenci notlarını tutmak için boş bir liste oluşturulur
notlar = []

print("20 öğrencinin sınav notlarını giriniz (0 ile 100 arasında olmalıdır):")

# Kullanıcıdan 20 öğrencinin notlarını al
for i in range(20):
    while True:  # Geçerli bir not alana kadar döngü devam eder
      try:
        girilenNot = int(input(f"{i+1}. öğrencinin notunu girin: "))  # Her bir not tam sayı olmak zorunda 
        if 0 <= girilenNot <= 100:
            notlar.append(girilenNot)  # Notu listeye ekle
            break # Gecerli not aldıgında donguden çık
        else:
            print("Lütfen 0 ile 100 arasında bir değer girin!")
      except ValueError:  
           print("Geçerli bir sayı giriniz!")  # Sayı dışında bir giriş yapılırsa uyarı ver
# Notların toplamını hesapla
toplam = sum(notlar)

# Notların ortalamasını hesapla
ortalama = toplam / len(notlar)

# Sonucu ekrana yazdır
print("\nSınıf Not Ortalaması:")
print(f"Toplam Not: {toplam}")
print(f"Ortalama: {ortalama}")

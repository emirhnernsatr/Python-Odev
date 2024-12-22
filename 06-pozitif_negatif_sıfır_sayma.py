# Kullanıcıdan 10 adet sayı alarak pozitif, negatif ve sıfırları sayar

# Kullanıcıdan sayı listesi almak için boş bir liste oluşturulur
sayılar = []

print("10 adet sayı giriniz:")

# Kullanıcıdan 10 adet sayı al
for i in range(10):
    sayı = int(input(f"{i+1}. sayıyı girin: "))  # Her bir sayıyı tamsayı olarak al
    sayılar.append(sayı)  # Sayıyı listeye ekle

# Pozitif, negatif ve sıfır sayısını takip eden sayaçlar
pozitif_sayac = 0
negatif_sayac = 0
sıfır_sayac = 0

# Listeyi dolaşarak her sayıyı kontrol et
for sayı in sayılar:
    if sayı > 0:
        pozitif_sayac += 1  # Sayı pozitifse, pozitif sayacı artır
    elif sayı < 0:
        negatif_sayac += 1  # Sayı negatifse, negatif sayacı artır
    else:
        sıfır_sayac += 1  # Sayı sıfırsa, sıfır sayacı artır

# Sonuçları ekrana yazdır
print("\nSonuçlar:")
print(f"Pozitif sayı adedi: {pozitif_sayac}")
print(f"Negatif sayı adedi: {negatif_sayac}")
print(f"Sıfır adedi: {sıfır_sayac}")


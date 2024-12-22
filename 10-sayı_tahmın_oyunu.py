import random  # random modülünü dahil ediyoruz, bu bilgisayarın rastgele sayı tutmasını sağlar

# Bilgisayarın tutacağı sayıyı belirle (1 ile 100 arasında)
bilgiayarNumarasi = random.randint(1, 100)

# Tahmin sayısını sıfırlıyoruz
tahminSayisi = 0

print("1 ile 100 arasında bir sayı tuttum. Tahmin etmeye başlayın!")

# Kullanıcının doğru tahmini yapana kadar döngü çalışacak
while True:
    # Kullanıcıdan tahmin al
    kullaniciTahmini = int(input("Tahmininizi girin: "))

    # Tahmin sayısını artır
    tahminSayisi += 1

    # Kullanıcının tahmini ile bilgisayarın tuttuğu sayıyı karşılaştır
    if kullaniciTahmini < bilgiayarNumarasi:
        print("Daha yüksek bir sayı söyleyin!")  # Tahmin düşükse kullanıcıya daha yüksek söylemesi söylenir
    elif kullaniciTahmini > bilgiayarNumarasi:
        print("Daha düşük bir sayı söyleyin!")  # Tahmin yüksekse kullanıcıya daha düşük söylemesi söylenir
    else:
        print(f"Tebrikler! {bilgiayarNumarasi} sayısını {tahminSayisi} denemede doğru tahmin ettiniz.")
        break  # Kullanıcı doğru tahmin ettiğinde döngü sonlanır

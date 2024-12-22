# Kullanıcıdan sıcaklık değeri ve birim bilgisi alınır
# Celsius'tan Fahrenheit'e veya Fahrenheit'ten Celsius'a dönüşüm yapılır

# Giriş sıcaklığını ve birimini al

sıcaklıkDonusturucu = float(input("Dönüştürülecek sıcaklık değerini girin: "))

sıcaklıkBirimi = input("Sıcaklığın birimini girin (C veya F): ").strip().upper()

# Kullanıcıdan alınan birime göre dönüşüm yap
if sıcaklıkBirimi == "C":
    # Celsius'tan Fahrenheit'e dönüştür
    donusturucu = (sıcaklıkDonusturucu * 9/5) + 32
    print(f"{sıcaklıkDonusturucu} °C, {donusturucu} °F'ye eşittir.")
elif sıcaklıkBirimi == "F":
    # Fahrenheit'ten Celsius'a dönüştür
    donusturucu = (sıcaklıkDonusturucu - 32) * 5/9
    print(f"{sıcaklıkDonusturucu} °F, {donusturucu} °C'ye eşittir.")
else:
    # Geçersiz birim hatası
    print("Geçersiz birim girdiniz. Lütfen sadece 'C' veya 'F' giriniz.")

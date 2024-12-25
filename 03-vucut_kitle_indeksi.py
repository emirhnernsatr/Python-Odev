# Kullanıcıdan boy (metre cinsinden) ve kilo (kilogram cinsinden) bilgisi alarak BMI hesaplayan program

# Kullanıcıdan boy bilgisini al (metre cinsinden)
boy = float(input("Boyunuzu metre cinsinden girin (örneğin 1.75): "))

# Kullanıcıdan kilo bilgisini al (kilogram cinsinden)
kilo = float(input("Kilonuzu kilogram cinsinden girin (örneğin 70): "))

# BMI hesaplama formülü: kilo / (boy * boy)
bmi = kilo/ (boy ** 2)

# BMI değerini ekrana yazdır
print(f"Vücut Kitle İndeksiniz (BMI): {bmi:.2f}")

# BMI'yi değerlendir ve durumu belirle
if bmi < 18.5:
    print("Sonuç: Zayıf")
elif 18.5 <= bmi < 24.9:
    print("Sonuç: Normal kilolu")
elif 25 <= bmi < 29.9:
    print("Sonuç: Fazla kilolu")
else:
    print("Sonuç: Obez")
    
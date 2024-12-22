# Girilen 5 farklı sayının basamaklarının toplamını hesaplayan program

# Kullanıcıdan 5 farklı sayı almak için boş bir liste oluşturulur
sayılar = []

print("5 farklı sayı giriniz:")

# Kullanıcıdan 5 sayı al
for i in range(5):
    sayı = int(input(f"{i+1}. sayıyı girin: "))  # Her bir sayıyı tamsayı olarak al
    sayılar.append(sayı)  # Sayıyı listeye ekle

# Basamak toplamlarını hesaplamak için bir döngü başlat
for idx, sayı in enumerate(sayılar):
    # Sayının basamaklarının toplamını bul
    rakam_sum = sum(int(rakam) for rakam in str(abs(sayı)))  # Sayıyı pozitif yap, her basamağı topla
    print(f"{idx+1}. sayı: {sayı}, Basamak toplamı: {rakam_sum}")

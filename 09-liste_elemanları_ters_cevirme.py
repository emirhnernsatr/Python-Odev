# Kullanıcıdan bir liste alarak elemanlarını tersine çeviren program

# Kullanıcıdan liste elemanlarını al
kullanıcıGirdisi = input("Liste elemanlarını aralarına boşluk koyarak girin: ")

# Girilen veriyi liste haline getirmek için 'split' fonksiyonu kullanılır
# Bu, boşluklarla ayrılmış bir dizeyi listeye dönüştürür
liste = kullanıcıGirdisi.split()

# Listeyi tersine çevirmek için 'reverse' metodu kullanılır
liste.reverse()

# Sonuç olarak ters çevrilmiş listeyi ekrana yazdır
print("Ters çevrilmiş liste:", liste)

from itertools import permutations

# Kullanıcıdan bir girdi alın
girdi = input("karakterleri giriniz : ")

# Girdinin tüm olası sıralamalarını bir liste içinde saklayın
tum_siralamalar = [''.join(siralama) for siralama in permutations(girdi)]

# Tüm sıralamaları ekrana yazdırın
for siralama in tum_siralamalar:
    print(siralama)

# Şifreleri bir dosyaya yazdırın
with open("olusturulan_sifre.txt", "w") as dosya:
    for şifre in tum_siralamalar:
        dosya.write(şifre + "\n")
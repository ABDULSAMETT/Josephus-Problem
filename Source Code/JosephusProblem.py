#-------------------------------------------------------------------------------
# Name:        Josephus Algorithm (Josephus Problemi)
# Purpose:     Çemberde belirli kurallara göre yapılan elemeler sonucunda
#              hayatta kalan son kişiyi bulmak için kullanılan algoritma.
#
# Author:      Abdul Samet
#
# Created:     12/09/2025  
# Copyright:   (c) Abdul Samet 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def joseph(n, k):
    """
    Josephus problemi için özyinelemeli (recursive) çözüm.
    
    Parametreler:
    n: Başlangıçtaki kişi sayısı.
    k: Her turda kaçıncı kişinin eleneceği.
    
    Dönüş değeri:
    Hayatta kalan kişinin sıfır tabanlı indeksi.
    """
    if n == 1:
        return 0  # Tek kişi kaldığında indeks 0 olur.

    # Özyinelemeli olarak bir önceki turun kazananını bul ve güncelle
    return (joseph(n - 1, k) + k) % n

# Kullanıcıdan giriş al
n = int(input("Çemberdeki kişi sayısını giriniz: "))
k = int(input("Kaçıncı kişi elensin: "))

# Josephus fonksiyonundan dönen indeks sıfır tabanlı olduğu için +1 ekliyoruz.
hayatta_kalan = joseph(n, k) + 1

# Sonucu ekrana yazdır
print(f"{n} kişinin arasından hayatta kalan kişi: {hayatta_kalan}")

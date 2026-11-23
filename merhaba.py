from datetime import date  # Bugünün yılını öğrenebilmek için date aracını içe aktarır.

name = input("Adınızı girin: ")  # Kullanıcıdan adını alır ve name değişkenine kaydeder.
birth_year = int(input("Doğum yılınızı girin: "))  # Doğum yılını metin olarak alır ve tam sayıya dönüştürür.
current_year = date.today().year  # Bugünün tarihinden içinde bulunduğumuz yılı alır.

if birth_year > current_year:
    print("Hatalı doğum yılı girdiniz. Lütfen geçerli bir yıl girin.")
else:
    age = current_year - birth_year
    print(f"Merhaba {name}, {age} yaşındasın!")
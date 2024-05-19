meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEES" : "sedikit tidak kesetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO" : "untuk menjadi agresif/marah"
            "NOOB" : "Orang orang yang tidak bagus/termpil dalam bermain suatu game/aktivitas"
            
            }
            
for i in range(5);
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    word = word.upper()
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("tidak ada di dict")

name_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya layıkıyla çok gülmek",
    "SLEEPY": "Uykulu",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}
word = input("Aradığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in name_dict.keys():
    print("{word}: {name_dict[word]}")
else:
    print("Bu kelime sözlükte bulunamadı!")

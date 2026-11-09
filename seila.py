meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online",
    "SLK": "geralmente usado quando se assusta,abreviação de se é louco ",
    "VLW": "abreviação da palavra valeu",
    "PPRT": "abreviação da palavra papo reto"
}

word = input("Digite uma palavra moderna que você não entende(escreva toda a palavra em letras maiúsculas):")

if word in meme_dict.keys():
    
    print(word + ": " + meme_dict[word])
    
else:
    
    print("Essa palavra ainda não está no dicionário.")

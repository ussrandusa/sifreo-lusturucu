while True:
    import random

    karakterler ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sayi = int(input("Şifreniz kaç karakter olsun?"))
    sifre = ""
    for i in range(sayi):
        sifre+=random.choice(karakterler)

    print(sifre*2)

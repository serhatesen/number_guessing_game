import random
import time

print("*************************")
print("1 - 40 arası sayı Tahmini yap")
print("*************************")

sys_numb = random.randint(1, 40)
guessing_right = 7

while guessing_right > 0:
    user_numb = input("Tahmininiz: ")

    if not user_numb.isdigit():
        print("Harf veya özel işaretler kullanılmaz. Sadece sayı giriniz.")
        continue

    user_numb = int(user_numb)
    guessing_right -= 1

    if sys_numb == user_numb:
        print("Tebrikler! Sayıyı buldunuz:", user_numb)
        break
    elif sys_numb > user_numb:
        print("Lütfen sayınızı büyütün..")
    else:
        print("Lütfen sayıyı küçültün..")

    if guessing_right == 1:
        print("Son hakkınız kaldı.")
    elif guessing_right == 0:
        print("Tahmin hakkınız bitti.")
    else:
        print("Bilgiler Sorgulanıyor.. Tahmin hakkınız:", guessing_right)

    time.sleep(2)

if guessing_right == 0:
    print("Sayıyı bulamadınız. Doğru sayı:", sys_numb)
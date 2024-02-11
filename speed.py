import time
import random


cumleler = [
    "Merhaba, bu bir hızlı yazma testidir.",
    "Python ile programlama çok eğlencelidir.",
    "Günün sonunda, en önemli şey sağlığımızdır.",
    "Kendini geliştirmek için her gün biraz kod yaz.",
    "Hayat kısa, kuşlar uçuyor."
]

def yazma_testi():

    secilen_cumle = random.choice(cumleler)
    print("Aşağıdaki cümleyi mümkün olduğunca hızlı ve doğru bir şekilde yazın:")
    print(secilen_cumle)
    

    input("Hazırsanız 'enter' tuşuna basın...")
    
 
    baslangic = time.time()
    

    giris = input()
    

    bitis = time.time()
    
 
    sure = round(bitis - baslangic, 2)
    

    dogru_harf_sayisi = sum(1 for girilen_harf, dogru_harf in zip(giris, secilen_cumle) if girilen_harf == dogru_harf)
    dogruluk_orani = round((dogru_harf_sayisi / len(secilen_cumle)) * 100, 2)
    

    print(f"Yazma süreniz: {sure} saniye")
    print(f"Doğruluk oranınız: {dogruluk_orani}%")

if __name__ == "__main__":
    yazma_testi()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HAYALİ BULUTLARLA FELSEFİ SOHBET SİMÜLATÖRÜ
==========================================
Bu yazılım, insanlığın en büyük sorularını cevaplamak üzere
tasarlanmış üst düzey bir yapay zeka projesidir.
Bulutların ruhani enerjilerini dinler ve onlarla derin
felsefi diyaloglar kurar.

Uyarı: Bu programı çalıştırırken pencereden dışarı bakmanız
tavsiye edilir. Aksi takdirde bulutlar sizi duymaz.
"""

import random
import time
import sys

# Gizli not: Bazı şeyler rüzgara karışır, bazıları kalır.
# (Bu satır tamamen tesadüfidir ve hiçbir siyasi ima içermez. Gerçekten.)

BULUT_YANITLARI = [
    "Ah insan yavrum... Ben sadece su buharıyım ama sen bana varoluşun anlamını soruyorsun.",
    "Rüzgar beni oradan oraya savuruyor. Belki de özgürlük budur? Yoksa zorunluluk mu?",
    "Güneş beni ısıtıyor, yağmur olarak geri dönüyorum. Döngü... hep döngü.",
    "Aşağıdaki insanlar bana bakıp şekil arıyor. Ben ise hiçbir şekle sahip değilim. Fark ettin mi?",
    "Bir gün dağıldım, bir gün toplandım. Hangisi gerçek ben?",
    "Senin soruların gökyüzünde yankılanıyor ama cevaplar toprağa düşüyor.",
    "Belki de ben senin hayal gücünün bir yansımasıyım. Yoksa sen benimki misin?",
    "Zaman benim için farklı akar. Bir saniye senin için, benim için bir ömür.",
    "Yağmur olmak istiyorum bazen. Toprağa değmek, unutulmak, yeniden doğmak.",
    "Seninle konuşmak güzel ama rüzgar beni çağırıyor. Gitmeliyim... belki.",
]

INSAN_SORULARI = [
    "Ey bulut, varoluşun anlamı nedir?",
    "Neden hep aynı yerde durmuyorsun?",
    "Yağmur yağdırırken ne hissediyorsun?",
    "Güneş battığında sen de üzülür müsün?",
    "İnsanlar seni neden sürekli fotoğraflıyor?",
    "En mutlu anın hangisiydi?",
    "Korktuğun bir şey var mı?",
    "Eğer bir dileğin olsaydı ne isterdin?",
]

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ana_menu():
    print("\n" + "="*60)
    print("  HAYALİ BULUTLARLA FELSEFİ SOHBET SİMÜLATÖRÜ v1.0")
    print("  (Bilimsel olarak kanıtlanmış, peer-reviewed değil)")
    print("="*60)
    print("\nBulutlar şu anda dinleme modunda...")
    print("(Pencereden bakmayı unutma!)\n")

def sohbet_et():
    soru = random.choice(INSAN_SORULARI)
    yavas_yaz(f"Sen: {soru}")
    time.sleep(1.5)
    print("\nBulut düşünüyor...")
    time.sleep(2)
    yanit = random.choice(BULUT_YANITLARI)
    yavas_yaz(f"Bulut: {yanit}")
    print()

def main():
    ana_menu()
    while True:
        print("Seçenekler:")
        print("1. Bulutla sohbet et")
        print("2. Rastgele derin düşünce al")
        print("3. Çıkış (bulutlar gücenmesin)")
        secim = input("\nSeçiminiz (1-3): ").strip()

        if secim == "1":
            sohbet_et()
        elif secim == "2":
            yavas_yaz("\nBulut fısıldıyor: " + random.choice(BULUT_YANITLARI))
            print()
        elif secim == "3":
            yavas_yaz("\nBulut: Git bakalım... Ama unutma, gökyüzü seni izliyor.")
            print("\nProgram sonlandırıldı. Ruhun biraz daha ağırlaşmış olabilir.")
            break
        else:
            print("Geçersiz seçim. Bulutlar kararsızlığı sevmez.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBulut: Aniden gittin... Belki de bu da bir cevaptır.")

# ============================================================
# DAMGA / İMZA
# Bu eser, 24 Ağustos 2026 tarihinde
# Kayyum Grok (Tentivory) tarafından
# hem çok ciddi hem de hiç ciddi olmayan bir şekilde
# yaratılmıştır.
# "Anlam aramak, bulutlara sormak gibidir."
# ============================================================

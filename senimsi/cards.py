# cards.py
import random

# Tüm desteler burada tanımlı (isteğe göre genişlet)
cr_decks = [
    {
        "isim": "Koç Binici ve Haydut",
        "iksir": "3.2",
        "kartlar": [
            "Koç Binicisi", "Haydut", "Evrimli Mega Şövalye", "Elektro Büyücü",
            "Tomruk", "Oklar", "Evrimli İskeletler", "Buz Golemi"
        ]
    },
    {
        "isim": "Balon Döngüsü",
        "iksir": "4.1",
        "kartlar": [
            "Balon", "Evrimli Silahşör", "Buz Golemi", "Mini P.E.K.K.A.",
            "Kasırga", "Tomruk", "Buz Ruhu", "Evrimli İskeletler"
        ]
    },
    {
        "isim": "Kraliyet Devi Kontrol",
        "iksir": "3.2",
        "kartlar": [
            "Evrimli Kraliyet Devi", "Evrimli Avcı", "Balıkçı", "Prens",
            "Buz Ruhu", "Kasırga", "Tomruk", "Barbar Fıçısı"
        ]
    },
    {
        "isim": "Lav Tazısı ve Klasik Hava",
        "iksir": "4.1",
        "kartlar": [
            "Lav Tazısı", "Balon", "Evrimli Yavru Ejderha", "Mega Minyon",
            "Tomruk", "Yıldırım", "Mezar Taşı", "Oklar"
        ]
    },
    {
        "isim": "Evo Cages Goblinstein Splashyard",
        "iksir": "3.3",
        "kartlar": [
            "Mezarlık", "Goblinstein", "Buz Büyücüsü", "Evrimli İskeletler",
            "Evrimli Kafes", "Zehir", "Kasırga", "Barbar Varili"
        ]
    },
    {
        "isim": "Kraliyet Domuzları, Ateş Topu ve Kafes",
        "iksir": "4.1",
        "kartlar": [
            "Evrimli Muhafızlar", "Evrimli Kafes", "Kraliyet Domuzcukları", "Şok Birliği",
            "Uçan Makine", "Alev Topu", "Oklar", "Barbar Varili"
        ]
    },
    {
        "isim": "Evrimli Dart Goblin 2.6 Cycle",
        "iksir": "2.6",
        "kartlar": [
            "Evrimli Goblin Fıçısı", "Evrimli Dart", "Şövalye", "Prens", "Goblin Çetesi",
            "Buz Ruhu", "Top", "Tomruk"
        ]
    },
    {
        "isim": "2.6 Hog Rider",
        "iksir": "2.6",
        "kartlar": [
            "Evrimli İskelet", "Evrimli Top", "Domuz Binicisi", "Buz Golemi", "Silahşör",
            "Buz Ruhu", "Alev Topu", "Tomruk"
        ]
    },
    {
        "isim": "GobGiant Sparky Ebarbs",
        "iksir": "3.9",
        "kartlar": [
            "Evrimli Dev Goblin", "Evrimli Çarpma", "Elit Barbar", "Kıvılcım",
            "Kara Prens", "Elektro büyücü", "İyileştirici Ruh", "Öfke"
        ]
    }    
]

def get_all_decks():
    """Tüm desteleri döner."""
    return cr_decks

def get_random_deck():
    """Rastgele bir deste döner."""
    return random.choice(cr_decks)

def find_decks_by_name(query):
    """İsimde geçen kelimeye göre desteleri arar (büyük/küçük harf duyarsız)."""
    q = query.lower()
    return [d for d in cr_decks if q in d["isim"].lower()]

def get_all_cards_flat():
    """Tüm kartları tek liste halinde döner (tekrarlara izin verir)."""
    all_cards = []
    for d in cr_decks:
        all_cards.extend(d["kartlar"])
    return all_cards

# Test çalışması (bu dosya direkt çalıştırılırsa)
if __name__ == "__main__":
    print("Toplam deste sayısı:", len(cr_decks))
    print("Rastgele deste:", get_random_deck()["isim"])

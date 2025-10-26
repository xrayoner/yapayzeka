from flask import Flask, render_template, request, jsonify
import math, random, json
import cards# CR kartları için

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json["message"]
    user_input_low = user_input.lower().strip()

    # 🎮 CR Deste
    if user_input_low == "cr deste":
        deste = cards.get_random_deck()
        kartlar = "\n".join([f"• {k}" for k in deste["kartlar"]])
        response_text = (
            f"CR DESTE: {deste['isim']}\n"
            f"İKSİR: {deste['iksir']}\n"
            f"KARTLAR:\n{kartlar}"
        )
        return jsonify(response=response_text)

    # ➕ Matematik işlemleri
    elif any(op in user_input for op in ["+", "-", "*", "/", "**"]):
        try:
            sonuc = eval(user_input)
            return jsonify(response=f"Sonuç: {sonuc}")
        except:
            return jsonify(response="❌ Geçersiz matematik işlemi!")

    # 🔢 EBOB
    elif user_input_low.startswith("ebob "):
        try:
            _, a, b = user_input.split()
            a, b = int(a), int(b)
            sonuc = math.gcd(a, b)
            return jsonify(response=f"{a} ile {b} sayılarının EBOB'u: {sonuc}")
        except:
            return jsonify(response="⚠️ Kullanım: ebob <sayı1> <sayı2>")

    # 🔢 EKOK
    elif user_input_low.startswith("ekok "):
        try:
            _, a, b = user_input.split()
            a, b = int(a), int(b)
            ebob = math.gcd(a, b)
            ekok = (a * b) // ebob
            return jsonify(response=f"{a} ile {b} sayılarının EKOK'u: {ekok}")
        except:
            return jsonify(response="⚠️ Kullanım: ekok <sayı1> <sayı2>")

    # 🔹 Aralarında Asal
    elif user_input_low.startswith("aa "):
        try:
            _, a, b = user_input.split()
            a, b = int(a), int(b)
            ebob = math.gcd(a, b)
            if ebob == 1:
                return jsonify(response=f"✅ {a} ile {b} aralarında asaldır.")
            else:
                return jsonify(response=f"❌ Hayır, {a} ile {b}, {ebob} sayısına bölünür.")
        except:
            return jsonify(response="⚠️ Kullanım: aa <sayı1> <sayı2>")

    # √ Kök Hesaplama
    elif user_input_low.startswith("kök "):
        try:
            _, sayi = user_input.split()
            sayi = int(sayi)
            kok = int(math.sqrt(sayi))
            kalan = sayi - kok**2
            if kalan == 0:
                return jsonify(response=f"{sayi}'nin karekökü = {kok}")
            else:
                return jsonify(response=f"{sayi} = {kok} kök {kalan}")
        except:
            return jsonify(response="⚠️ Kullanım: kök <sayı>")

    # 💬 Sohbet
    elif any(s in user_input_low for s in ["merhaba", "maraba", "merabe", "meraba", "mehraba", "selamün aleyküm", "hello", "hi"]):
      return jsonify(response="Sanada merhaba, nasılsın? 😊")

    elif any(s in user_input_low for s in ["nasılsın", "nasilsın", "nasilsun", "nasulsun", "nbr"]):
      return jsonify(response="İyiyim, sen nasılsın? 😊")

    elif any(s in user_input_low for s in ["iyiyim", "iym", "iyim", "güzel", "müq", "müp"]):
      return jsonify(response="İyi olmana sevindim! 😊")

    elif any(s in user_input_low for s in ["kötü", "bok gibi"]):
      return jsonify(response="Üzüldüm. Noldu, anlatmak ister misin?")

    elif any(s in user_input_low for s in ["tşk", "tsk", "teşekkürler", "sağol", "sagol", "taşakkürler"]):
      return jsonify(response="Rica ederim. Sorduğun için ben sana sağol.")

    elif "kim tarafından yazıl" in user_input_low:
      return jsonify(response="Ben Hasan Efe tarafından yazıldım! 🧠")

    elif "chatgpt mi senmi" in user_input_low or "gemini mi senmi" in user_input_low:
      return jsonify(response="Benim kendi yanıtlarım var, ben.")

    elif "81 ili say" in user_input_low:
      return jsonify(response="Elbette, Türkiye'deki 81 ili liste şeklinde ve alfabetik sırayla ayrıntılı bir şekilde sunuyorum. "
                            "Adana, Adıyaman, Afyonkarahisar, Ağrı, Amasya, Ankara, Antalya, Artvin, Aydın, Balıkesir, Bilecik, "
                            "Bingöl, Bitlis, Bolu, Burdur, Bursa, Çanakkale, Çankırı, Çorum, Denizli, Diyarbakır, Düzce, Edirne, "
                            "Elazığ, Erzincan, Erzurum, Eskişehir, Gaziantep, Giresun, Gümüşhane, Hakkari, Hatay, Iğdır, Isparta, "
                            "İstanbul, İzmir, Kahramanmaraş, Karabük, Karaman, Kars, Kastamonu, Kayseri, Kilis, Kırıkkale, Kırklareli, "
                            "Kırşehir, Kocaeli, Konya, Kütahya, Malatya, Manisa, Mardin, Mersin, Muğla, Muş, Nevşehir, Niğde, Ordu, "
                            "Osmaniye, Rize, Sakarya, Samsun, Şanlıurfa, Siirt, Sinop, Sivas, Şırnak, Tekirdağ, Tokat, Trabzon, "
                            "Tunceli, Uşak, Van, Yalova, Yozgat, Zonguldak, Aksaray, Bayburt.")
if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)



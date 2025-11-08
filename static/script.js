document.getElementById("sendBtn").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
function showHamzaOnce() {
    let popup = document.getElementById("hamzaPopup");
    if (!popup) {
        popup = document.createElement("div");
        popup.id = "hamzaPopup";
        popup.innerHTML = `<img src="/static/hamza.jpg" alt="hamza">`;
        document.body.appendChild(popup);
    }

    const license = document.getElementById("license");
    popup.classList.add("visible");
    if (license) license.classList.add("visible");

    // Bot mesajı ekle
    const chatBox = document.getElementById("chatBox");
    if (chatBox) {
        const botMsg = document.createElement("div");
        botMsg.classList.add("message-box", "bot-message");
        botMsg.textContent = "BU RESİM HAMZA'DAN İZİN ALINMIŞTIR. KALDIRMAK İSTİYORSANIZ hasanefeoner10@gmail.com adresine e-mail atınız";
        chatBox.appendChild(botMsg);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    setTimeout(() => {
        popup.classList.remove("visible");
        if (license) license.classList.remove("visible");
        // İsterseniz tamamen kaldırmak için:
        // setTimeout(() => popup.remove(), 300);
    }, 3000); // 3 saniye sonra kaybolur
}

function sendMessage() {
    const userInput = document.getElementById("userInput");
    const message = userInput.value.trim();
    const chatBox = document.getElementById("chatBox");

    if (message === "") return;

    // Kullanıcı mesajını ekle
    const userMsg = document.createElement("div");
    userMsg.classList.add("message-box", "user-message");
    userMsg.textContent = message;
    chatBox.appendChild(userMsg);
    chatBox.scrollTop = chatBox.scrollHeight;

    userInput.value = "";

    // Eğer tetikleyici mesajsa popup göster ve backend'e gönderme
    if (message.toLowerCase() === "hamza 2.0") {
        showHamzaOnce();
        return;
    }

    // Backend'e gönder
    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        // Bot mesajını ekle
        const botMsg = document.createElement("div");
        botMsg.classList.add("message-box", "bot-message");
        botMsg.textContent = data.response;
        chatBox.appendChild(botMsg);
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error("Hata:", error));
}

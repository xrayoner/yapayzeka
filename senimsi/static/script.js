document.getElementById("sendBtn").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

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

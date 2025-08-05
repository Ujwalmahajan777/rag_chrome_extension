document.addEventListener("DOMContentLoaded", () => {
  const urlInput = document.getElementById("urlInput");
  const questionInput = document.getElementById("questionInput");
  const loadBtn = document.getElementById("loadBtn");
  const sendBtn = document.getElementById("sendBtn");
  const chatBox = document.getElementById("chatBox");

  function addMessage(sender, text) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);

    const iconSpan = document.createElement("span");
    iconSpan.classList.add("message-icon");
    iconSpan.textContent = sender === "user" ? "👤" : "🤖";

    const textSpan = document.createElement("span");
    textSpan.textContent = text;

    messageDiv.appendChild(iconSpan);
    messageDiv.appendChild(textSpan);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  loadBtn.addEventListener("click", async () => {
    const url = urlInput.value.trim();
    if (!url) return;

    addMessage("bot", `Loading content from: ${url} ...`);

    try {
      const res = await fetch("http://localhost:8000/set_url", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url })
      });

      if (res.ok) {
        addMessage("bot", "✅ Content loaded! You can now ask questions.");
      } else {
        addMessage("bot", "❌ Failed to load content.");
      }
    } catch (err) {
      addMessage("bot", "⚠️ Error connecting to server.");
    }
  });

  sendBtn.addEventListener("click", async () => {
    const query = questionInput.value.trim();
    if (!query) return;
    addMessage("user", query);
    questionInput.value = "";

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
      });

      if (res.ok) {
        const data = await res.json();
        addMessage("bot", data.response || "No response.");
      } else {
        addMessage("bot", "❌ Error from server.");
      }
    } catch (err) {
      addMessage("bot", "⚠️ Error connecting to server.");
    }
  });
});

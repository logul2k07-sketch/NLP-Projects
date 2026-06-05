async function classifyNews() {
  const text = document.getElementById("newsInput").value.trim();
  const resultDiv = document.getElementById("result");
  const errorDiv = document.getElementById("error");

  resultDiv.classList.add("hidden");
  errorDiv.classList.add("hidden");

  if (!text) {
    errorDiv.textContent = "Please enter some news text.";
    errorDiv.classList.remove("hidden");
    return;
  }

  const btn = document.getElementById("classifyBtn");
  btn.textContent = "Classifying...";
  btn.disabled = true;

  try {
    const res = await fetch("/classify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();

    if (data.error) {
      errorDiv.textContent = data.error;
      errorDiv.classList.remove("hidden");
      return;
    }

    document.getElementById("categoryBadge").textContent = data.category;
    document.getElementById("confidenceText").textContent =
      `Confidence: ${data.confidence}%`;

    const scoresList = document.getElementById("scoresList");
    scoresList.innerHTML = "";

    const maxVal = Math.max(...Object.values(data.scores));

    for (const [cat, count] of Object.entries(data.scores)) {
      const pct = maxVal > 0 ? Math.round((count / maxVal) * 100) : 0;
      scoresList.innerHTML += `
        <div class="score-row">
          <span class="score-label">${cat}</span>
          <div class="score-bar-wrap">
            <div class="score-bar" style="width: ${pct}%"></div>
          </div>
          <span class="score-num">${count}</span>
        </div>`;
    }

    resultDiv.classList.remove("hidden");
  } catch {
    errorDiv.textContent = "Something went wrong. Please try again.";
    errorDiv.classList.remove("hidden");
  } finally {
    btn.textContent = "Classify";
    btn.disabled = false;
  }
}

document.getElementById("newsInput").addEventListener("keydown", (e) => {
  if (e.ctrlKey && e.key === "Enter") classifyNews();
});

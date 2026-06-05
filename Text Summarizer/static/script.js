async function summarize() {
    const text = document.getElementById("inputText").value.trim();
    const numSentences = document.getElementById("numSentences").value;
    const resultDiv = document.getElementById("result");
    const errorDiv = document.getElementById("error");
    const summaryText = document.getElementById("summaryText");

    resultDiv.classList.add("hidden");
    errorDiv.classList.add("hidden");

    if (!text) {
        errorDiv.textContent = "Please enter some text to summarize.";
        errorDiv.classList.remove("hidden");
        return;
    }

    const btn = document.getElementById("summarizeBtn");
    btn.textContent = "Summarizing...";
    btn.disabled = true;

    try {
        const res = await fetch("/summarize", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text, num_sentences: numSentences }),
        });

        const data = await res.json();

        if (data.error) {
            errorDiv.textContent = data.error;
            errorDiv.classList.remove("hidden");
        } else {
            summaryText.textContent = data.summary;
            resultDiv.classList.remove("hidden");
        }
    } catch {
        errorDiv.textContent = "Something went wrong. Please try again.";
        errorDiv.classList.remove("hidden");
    } finally {
        btn.textContent = "Summarize";
        btn.disabled = false;
    }
}

async function analyzeSentiment() {
    let review = document.getElementById("review").value;
    let response = await fetch("https://your-vercel-api-url.vercel.app/classify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ review: review })
    });

    let data = await response.json();
    document.getElementById("result").innerHTML = `<strong>Sentiment:</strong> ${data.sentiment} (Confidence: ${data.confidence.toFixed(2)})`;
}

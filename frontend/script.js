async function uploadPDF() {
    const file = document.getElementById("pdfFile").files[0];
    if (!file) {
        alert("Please select a PDF file first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    document.getElementById("uploadStatus").innerText = data.message;
}

async function askQuestion() {
    const question = document.getElementById("question").value;
    if (!question) {
        alert("Please type a question first.");
        return;
    }

    const formData = new FormData();
    formData.append("question", question);

    const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    document.getElementById("answer").innerText = data.answer;
}

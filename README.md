# GenAI for PDF Summarizer & Question Generator

## 📌 Project Overview

GenAI-for-Pdf-Summarizer is an AI-powered web application designed to summarize PDF documents and generate meaningful questions using advanced language models (GPT-4o or compatible models). The system reads the content from uploaded PDF files, produces concise summaries (around 250 words), and generates six context-based, relevant questions derived solely from the PDF content.

This project is ideal for students, researchers, analysts, and professionals who want to quickly extract insights from lengthy documents.

![image](https://github.com/user-attachments/assets/00c4e604-bb3d-435e-ae03-26782649c145)

---

## 🚀 Key Features

* 📄 **Upload and Process PDF Files**
* 🧠 **AI-Powered Summarization** using Generative AI models
* ❓ **Automated Question Generation** (6 context-aware questions)
* 📂 **Artifacts Folder for Uploaded PDFs**
* 🌐 **User-Friendly Interface** (HTML, CSS, JavaScript frontend)
* ⚙️ **Backend Powered by Python & Flask** (or FastAPI if applicable)

---

## 📁 Project Structure

```
GenAI-for-Pdf-Summarizer/
│
├── artifacts/           # Stores uploaded PDF files
├── src/                 # Backend logic, PDF reader, AI service handlers
├── static/              # CSS, JavaScript, images
├── templates/           # HTML templates (UI pages)
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
├── LICENSE              # License information
└── README.md            # Project documentation
```

---

## 🛠️ Technologies Used

| Component        | Technology             |
| ---------------- | ---------------------- |
| Frontend         | HTML, CSS, JavaScript  |
| Backend          | Python (Flask/FastAPI) |
| AI Model         | GPT-4o / OpenAI API    |
| PDF Processing   | PyPDF2, pdfplumber     |
| Deployment Ready | Azure / Docker ready   |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/GenAI-for-Pdf-Summarizer.git
cd GenAI-for-Pdf-Summarizer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Keys

Create a `.env` file and add your OpenAI or API credentials:

```
OPENAI_API_KEY=your_api_key_here
```

### 4️⃣ Run the Application

```bash
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## ▶️ How It Works

1. User uploads a PDF file.
2. System reads and extracts text from the PDF.
3. GenAI generates a concise 250-word summary.
4. AI generates 6 meaningful questions from the PDF content.
5. Results are displayed and available for download or copy.

---

## 📊 Dataset Used (For Testing)

This project has been tested using the **“Dataset of PDF Files”** from Kaggle:
🔗 [https://www.kaggle.com/datasets/manisha717/dataset-of-pdf-files](https://www.kaggle.com/datasets/manisha717/dataset-of-pdf-files)

---

## 📌 Future Enhancements

* ✅ Multi-page PDF summarization with context retention
* ✅ Support for multiple summary lengths (short, medium, detailed)
* ✅ Export results as PDF / DOCX
* ✅ Add voice-based summary playback (Text-to-Speech)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## 🙌 Acknowledgements

* OpenAI GPT models
* PyPDF2, pdfplumber
* Flask Framework
* Kaggle Dataset Providers

---

## ⭐ Show Your Support

If you like this project, please ⭐ the repository and share it with others!

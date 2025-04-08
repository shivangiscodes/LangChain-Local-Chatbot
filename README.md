# 🌟 LangChain-LocalChatbot

A Streamlit-based chatbot powered by LangChain and OpenAI, designed to answer questions from uploaded text files using local document retrieval.

---

## 🚀 Features

- 📄 Upload any `.txt` file and ask questions based on its contents.
- 🔍 Uses LangChain's `RetrievalQA` pipeline for intelligent Q&A.
- 💬 Powered by OpenAI's GPT models for context-aware responses.
- 🧠 Embedding and chunking handled with `FAISS` and `TextSplitter`.
- 🌐 Fully interactive and private interface via Streamlit.

---

## 🛠️ Requirements

Install all dependencies using:

```bash
pip install streamlit langchain openai faiss-cpu

```
🔑 Setup
OpenAI API Key
Replace the line in chatbot_ui.py with your actual OpenAI API key:

os.environ["OPENAI_API_KEY"] = "your-openai-key"

---

▶️ Run the App
To launch the chatbot app, run:

bash
Copy
Edit
streamlit run chatbot_ui.py

---

📥 Usage
Upload a .txt file using the file uploader.

Type your question in the input box.

Click "Ask" and get a response from the chatbot based on your file’s content.

---

🧪 Example Use Case
Upload a research paper, product manual, or textbook chapter and query it interactively for summaries, answers, or clarifications — all on your local system with no external file sharing.

---

📃 License
This project is for educational and demonstration purposes only.

---

🙌 Acknowledgements
Thanks to LangChain, OpenAI, and Streamlit for their powerful tools and support for developers.

# AI Research Assistant 

An intelligent assistant designed to streamline academic research by leveraging advanced AI techniques. This tool integrates Retrieval-Augmented Generation (RAG) with a multi-agent system to efficiently process and summarize information from academic papers.

---

## 🧠 Features

- **PDF Text Extraction**:Utilizes `PyPDF2` to extract text from academic papers in PDF format
- **Semantic Embedding**:Employs `SentenceTransformer` to convert text into meaningful embeddings
- **Efficient Retrieval**:Implements `FAISS` for fast and accurate document retrieval
- **Multi-Agent System**:
  - **Retrieval Agent**:Fetches relevant documents based on user queries
  - **Generation Agent**:Generates coherent responses using OpenAI's GPT models
- **User-Friendly Interface**:Built with `Streamlit` to provide an interactive web application

---

## 🏗️ Architecture Overview

1. **Data Collection & Preprocessing**:
    Extracts text from PDFs located in a specified director.
2. **Knowledge Base Construction**:
    Converts extracted text into embeddings using `SentenceTransformer.
    Indexes embeddings with `FAISS` for efficient similarity searc.
3. **Multi-Agent System**:
   - **Retrieval Agent** Handles user queries by retrieving top-k relevant document.
   - **Generation Agent** Generates answers based on retrieved documents using OpenAI's GPT model.
4. **User Interface**:
    Provides an input field for user queries and displays generated response.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher- OpenAI API ey

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Aarushi232005/-AI_Research_Assistant.git
   cd -AI_Research_Assistant
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

  - Create a `.env` file in the root directoy.
  - Add your OpenAI API ky:

     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

---

## 🧪 Usage

1. **Prepare your PDF documents**:
  - Place all academic PDFs in a directory, e.g., `./pdf/`.

2. **Run the application**:

   ```bash
   streamlit run app.py
   ```

3. **Interact with the assistant**:
  - Open the provided local URL in your brower.
  - Enter your research query in the input fild.
  - View the generated response based on the retrieved documets.

---

## 📁 Project Structure

```bash
.
├── app.py                 # Streamlit application
├── rag_pipeline.py        # Core logic for RAG system
├── cohere.env             # Environment variables (e.g., API keys)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── __pycache__/           # Cached Python files
```

---

## 🤝 Contribuing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull reuest.

---

## 📄 Liense

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for dtails.

---

## 📬 Cntact

For any inquiries or feedback, please contact [Aarushi232005](https://github.com/Aarushi32005).

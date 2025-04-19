# rag_pipeline.py

import os
from dotenv import load_dotenv

from langchain_cohere import ChatCohere, CohereEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationSummaryMemory
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
COHERE_API_KEY = "3fqSbt1Wj1ZSmnPaOPdLXRzou6QngA7L0tuLB4Ce"

# Embedding model setup
embedding_model = CohereEmbeddings(
    cohere_api_key=COHERE_API_KEY,
    model="embed-english-v3.0",
)

# LLM setup
llm = ChatCohere(cohere_api_key=COHERE_API_KEY, model="command-a-03-2025")

# Prompt template
template = """
As a senior research reviewer, carefully analyze the following materials and conversation history to provide a critical evaluation:

<Context>
{context}
</Context>

<Conversation History>
{history}
</Conversation History>

Research Question: {question}

Your expert analysis should include:
1. Summary of key methodology and findings
2. Critical assessment of research validity and significance
3. Identification of key contributions to the field
4. Evaluation of limitations and potential biases
5. Recommendations for future research directions

Maintain rigorous academic standards while ensuring clarity for interdisciplinary audiences. Highlight both strengths and weaknesses using evidence from the context.

Expert Analysis:
"""
prompt = PromptTemplate(input_variables=["history", "context", "question"], template=template)

def split_text(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    return splitter.create_documents([content])


# Load vector store
def create_vector_store(docs):
    return FAISS.from_documents(
        documents=docs,
        embedding=embedding_model,
        distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT
    )

# Get retriever
def get_retriever(vector_store):
    return vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 20,
            "lambda_mult": 0.5,
            "score_threshold": 0.7,
        }
    )

# Build the full RAG pipeline
def build_qa_pipeline(file_path: str):
    chunks = split_text(file_path)
    vector_store = create_vector_store(chunks)
    retriever = get_retriever(vector_store)
    memory = ConversationSummaryMemory(llm=llm, memory_key="history", input_key="question")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={
            "prompt": prompt,
            "memory": memory
        },
        return_source_documents=True
    )

    return qa_chain

# Invoke the pipeline
def query_pipeline(qa_chain, query: str):
    result = qa_chain.invoke(query)
    return result["result"]
# rag_pipeline.py
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_cohere import CohereEmbeddings

embedding_model = CohereEmbeddings(
    cohere_api_key= "3fqSbt1Wj1ZSmnPaOPdLXRzou6QngA7L0tuLB4Ce" ,
    model="embed-english-v3.0",
)

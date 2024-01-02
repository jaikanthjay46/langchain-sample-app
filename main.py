from dotenv import load_dotenv
from traceloop.sdk import Traceloop
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# Load environment variables
load_dotenv()

# Initialize Traceloop
Traceloop.init(app_name="PDF Chat")

# Mock Data
usernames = ["John McClane", "Lucy McClane", "Hans Gruber"]


# Model Configuration
model = ChatOpenAI(temperature=0.2, max_tokens=200)

def demo_queries():
    # Load PDF and split into pages
    loader = UnstructuredPDFLoader("book.pdf")
    pages = loader.load_and_split()
    
    # Initialize embeddings and document retriever
    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(pages, embeddings).as_retriever()
    
    
    for i in range(1, 20):
        queries = [
            "What is the book about?",
            "Who is the author?",
            "What is the name of the author?",
            "What is the name of the book?",
            "Who is Rich Dad?",
            "Who is Poor Dad?",
            "Give me a summary of the book in 100 words.",
            "What are the 3 key takeaways from the book?"
        ]
        for queryroot in queries:
            for ind, querysuffix in enumerate([' Concise Answer', 'Long Answer (~250 words)', 'Long Answer (~750 words)']):
                # Set Traceloop association properties
                Traceloop.set_association_properties({ "user_id": usernames[ind], "chat_id": querysuffix })
                
                # Construct the query
                query = queryroot + querysuffix
                print(query)
                
                # Retrieve relevant documents
                docs = docsearch.get_relevant_documents(query)
                
                # Load question answering chain
                chain = load_qa_chain(model, chain_type="stuff")
                
                # Run the chain to get the answer
                output = chain.run(input_documents=docs, question=query)
                print(output)

# Call the function to demonstrate RAG pipeline
demo_queries()

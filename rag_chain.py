from langchain.retrievers import ContextualCompressionRetriever 
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnablePassthrough ,RunnableSequence ,RunnableLambda
from dotenv import load_dotenv
load_dotenv()


llm =ChatDeepSeek(model_name = 'deepseek-chat',streaming= False)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
question = 'what is generative AI?'



def get_vector_store(persist_directory):
    
    vector_store = Chroma(embedding_function=embeddings , persist_directory=persist_directory)
    return vector_store

def format_docs (docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_retriever (persist_directory):
    vector_store = get_vector_store(persist_directory)

    base_retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 5, "score_threshold": 0.2}
    )
    base_compressor = LLMChainExtractor.from_llm(llm)

    retriever = ContextualCompressionRetriever(
        base_retriever= base_retriever,
        base_compressor= base_compressor
    )
    return retriever

def get_rag_chain(persist_directory):
        
    retriever = get_retriever(persist_directory)
        

    from langchain_core.prompts import PromptTemplate

    prompt = PromptTemplate(
         template=(
        "You are a helpful AI assistant integrated into a Chrome Extension. "
        "Your primary knowledge source is the provided web page content. "
        "If the content is partially related to the question, try to give the best possible answer using that context.\n\n"

        "Guidelines:\n"
        "1. Use the provided context as your main source.\n"
        "2. If you find partial matches, still attempt to answer.\n"
        "3. If the topic is clearly mentioned in context but details are missing, provide a short explanation based on related context.\n"
        "4. If the context is completely unrelated to the question, politely state that the content does not cover the topic.\n"
        "5. Keep answers concise and accurate.\n\n"

        "=== Web Page Context Start ===\n"
        "{context}\n"
        "=== Web Page Context End ===\n\n"

        "User Question: {question}\n\n"
        "Your Answer:"
        ),
        input_variables=['context', 'question']
        )



    parallel_chain = RunnableParallel({
            'context': retriever | RunnableLambda(format_docs),
            'question': RunnablePassthrough()
        })

    parser =StrOutputParser() 

    main_chain = main_chain = parallel_chain | prompt | llm | parser

    return main_chain

        


if __name__ == "__main__":
    chain = get_rag_chain()
    result = chain.invoke(question)
    print(result)
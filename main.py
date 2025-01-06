from backend.conversation.chat import chat_with_travel_assistant
from backend.memory.chroma_memory.add_data import add_pdf_to_chroma
from backend.memory.mem0_memory.try_mem0 import add_memory_in_mem0, extract_relevant_memories

if __name__ == "__main__":
    # add_pdf_to_chroma(
    #     pdf_path="/Users/arkajitdatta/Documents/projects/springboard/embedding/pdfs/jaipur_wiki.pdf"
    # )
    chat_with_travel_assistant()
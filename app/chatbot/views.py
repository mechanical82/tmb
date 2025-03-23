from django.shortcuts import render
import datetime

# New Chat
# import os
# from django.shortcuts import render
# from django.http import JsonResponse
# from dotenv import load_dotenv
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
# from langchain.docstore.document import Document
# import openai


def chatbot(request):
    context = {
        'title': 'Чат с искусственным интелектом',
        'description': 'Чат с искусственным интелектом',
        'time_message': datetime.datetime.now().strftime('%H:%M'),
        'current_path': request.get_full_path(),
    }
    return render(request, "chatbot.html", context)


# # Загружаем переменные окружения
# load_dotenv()

# openai.api_key = os.environ.get("OPENAI_API_KEY")

# # Определяем класс для обработки документа
# class Chunk:
#     def __init__(self, path_to_base: str, sep: str = " ", ch_size: int = 2048):
#         with open(path_to_base, 'r', encoding='utf-8') as file:
#             document = file.read()
    
#         source_chunks = []
#         splitter = CharacterTextSplitter(separator=sep, chunk_size=ch_size)
#         for chunk in splitter.split_text(document):
#             source_chunks.append(Document(page_content=chunk, metadata={}))

#         embeddings = OpenAIEmbeddings()
#         self.db = FAISS.from_documents(source_chunks, embeddings)

#     def get_answer(self, query: str):
#         system_message = (
#             "Ты-консультант в ювелирной компании, ответь на вопрос клиента на основе документа. "
#             "Не придумывай ничего от себя, отвечай кратко по документу. "
#             "Не упоминай, что используешь документ для ответа."
#         )
#         docs = self.db.similarity_search(query, k=4)
#         message_content = '\n'.join([doc.page_content for doc in docs])
#         messages = [
#             {"role": "system", "content": system_message},
#             {"role": "user", "content": f"Документ: {message_content}\n\nВопрос: {query}"}
#         ]

#         completion = openai.ChatCompletion.create(model="gpt-4o-mini",
#                                                   messages=messages,
#                                                   temperature=0)
#         return completion.choices[0].message.content

# # Загружаем базу (путь к текстовому файлу с данными)
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# path_to_data = os.path.join(BASE_DIR, "data.txt")

# chunk = Chunk(path_to_data)

# def chatbot_view(request):
#     if request.method == "POST":
#         user_message = request.POST.get("message", "")
#         bot_response = chunk.get_answer(user_message)
#         return JsonResponse({"response": bot_response})
#     return render(request, "chat.html")



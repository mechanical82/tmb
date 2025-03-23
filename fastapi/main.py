import ssl
from fastapi import FastAPI
from chunks import Chunk
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ssl

# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# openssl.cnf
# инициализация индексной базы
chunk = Chunk(path_to_base="Simble2.txt")

# класс с типами данных параметров 
class Item(BaseModel): 
    text: str

# создаем объект приложения
app = FastAPI()
# app.add_middleware(HTTPSRedirectMiddleware)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
ssl_context.load_cert_chain('/path/to/cert.pem', keyfile='/path/to/key.pem')

# настройки для работы запросов
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# функция обработки get запроса + декоратор 
@app.get("/")
def read_root():
    return {"message": "answer"}

# функция обработки post запроса + декоратор 
@app.post("/api/get_answer")
def get_answer(question: Item):
    answer = chunk.get_answer(query=question.text)
    return {"message": answer}


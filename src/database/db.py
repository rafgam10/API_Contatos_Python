import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host=os.getenv('ENV_HOST'),
        port=os.getenv('ENV_PORT'),
        user=os.getenv('ENV_USER'),
        password=os.getenv('ENV_PASSWORD')
    )

## Listar Contatos:
def listar_contatos_db():
    contatos = []
    with conectar() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM Contatos;')
            datas = cursor.fetchall()
    
    for data in datas:
        contato = {
            "id": data.get('id'),
            "nome": data.get('nome'),
            "telefone": data.get('telefone'),
            "email": data.get('email'),
            "data_aniversario": data.get('data_aniversario')
        }
        
        contatos.append(contato)
    
    return contatos
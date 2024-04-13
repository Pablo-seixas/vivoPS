import sys
from pathlib import Path

# Adiciona o diretório pai ao sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

# Importa a classe MongoClient do módulo mongo_client
# # from store.db.mongo_client import MongoClient

# Define uma constante global para o número máximo de tentativas de conexão
MAX_CONNECTION_ATTEMPTS = 3

# Função auxiliar para limpar uma string removendo caracteres especiais
def clean_string(string):
    return ''.join(e for e in string if e.isalnum())

# Inicializa o logger do pacote
import logging
logging.basicConfig(level=logging.INFO)


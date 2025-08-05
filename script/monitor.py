#!/usr/bin/env python3

import os
import requests
import logging
from datetime import datetime
from dotenv import load_dotenv

# Caminho do .env
ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=ENV_PATH)

# Carregar variáveis do .env
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
SITE_URL = os.getenv("SITE_URL", "http://localhost")
LOG_FILE = "/var/log/monitoramento.log"

# Configurar log
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def enviar_discord_alerta(mensagem):
    payload = {"content": mensagem}
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code != 204:
            logging.warning(f"Falha ao enviar alerta. Código HTTP: {response.status_code}")
    except Exception as e:
        logging.warning(f"Erro ao enviar alerta para o Discord: {e}")

def verificar_site():
    try:
        resposta = requests.get(SITE_URL, timeout=5)
        if resposta.status_code == 200:
            logging.info(f"Site OK - Status HTTP: {resposta.status_code}")
        else:
            mensagem = f"🚨 Site fora do ar! Status HTTP: {resposta.status_code}"
            logging.error(mensagem)
            enviar_discord_alerta(mensagem)
    except Exception as erro:
        mensagem = f"🚨 Erro ao acessar o site: {erro}"
        logging.error(mensagem)
        enviar_discord_alerta(mensagem)

if __name__ == "__main__":
    verificar_site()

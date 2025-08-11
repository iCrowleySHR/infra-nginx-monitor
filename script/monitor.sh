#!/bin/bash

# Carregar variáveis do .env
ENV_FILE="$(dirname "$0")/.env"
if [ -f "$ENV_FILE" ]; then
    export $(grep -v '^#' "$ENV_FILE" | xargs)
else
    echo "[ERRO] Arquivo .env não encontrado!"
    exit 1
fi

# Configurações
URL="${SITE_URL:-http://localhost}"
WEBHOOK_URL="$DISCORD_WEBHOOK"
LOG_FILE="/var/log/monitoramento.log"
DATA=$(date '+%Y-%m-%d %H:%M:%S')

# Verificar status do site
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$STATUS_CODE" -ne 200 ]; then
    MSG="[$DATA] 🚨 Site fora do ar! Status HTTP: $STATUS_CODE ! Tentando reiniciar..."
    echo "$MSG" >> "$LOG_FILE"

    # Enviar alerta para Discord
    curl -s -H "Content-Type: application/json" \
         -X POST \
         -d "{\"content\": \"$MSG\"}" \
         "$WEBHOOK_URL" > /dev/null
    sudo systemctl restart nginx
else
    echo "[$DATA] ✅ Site OK (Status: $STATUS_CODE)" >> "$LOG_FILE"
fi

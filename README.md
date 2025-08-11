# infra-nginx-monitor

Este projeto tem como objetivo configurar uma infraestrutura Linux local capaz de hospedar um servidor web Nginx com uma página HTML simples, garantindo sua alta disponibilidade por meio de verificações automáticas e envio de alertas em caso de falhas.

Proposto pelo programa de bolsa **CompassUOL**.

<img width="139" height="48" alt="image" src="https://github.com/user-attachments/assets/4faaf2ea-d6c2-4e02-9507-3f4e928108aa" />

---

## Índice

- [Funcionalidades Implementadas](#funcionalidades-implementadas)  
- [Ferramentas utilizadas](#ferramentas-utilizadas)  
- [Distro](#distro)  
- [Instalação do Nginx](#instalação-do-nginx)  
- [Instalação do Git](#instalação-do-git)  
- [Configurações do Nginx](#configurações-do-nginx)  
- [Script de Monitoramento + Webhook](#script-de-monitoramento--webhook)  
- [Explicação do Script monitor.sh](#explicação-do-script-monitorsh)  
- [Testes](#testes)  
- [Finalização](#finalização)  

---

## Funcionalidades Implementadas

- **Hospedagem local** com Nginx e HTML/CSS/JS.
- **Monitoramento automático** do serviço com `monitor.sh`.
- **Integração via Webhook** para alertas no Discord.
- **Execução agendada** com `crontab` para verificar o status a cada minuto.
- **Armazenamento de logs** em `/var/log/monitoramento.log`.
- **Configuração no WSL (Ubuntu)** para fácil uso em ambiente Windows.
- **Controle de serviços** via `systemctl` com comandos documentados.

---

## Ferramentas utilizadas

<table>
  <tr>
    <td align="center">
      <img src="https://skillicons.dev/icons?i=ubuntu" width="60"/><br>
      <sub><b>Ubuntu</b></sub>
    </td>
    <td align="center">
      <img src="https://skillicons.dev/icons?i=html" width="60"/><br>
      <sub><b>HTML</b></sub>
    </td>
    <td align="center">
      <img src="https://skillicons.dev/icons?i=css" width="60"/><br>
      <sub><b>CSS</b></sub>
    </td>
    <td align="center">
      <img src="https://skillicons.dev/icons?i=js" width="60"/><br>
      <sub><b>JavaScript</b></sub>
    </td>
    <td align="center">
      <img src="https://skillicons.dev/icons?i=bash" width="60"/><br>
      <sub><b>Bash</b></sub>
    </td>
    <td align="center">
      <img src="https://skillicons.dev/icons?i=discord" width="60"/><br>
      <sub><b>Discord</b></sub>
    </td>
      <td align="center">
      <img src="https://skillicons.dev/icons?i=nginx" width="60"/><br>
      <sub><b>Nginx</b></sub>
    </td>
    </td>
      <td align="center">
      <img src="https://skillicons.dev/icons?i=git" width="60"/><br>
      <sub><b>Git</b></sub>
    </td>
  </tr>
</table>

---

## Distro

O projeto utiliza a **WSL** do Windows com a Distro **Ubuntu**.
<p align="center">
<img width="978" height="504" alt="image" src="https://github.com/user-attachments/assets/7ba51088-6174-45f2-89b9-081d2b081a4b" />
</p>

---

## Instalação do Nginx
**Nginx** é um servidor web, normalmente utilizado para hospedar sites

A instalação e configuração serão feitas usando o usuário `root`. Para acessar esse usuário, utilize o comando abaixo; será solicitada a senha para prosseguir:

### Sintaxe
```bash
su
```

Após a execução, o terminal ficará assim:
<p align="center">
<img width="979" height="507" alt="image" src="https://github.com/user-attachments/assets/d524d53a-154b-4e64-b51e-ab061668e810" />
</p>

---

Para instalar os pacotes **Nginx**, utilizaremos os comandos:
### Sintaxe
```bash
apt update
apt upgrade
apt install nginx
```

Devemos confirmar todas as instalações que o terminal pedir.
<p align="center">
<img width="978" height="504" alt="image" src="https://github.com/user-attachments/assets/9fcedf38-9243-4193-8758-7d7da15519c8" />
</p>

Automaticamente após a instalação, o servidor já estará funcionando, podemos conferir o status do serviço atráves do comando:

### Sintaxe
```bash
systemctl status nginx
```

Para sair basta clicar `Q` ou `CTRL + C`

<p align="center">
<img width="980" height="503" alt="image" src="https://github.com/user-attachments/assets/c44539a0-804f-4644-a84f-56bb8e24b9d7" />
</p>

Para manipular a aplicação futuramente, utilizaremos essa tabela a seguir.

| Comando                         | Ação                                           |
|----------------------------------|------------------------------------------------|
| `systemctl status`              | Mostra o status geral do `systemd`            |
| `systemctl status nome` | Mostra o status de um serviço específico       |
| `systemctl start nome`  | Inicia o serviço                               |
| `systemctl stop nome`   | Para o serviço                                 |
| `systemctl restart nome`| Reinicia o serviço                             |
| `systemctl reload nome` | Recarrega as configurações sem reiniciar       |
| `systemctl enable nome` | Ativa o serviço para iniciar com o sistema     |
| `systemctl disable nome`| Desativa o serviço no boot                     |
| `systemctl is-active nome` | Verifica se o serviço está ativo           |
| `systemctl list-units --type=service` | Lista todos os serviços carregados       |

Caso o serviço esteja desativado, podemos iniciar ele atráves do comando 

### Sintaxe
```bash
systemctl start nginx
```

---

Como o serviço do **Nginx** já está em execução e o **WSL** configura automaticamente as interfaces de rede, o site pode ser acessado localmente na sua máquina e, em alguns casos, até pela sua rede doméstica (se o compartilhamento estiver ativado).

Para descobrir o IP local da máquina, utilize o comando:

### Sintaxe
```bash
ip -4 a
```
<p align="center">
<img width="978" height="506" alt="image" src="https://github.com/user-attachments/assets/10537702-3a8b-4660-abb6-f6abee7e365b" />
</p>

Com qualquer um dos endereços IP exibidos, você pode acessar o site digitando diretamente no navegador. Isso mostrará a página padrão do **Nginx** em execução no seu ambiente local.

<p align="center">
<img width="1919" height="1000" alt="image" src="https://github.com/user-attachments/assets/a661d69e-9a01-493e-8268-f88e3805f4b1" />
</p>

---

## Instalação do Git
O site que será hospedado está disponível em um repositório no **GitHub**, e utilizaremos o **Git** para clonar esse repositório diretamente para o ambiente do servidor.

Para instalar os pacotes **Git**, utilizaremos os comandos:

### Sintaxe
```bash
apt install git
```

Devemos confirmar todas as instalações que o terminal pedir.

<p align="center">
<img width="978" height="505" alt="image" src="https://github.com/user-attachments/assets/990a2acf-378c-4f42-ac5f-33312ee480f2" />
</p>

---

## Configurações do Nginx

Com o **Nginx** e **Git** já instalados, o próximo passo é implementar o nosso site no servidor para que ele possa ser acessado. Caso necessário, também faremos ajustes nas configurações padrão.


Para obter os arquivos do repositório do **GitHub** e disponibilizá-los no servidor **Nginx**, primeiro precisamos acessar o diretório responsável por hospedar o site.
### Sintaxe
```bash
cd /var/www/html
```
<p align="center">
<img width="977" height="508" alt="image" src="https://github.com/user-attachments/assets/13af554b-fed2-4707-975e-ae3823168c50" />
</p>


### Sintaxe
```bash
git clone https://github.com/iCrowleySHR/infra-nginx-monitor.git
```

<p align="center">
<img width="974" height="507" alt="image" src="https://github.com/user-attachments/assets/5708230d-f8a0-4a3c-b951-fd5e2b6721a4" />
</p>

Com o repositório clonado, precisamos apenas transferir os arquivos do site para a raíz da pasta.
Acesse a pasta com o comando:

### Sintaxe
```bash
cd infra-nginx-monitor/website
```
<p align="center">
<img width="973" height="507" alt="image" src="https://github.com/user-attachments/assets/8f9966a6-1c49-4775-ad03-b6a94aec30c8" />
</p>

O nome dos arquivos podem ser encontrados digitando `ls` dentro da pasta

Depois de entrarmos, usaremos o comando `mv` para mover os arquivos para o diretório `/var/www/html`

### Sintaxe
```bash
mv index.html reveal.js style.css /var/www/html
```
<p align="center">
<img width="977" height="510" alt="image" src="https://github.com/user-attachments/assets/75cacf47-9521-49e1-8158-07c399704d56" />
</p>

Agora voltaremos para a pasta `/var/www/html` para excluirmos os arquivos desnecessários, como o arquivo index do **Nginx** e a pasta que clonamos, que não utilizaremos mais.

### Sintaxe
```bash
cd /var/www/html
rm -r index.nginx-debian.html
rm -r infra-nginx-monitor
```
<p align="center">
<img width="979" height="515" alt="image" src="https://github.com/user-attachments/assets/8e9fdb26-1832-46d6-8eb9-a41cb3d0f779" />
</p>

Depois dessas configurações, se você acessar o seu IP novamente no navegador, você já encontrará seu site hospedado com sucesso!

<p align="center">
<img width="1920" height="1003" alt="image" src="https://github.com/user-attachments/assets/2727fa5f-21a1-4b6a-b4f4-b237339d1d0e" />
</p>

---

O **Nginx** vem configurado automaticamente para funcionamento após sua instalação, mas, os arquivos de configurações de porta e etc, podem ser encontrados nos diretórios abaixo:

`/etc/nginx/sites-enabled/`

`/etc/nginx/sites-available/`

`/etc/nginx/nginx.conf`

---

## Script de Monitoramento + Webhook
O script de monitoramento verifica automaticamente se o servidor Nginx está funcionando. Caso o site fique fora do ar, ele envia um alerta para o Discord usando um Webhook, avisando na hora sobre o problema.
Essa integração é importante para você receber notificações rápidas e conseguir agir antes que o problema afete os usuários. Iremos configurar tudo isso na WSL, junto ao script e o `.env` do repositório.

Nesse projeto, utilizaremos o **Discord** para notificação de erros na nossa aplicação, foi criado um servidor onde por ele será enviado qualquer alerta de erro.

<p align="center">
<img width="1853" height="1005" alt="image" src="https://github.com/user-attachments/assets/9fbf1247-0197-4e7a-9a39-1ccd1dbbac7b" />
</p>

Precisamos do Webhooks do bot, podemos encontrar nesse menu:

`Config. do servidor -> Interações -> Webhooks`

<p align="center">
<img width="1852" height="1033" alt="image" src="https://github.com/user-attachments/assets/5c45ab4c-e1f2-4252-b129-11b9032312d3" />
</p>

<p align="center">
<img width="1920" height="1042" alt="image" src="https://github.com/user-attachments/assets/d1f0a129-3366-4df7-afc4-e3ffcbb82f3f" />
</p>

Copie a URL, ela será muito importante, o script a utilizará para enviar alertas sempre que o servidor estiver offline.

---

## Explicação do Script monitor.sh
O script `monitor.sh` verifica automaticamente se o servidor web está online e envia alertas para o Discord caso o site fique fora do ar. Ele registra tudo em um arquivo de log para acompanhamento.
Veja o código dele todo comentado para entendimento.

```bash
# Define o caminho do arquivo .env (mesmo diretório do script)
ENV_FILE="$(dirname "$0")/.env"

# Verifica se o arquivo .env existe
if [ -f "$ENV_FILE" ]; then
    # Exporta as variáveis do .env, ignorando linhas comentadas
    export $(grep -v '^#' "$ENV_FILE" | xargs)
else
    # Caso não encontre o .env, mostra erro e encerra o script
    echo "[ERRO] Arquivo .env não encontrado!"
    exit 1
fi

# Define a URL do site (do .env ou padrão localhost)
URL="${SITE_URL:-http://localhost}"

# URL do Webhook do Discord (do .env)
WEBHOOK_URL="$DISCORD_WEBHOOK"

# Caminho do arquivo de log
LOG_FILE="/var/log/monitoramento.log"

# Data e hora atuais
DATA=$(date '+%Y-%m-%d %H:%M:%S')

# Faz requisição para o site e captura o código HTTP de resposta
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

# Se o status for diferente de 200, considera que o site está fora do ar
if [ "$STATUS_CODE" -ne 200 ]; then
    # Monta a mensagem de erro
    MSG="[$DATA] 🚨 Site fora do ar! Status HTTP: $STATUS_CODE ! Tentando reiniciar..."
    # Registra no log
    echo "$MSG" >> "$LOG_FILE"
    # Envia alerta para o Discord
    curl -s -H "Content-Type: application/json" \
         -X POST \
         -d "{\"content\": \"$MSG\"}" \
         "$WEBHOOK_URL" > /dev/null
    # Em caso de falha tenta reiniciar o servidor
    sudo systemctl restart nginx
else
    # Caso o site esteja OK, registra no log
    echo "[$DATA] ✅ Site OK (Status: $STATUS_CODE)" >> "$LOG_FILE"
fi

```

---

Criaremos uma pasta para armazenar nossos scripts com o nome `/monitoramento/`, nela iremos armazenar nosso script e configurá-lo:

### Sintaxe
```bash
mkdir /monitoramento

```

<p align="center">
<img width="1360" height="508" alt="image" src="https://github.com/user-attachments/assets/9bc65b32-35d7-45ce-a436-6d3aec0e5b91" />
</p>

Agora entraremos nela e clonaremos denovo o repositório, porém pegaremos apenas o script que precisamos.
Pegaremos o `monitor.sh` e o `.env.example`. O comando abaixo entra na pasta, clona o repositório e move os arquivos necessário para a raíz da pasta `/monitoramento/`. Após isso, exclui os arquivos desnecessários.

### Sintaxe
```bash
cd /monitoramento
git clone https://github.com/iCrowleySHR/infra-nginx-monitor.git
mv infra-nginx-monitor/script/monitor.sh infra-nginx-monitor/script/.env.example /monitoramento/
rm -r infra-nginx-monitor
```

<p align="center">
<img width="1369" height="337" alt="image" src="https://github.com/user-attachments/assets/68d5875c-1f69-45e2-92a3-83edb05ab943" />
<img width="1375" height="192" alt="image" src="https://github.com/user-attachments/assets/930d12ba-d8db-4bb3-9569-104529a740e7" />
</p>

---

Agora vamos configurar o arquivo `.env`. Para isso, abra o arquivo `.env.example` e insira a URL do servidor **Nginx** e a **URL do Webhook**.
Depois de fazer as alterações, salve o arquivo com o nome `.env`. Para isso, utilize o editor **Nano** e, ao salvar, pressione `CTRL + O`, depois altere o nome do arquivo para `.env` e confirme.
Caso não saiba qual é o valor da variável `SITE_URL`, basta usar o comando que utilizamos anteriormente para descobrir a URL do servidor.
É extremamente importante configurar esse arquivo corretamente, pois é através dele que o script saberá qual site monitorar e para quem enviar os avisos em caso de erro. Sem essa configuração, o script não funcionará.

### Sintaxe
```bash
ip -4 a  # Comando para descobrir a IP para acessar o site
```

### Sintaxe
```bash
nano .env.example
```

<p align="center">
<img width="1370" height="628" alt="image" src="https://github.com/user-attachments/assets/72cc5f20-7721-4c64-9865-3166fd5940da" />
</p>

Após isso, devemos dar permissões para o `monitor.sh` e criar os arquivos de logs com as permissões. Podemos utilizar esses comandos.

### Sintaxe
```bash
chmod +x /monitoramento/monitor.sh
sudo touch /var/log/monitoramento.log
sudo chmod 666 /var/log/monitoramento.log
```

<p align="center">
<img width="1372" height="629" alt="image" src="https://github.com/user-attachments/assets/76de5967-3cea-4e67-a7a5-9d621558ce3b" />
</p>


---

Para o código ser executado a cada minuto, devemos acessar o `crontab`.

### Sintaxe
```bash
crontab -e
```

Dentro do arquivo, colocaremos no final dele esse trecho para rodar a cada minuto e salvaremos.

### Sintaxe
```bash
* * * * * /monitoramento/monitor.sh
```

<p align="center">
<img width="1373" height="629" alt="image" src="https://github.com/user-attachments/assets/592bb679-7e2f-4291-a49c-05f6f5b7e290" />
</p>


## Testes

Com todos esses passos, o **Nginx** está online e a cada minuto está sendo monitorado o funcionamento dele pelo `monitor.sh`

Podemos conferir entrando nos logs do script
### Sintaxe
```bash
cat /var/log/monitoramento.log
```

<p align="center">
<img width="1369" height="629" alt="image" src="https://github.com/user-attachments/assets/5491f554-54c6-49df-9cdf-695fe9d00a01" />
</p>

---


Em caso de erros, seremos notificados pelo servidor do **Discord** e será armazenado no `/var/log/monitoramento.log`

Na imagem a seguir, o **Nginx** será parado e aparecerá as mensagens no **Discord**

Podemos usar:
### Sintaxe
```bash
systemctl stop nginx # Coamndo que para a aplicação
```


<p align="center">
<img width="1856" height="1019" alt="image" src="https://github.com/user-attachments/assets/3e12db88-9e51-4c12-9ba8-799ac18cedf3" />
<img width="1072" height="625" alt="image" src="https://github.com/user-attachments/assets/cdf06f58-b833-4971-a765-b9f470d22d94" />
</p>

---

Toda vez que o Linux é ligado, ele sempre executará o script a cada minuto e o **Nginx** sempre estará ligado, com as configurações apresentadas.


## Veja o vídeo de funcionamento

<a href="https://www.youtube.com/watch?v=8fT1ba6jNdo">
  <p align="center">
    <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e1cc40fe-0606-462e-b458-e595de40a31c" />
  </p>
</a>

## Finalização
Com isso, sua infraestrutura local com Nginx está instalada, monitorada e pronta para receber notificações em tempo real via Discord.

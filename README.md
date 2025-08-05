# infra-nginx-monitor

Este projeto tem como objetivo configurar uma infraestrutura Linux local capaz de hospedar um servidor web Nginx com uma página HTML simples, garantindo sua alta disponibilidade por meio de verificações automáticas e envio de alertas em caso de falhas.

Proposto pelo programa de bolsa **CompassUOL**.

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
```bash
systemctl start nginx
```

---

Como o serviço do **Nginx** já está em execução e o **WSL** configura automaticamente as interfaces de rede, o site pode ser acessado localmente na sua máquina e, em alguns casos, até pela sua rede doméstica (se o compartilhamento estiver ativado).

Para descobrir o IP local da máquina, utilize o comando:
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

Nesse diretório, podemos clonar o nosso repositório

### Sintaxe
```bash
git clone https://github.com/iCrowleySHR/infra-nginx-monitor.git
```

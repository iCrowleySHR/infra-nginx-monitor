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

## Instalação e Configuração do Nginx
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

Para instalar os pacotes **Nginx**, você utiliza o comando:
### Sintaxe
```bash
apt update
apt upgrade
apt install nginx
```

Você poderá confirmar todas as instalações que o terminal pedir.
<p align="center">
<img width="978" height="504" alt="image" src="https://github.com/user-attachments/assets/9fcedf38-9243-4193-8758-7d7da15519c8" />
</p>

Automáticamente após a instalação, o servidor já estará funcionando, você podera conferir o status do serviço atráves do comando:

```bash
systemctl status nginx
```

Para sair basta clicar `Q` ou `CTRL + C`

Imagem de como você deve encontrar o terminal: 
<p align="center">
<img width="980" height="503" alt="image" src="https://github.com/user-attachments/assets/c44539a0-804f-4644-a84f-56bb8e24b9d7" />
</p>

Para manipular a aplicação futuramente, utilizaremos essa tabela a seguir.

| Comando                         | Ação                                           |
|----------------------------------|------------------------------------------------|
| `systemctl status`              | Mostra o status geral do `systemd`            |
| `systemctl status nome.service` | Mostra o status de um serviço específico       |
| `systemctl start nome.service`  | Inicia o serviço                               |
| `systemctl stop nome.service`   | Para o serviço                                 |
| `systemctl restart nome.service`| Reinicia o serviço                             |
| `systemctl reload nome.service` | Recarrega as configurações sem reiniciar       |
| `systemctl enable nome.service` | Ativa o serviço para iniciar com o sistema     |
| `systemctl disable nome.service`| Desativa o serviço no boot                     |
| `systemctl is-active nome.service` | Verifica se o serviço está ativo           |
| `systemctl list-units --type=service` | Lista todos os serviços carregados       |

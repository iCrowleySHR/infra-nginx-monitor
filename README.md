# infra-nginx-monitor

Este projeto tem como objetivo configurar uma infraestrutura Linux local capaz de hospedar um servidor web Nginx com uma página HTML simples, garantindo sua alta disponibilidade por meio de verificações automáticas e envio de alertas em caso de falhas.

Proposto pelo programa de bolsa **CompassUOL**.

---

## Distro

O projeto utiliza a **WSL** do Windows com a Distro **Ubuntu**.

<img width="978" height="504" alt="image" src="https://github.com/user-attachments/assets/7ba51088-6174-45f2-89b9-081d2b081a4b" />


---

## Instalação e Configuração do Nginx
**Nginx** é um servidor web, normalmente utilizado para hospedar sites

A instalação e configuração serão feitas usando o usuário `root`. Para acessar esse usuário, utilize o comando abaixo; será solicitada a senha para prosseguir:

### Sintaxe
```bash
su
```

Após a execução, o terminal ficará assim:

<img width="979" height="507" alt="image" src="https://github.com/user-attachments/assets/d524d53a-154b-4e64-b51e-ab061668e810" />

---

Para instalar os pacotes **Nginx**, você utiliza o comando:
### Sintaxe
```bash
apt update
apt upgrade
apt install nginx
```
Você poderá confirmar todas as instalações que o terminal pedir.

<img width="978" height="504" alt="image" src="https://github.com/user-attachments/assets/9fcedf38-9243-4193-8758-7d7da15519c8" />

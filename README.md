# 🔐 Educational Ransomware Project - Python

Este projeto foi desenvolvido como parte de um desafio educacional da [DIO](https://www.dio.me/), com o objetivo de demonstrar, de forma **controlada e ética**, como funciona um ransomware simples em Python, utilizando criptografia simétrica com a biblioteca `cryptography`.

> ⚠️ **ATENÇÃO:** Este projeto é **exclusivamente para fins educacionais** e de estudo. O autor **não se responsabiliza por qualquer uso indevido** ou ilegal deste código.

---

## 🧩 Estrutura do Projeto

- `encrypter.py` – Script responsável por criptografar arquivos.
- `decrypter.py` – Script para descriptografar os arquivos.
- `secret.key` – Arquivo gerado automaticamente que contém a chave secreta usada na criptografia.

---

## 🔧 Como Funciona

### 1. Criptografia (`encrypter.py`)

O script:

- Gera uma chave única (`secret.key`)
- Varre a pasta atual e criptografa todos os arquivos (exceto os próprios scripts e a chave)
- Substitui o conteúdo dos arquivos pelo conteúdo criptografado

### 2. Descriptografia (`decrypter.py`)

O script:

- Lê a chave de `secret.key`
- Descriptografa todos os arquivos criptografados no mesmo diretório
- Restaura os arquivos ao estado original (se a chave for válida)

---

## ▶️ Como Executar

1. Instale a biblioteca necessária:

```bash
pip install cryptography

#!/bin/bash

# Instale as dependências do Python
python3 -m pip install -r requirements.txt

# Inicie o script Python
while true; do
    python3 main.py
    read -p "Pressione Enter para reiniciar..."
done

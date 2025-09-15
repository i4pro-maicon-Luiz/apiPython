# API Meteorológica Flask + Frontend HTML

Este projeto traz uma API em Python (Flask) que consulta dados meteorológicos da [Open-Meteo](https://open-meteo.com/) e uma interface web simples para busca por cidade e estado.

## Pré-requisitos

- Python 3 instalado
- Pip instalado
- Instalar dependências:
  ```
  pip install flask flask-cors requests
  ```

## Como rodar a API

1. Abra o terminal na pasta do projeto.
2. Execute o backend Flask:
   ```
   python app.py
   ```
   O servidor estará disponível em `http://127.0.0.1:5000`.

## Como usar o frontend

1. Abra o arquivo `index.html` em seu navegador.
2. Informe a cidade e o estado (UF) nos campos e clique em **Buscar Tempo**.
3. Os dados meteorológicos serão exibidos em uma tabela estilizada.

## Observações

- O backend utiliza o serviço Nominatim (OpenStreetMap) para converter cidade e estado em latitude/longitude.
- Se não informar cidade e estado, será exibido o tempo padrão de São Paulo/SP.
- O frontend exibe um GIF de carregamento enquanto busca os dados.

---
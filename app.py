# ---------------------------------------------------------------
# API Flask para consulta de dados meteorológicos via Open-Meteo
#
# Explicação linha por linha:
# 1. from flask import Flask, request, jsonify
#    Importa as classes e funções necessárias do Flask para criar a aplicação web, manipular requisições e retornar respostas em JSON.
# 2. import requests
#    Importa a biblioteca requests para fazer requisições HTTP externas.
# 3. from flask_cors import CORS
#    Importa a função CORS para permitir requisições de outros domínios (Cross-Origin Resource Sharing).
# 5. app = Flask(__name__)
#    Cria uma instância da aplicação Flask.
# 6. CORS(app)
#    Ativa o suporte a CORS na aplicação Flask.
# 8. @app.route('/weather')
#    Define uma rota /weather para acessar a função abaixo via HTTP.
# 9. def weather():
#    Define a função que será executada quando a rota /weather for acessada.
# 10. latitude = request.args.get('latitude', '-23.55')
#     Obtém o parâmetro latitude da URL, ou usa -23.55 como padrão.
# 11. longitude = request.args.get('longitude', '-46.63')
#     Obtém o parâmetro longitude da URL, ou usa -46.63 como padrão.
# 12. url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
#     Monta a URL da API externa de previsão do tempo usando os valores de latitude e longitude.
# 13. response = requests.get(url)
#     Faz uma requisição GET para a URL montada.
# 14. if response.status_code == 200:
#     Verifica se a resposta da API foi bem-sucedida (código 200).
# 15. data = response.json()
#     Converte a resposta da API para um objeto Python (JSON).
# 16. return jsonify(data["current_weather"])
#     Retorna os dados do tempo atual em formato JSON para o cliente.
# 17. else:
#     Caso a resposta não seja bem-sucedida...
# 18. return jsonify({"error": "Erro ao buscar dados"}), 500
#     Retorna um erro em JSON com código HTTP 500.
# 20. if __name__ == "__main__":
#     Verifica se o arquivo está sendo executado diretamente.
# 21. app.run(debug=True)
#     Inicia o servidor Flask em modo debug.
# ---------------------------------------------------------------

from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_lat_lon(city, state):
    # Utiliza Nominatim (OpenStreetMap) para buscar latitude e longitude
    url = f"https://nominatim.openstreetmap.org/search?city={city}&state={state}&country=Brazil&format=json"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return data["lat"], data["lon"]
    return None, None

@app.route('/weather')
def weather():
    city = request.args.get('city')
    state = request.args.get('state')
    if city and state:
        latitude, longitude = get_lat_lon(city, state)
        if not latitude or not longitude:
            return jsonify({"error": "Cidade ou estado não encontrados"}), 400
    else:
        latitude = '-23.55'
        longitude = '-46.63'
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data["current_weather"])
    else:
        return jsonify({"error": "Erro ao buscar dados"}), 500

if __name__ == "__main__":
    app.run(debug=True)
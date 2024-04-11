from flask import Flask, jsonify

app = Flask(__name__)

# Lista de nomes
informacoes_pessoais = {
    "Joao": {
        "idade": 30,
        "profissao": "Engenheiro",
        "cidade": "Sao Paulo"
    },
    "Maria": {
        "idade": 25,
        "profissao": "Medica",
        "cidade": "Rio de Janeiro"
    },
    "Pedro": {
        "idade": 35,
        "profissao": "Professor",
        "cidade": "Belo Horizonte"
    },
    "Ana": {
        "idade": 28,
        "profissao": "Advogada",
        "cidade": "Brasilia"
    }
}

@app.route('/backend', methods=['GET'])
def get_informacoes_pessoais():
    return jsonify(informacoes_pessoais)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)



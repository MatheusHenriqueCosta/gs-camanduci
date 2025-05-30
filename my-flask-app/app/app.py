from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/frete', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'frete'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
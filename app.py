from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, mundo! Esta es la página de inicio."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(f"Recibido el webhook con los datos: {data}")
    return jsonify({"message": "¡Webhook recibido exitosamente!"}), 200

if __name__ == '__main__':
    app.run(debug=True)

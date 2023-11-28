from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    data = request.get_json()

    if 'number' in data:
        provided_number = data['number']
        squared_number = provided_number ** 2
        return jsonify({"response": f"Pong! {squared_number}"})
    else:
        return jsonify({"response": "Pong!"})

if __name__ == '__main__':
    app.run(debug=True)


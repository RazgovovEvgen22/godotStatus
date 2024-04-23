from flask import Flask, jsonify, request

app = Flask(__name__)

# Предполагаем, что состояние хранится в памяти сервера, но его можно сохранять и в базу данных
app_state = {'is_running': False}

@app.route('/state', methods=['GET'])
def get_state():
    return jsonify(app_state)

@app.route('/update_state', methods=['POST'])
def update_state():
    global app_state
    new_state = request.json.get('is_running')
    if new_state is not None:
        app_state['is_running'] = new_state
        return jsonify({'message': 'State updated successfully'}), 200
    return jsonify({'message': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')

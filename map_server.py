from flask import Flask, request, jsonify

app = Flask(__name__)
map_data = {'latitude': 0, 'longitude': 0}

@app.route('/update_map', methods=['POST'])
def update_map():
    global map_data
    data = request.json
    map_data['latitude'] = data.get('latitude', map_data['latitude'])
    map_data['longitude'] = data.get('longitude', map_data['longitude'])
    return jsonify({'message': 'Map updated'})

@app.route('/get_map_data', methods=['GET'])
def get_map_data():
    global map_data
    return jsonify(map_data)

if __name__ == '__main__':
    app.run(debug=True)
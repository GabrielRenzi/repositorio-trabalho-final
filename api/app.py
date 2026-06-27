from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# caminho para o JSON dos videos
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'videos.json')

def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# rota 1 para status da aplicação
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"nome": "Streaming Edu API", "versao": "1.0.0", "status": "online"}), 200

# rota 2 para retornar todos os vídeos
@app.route('/videos', methods=['GET'])
def get_videos():
    videos = load_data()
    return jsonify(videos), 200

# rota 3 para retornar vídeo por ID
@app.route('/videos/<int:video_id>', methods=['GET'])
def get_video_by_id(video_id):
    videos = load_data()
    video = next((v for v in videos if v['id'] == video_id), None)
    
    if video:
        return jsonify(video), 200
    else:
        return jsonify({"erro": "Vídeo não encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
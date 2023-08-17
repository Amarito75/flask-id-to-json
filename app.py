from flask import Flask, request, jsonify
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Activate CORS for all routes


@app.route('/', methods=['POST'])
def ajouter_ids_dans_json():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Aucun fichier téléchargé'})

        fichier = request.files['file']
        if fichier.filename == '':
            return jsonify({'error': 'Aucun fichier sélectionné'})

        data = json.load(fichier)

        modified_data = []
        for idx, entry in enumerate(data, start=1):
            entry_dict = {'id': idx, **entry}
            modified_data.append(entry_dict)

        modified_json = json.dumps(modified_data, indent=4)

        return jsonify({'modified_json': modified_json})

    except Exception as e:
        return jsonify({'error': f'Une erreur s\'est produite : {e}'})


if __name__ == '__main__':
    app.run(debug=True)

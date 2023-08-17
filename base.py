# from flask import Flask, request, jsonify, send_file
# import json

# app = Flask(__name__)

# @app.route('/upload', methods=['GET','POST'])
# def ajouter_ids_dans_json():
#     try:
#         if 'file' not in request.files:
#             return jsonify({'error': 'Aucun fichier téléchargé'})

#         fichier = request.files['file']
#         if fichier.filename == '':
#             return jsonify({'error': 'Aucun fichier sélectionné'})

#         data = json.load(fichier)

#         for idx, entry in enumerate(data, start=1):
#             entry_dict = {
#                 'id': idx,
#                 **entry
#             }
#             data[idx - 1] = entry_dict

#         with open('json.json', 'w') as fichier:
#             json.dump(data, fichier, indent=4)
        
#         return jsonify(data)

#     except Exception as e:
#         return jsonify({'error': f'Une erreur s\'est produite : {e}'})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
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


# @app.route('/transform', methods=['POST'])
# def transform_text():
#     try:
#         data = request.json
#         input_text = data.get('text', '')

#         entries = [entry.strip() for entry in input_text.split('\n') if entry.strip()]
#         transformed_entries = []

#         for idx, entry in enumerate(entries, start=1):
#             entry_dict = json.loads(entry)
#             entry_dict['id'] = idx
#             transformed_entries.append(entry_dict)

#         transformed_text = json.dumps(transformed_entries, indent=4)

#         return jsonify({'transformed_text': transformed_text})

#     except Exception as e:
#         return jsonify({'error': f'Une erreur s\'est produite : {e}'})    

    
if __name__ == '__main__':
    app.run(debug=True)

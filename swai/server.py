from flask import Flask, render_template, request, jsonify
from SWAI import GenerateStudyMaterial

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    data = "hello!"
    return jsonify(data), 200

@app.route('/data', methods = ['GET', 'POST'])
@app.route('/aiQuery', methods = ['GET', 'POST'])

def data():
    if request.method == 'POST':
        data = request.json
        return jsonify({"message": "Data added successfully!"}), 200
    elif request.method == 'GET':
        generator = GenerateStudyMaterial("", "multiple choice question", "https://cdn.discordapp.com/attachments/729700899005661215/1222225216630034532/WIN_20240326_09_46_13_Pro.jpg?ex=661570ef&is=6602fbef&hm=2747b276a63a43568fcc38365f04dd5b8a5f4bccdc0df91ec24bf2caa1305b72&")
        # question, answer = generator.generateQuestion()
        
        question, answer = generator.generateQuestionFromImage()

        data = question + answer
        return jsonify(data), 200
    
def aiQuery():
    if request.method == "GET":
        # Example: Process AI query here
        query = request.json.get('query')
        # Example response
        response = {'query': query, 'response': 'AI response goes here'}
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug = True)
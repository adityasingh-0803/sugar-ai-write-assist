from flask import Flask, request, jsonify
from grammar_tool import correct_grammar
from suggestion import suggest_next_sentence

app = Flask(__name__)

@app.route('/correct', methods=['POST'])
def correct():
    data = request.get_json()
    text = data.get("text", "")
    corrected = correct_grammar(text)
    return jsonify({"original": text, "corrected": corrected})

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    prompt = data.get("text", "")
    suggestion = suggest_next_sentence(prompt)
    return jsonify({"prompt": prompt, "suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)

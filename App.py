from flask import Flask, request, jsonify

app = Flask(__name__)

# List of bad words
BAD_WORDS = ["badword1", "badword2", "badword3"]

@app.route('/highlight', methods=['POST'])
def highlight_bad_words():
    data = request.json
    text = data.get("text", "")
    
    for word in BAD_WORDS:
        if word in text:
            text = text.replace(word, f"<span class='highlight'>#{word}</span>")
    
    return jsonify({"highlighted_text": text})

if __name__ == '__main__':
    app.run(debug=True)

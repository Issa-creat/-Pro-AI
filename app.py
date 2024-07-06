from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# تحميل نموذج اللغة العربية
nlp = spacy.load("ar_core_news_sm")

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    text = data['text']
    
    # تحليل النص باستخدام spaCy
    doc = nlp(text)
    
    total_amount = 0
    
    # استخراج الأرقام بعد كلمة "ب" أو "ريال"
    for token in doc:
        if token.text == 'ب' or token.text == 'ريال':
            if token.nbor().like_num:
                total_amount += int(token.nbor().text)
    
    return jsonify({'total_amount': total_amount})

if __name__ == '__main__':
    app.run(debug=True)

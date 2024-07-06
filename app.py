from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# تحميل نموذج جاهز لتحليل النصوص
nlp = pipeline("ner", model="dslim/bert-base-NER")

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    text = data['text']
    
    # تحليل النص باستخدام النموذج
    result = nlp(text)
    
    # استخراج الأرقام بعد كلمة "ب" أو "ريال"
    total_amount = sum(int(entity['word']) for entity in result if entity['entity'] == 'MONEY')
    
    return jsonify({'total_amount': total_amount})

if __name__ == '__main__':
    app.run(debug=True)

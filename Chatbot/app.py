from flask import Flask, request, jsonify
from pyngrok import ngrok
from model import FAQBot

app = Flask(__name__)
bot = FAQBot()

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the FAQ Chatbot API. Use POST to /chat with {'question': 'your question', 'lang': 'ar' or 'en'}"})

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return '''
        <html>
        <body>
        <h1>FAQ Chatbot Test</h1>
        <form method="post">
        Question: <input type="text" name="question"><br>
        Language: <select name="lang">
        <option value="ar">Arabic</option>
        <option value="en">English</option>
        </select><br>
        <input type="submit">
        </form>
        </body>
        </html>
        '''
    
    data = request.get_json() if request.is_json else request.form
    user_input = data.get('question', '').strip()
    lang = data.get('lang', '').strip().lower()
    if lang not in {"ar", "en"}:
        lang = bot.detect_language(user_input)
    
    if not user_input:
        return jsonify({"error": "No question provided"}), 400
    
    results = bot.find_similar(user_input, top_k=5)
    
    if not results:
        msg = "عذرًا، لم أجد إجابة مناسبة. حاول إعادة صياغة السؤال." if lang == "ar" else "Sorry, I couldn't find a suitable answer. Please try rephrasing your question."
        return jsonify({"message": msg})

    response = [
        {
            "question": result["question"],
            "answer": result["answer"],
            "similarity": round(result["similarity"], 2)
        }
        for result in results
        if (lang == "ar" and result['lang'] == 'ar') or (lang == "en" and result['lang'] == 'en')
    ]

    if response:
        return jsonify({"results": response})

    fallback = results[0]
    msg = "لا توجد نتائج باللغة المختارة، إليك أفضل إجابة بلغة أخرى." if lang == "ar" else "No results in the selected language; here is the best alternative answer."
    return jsonify({
        "message": msg,
        "fallback": {
            "question": fallback["question"],
            "answer": fallback["answer"],
            "similarity": round(fallback["similarity"], 2)
        }
    })

if __name__ == '__main__':
    # تشغيل ngrok للوصول العام
    ngrok.set_auth_token("3CqiGMh0OGQR6cPIoY6UEyVm4xI_3FFJTR8EDXLhSjmjPZTd3")  # Replace with your token
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")
    
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
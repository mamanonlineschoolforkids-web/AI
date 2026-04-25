from flask import Flask, request, jsonify
from pyngrok import ngrok
from model import FAQBot

app = Flask(__name__)
bot = FAQBot()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
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
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")
    
    app.run(host='0.0.0.0', port=5000)
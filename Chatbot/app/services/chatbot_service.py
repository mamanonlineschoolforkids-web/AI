from model.faq_bot import FAQBot

bot = FAQBot()

def get_response(user_input: str):
    
    # 🔥 detect language تلقائي
    lang = bot.detect_language(user_input)

    results = bot.find_similar(user_input)

    if not results:
        return {"message": "No answer found"}

    # فلترة حسب اللغة
    filtered = [r for r in results if r["lang"] == lang]

    if filtered:
        return filtered
    else:
        return [results[0]]
def detect_language(text: str) -> str:
    return "ar" if any("\u0600" <= c <= "\u06FF" for c in text) else "en"
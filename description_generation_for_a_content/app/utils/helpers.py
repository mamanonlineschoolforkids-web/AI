import re
import os


# ---------- Clean Text ----------
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^ء-يA-Za-z0-9 .,!?]', '', text)
    return text.strip()


# ---------- Split Text ----------
def split_text(text, max_words=200):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]


# ---------- Create Temp Path ----------
def get_temp_path(filename):
    return os.path.join("temp", filename)
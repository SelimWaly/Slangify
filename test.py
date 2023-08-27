import langid

def detect_language(text):
    try:
        detected_lang, _ = langid.classify(text)
        return detected_lang
    except:
        return "Unable to detect language"

if __name__ == "__main__":
    while True:
        user_input = input("Enter text: ")
        detected_language = detect_language(user_input)
        print(f"The detected language is: {detected_language}")

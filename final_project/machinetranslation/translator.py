from googletrans import Translator

def english_to_french(english_text):
    """
    Translates English text to French.

    :param english_text: The text in English to be translated.
    :return: The translated text in French, or None if translation fails.
    """
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(english_text, src='en', dest='fr')
    french_text = translation.text
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.

    :param french_text: The text in French to be translated.
    :return: The translated text in English, or None if translation fails.
    """
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(french_text, src='fr', dest='en')
    english_text = translation.text
    return english_text

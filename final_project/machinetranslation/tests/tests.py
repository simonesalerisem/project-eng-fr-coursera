from ..machinetranslation import translator

def test_english_to_french():
    english_text = "Hi"
    expected_french_text = "Salut"
    french_text = translator.english_to_french(english_text)
    print(french_text)
    assert french_text == expected_french_text

def test_french_to_english():
    french_text = "Salut"
    expected_english_text = "Hi"
    english_text = translator.french_to_english(french_text)
    print(english_text)
    assert english_text == expected_english_text

# Run the tests
test_english_to_french()
test_french_to_english()
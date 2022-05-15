from googletrans import Translator
translator = Translator()
out = translator.translate('Plum', dest='pl').text
print(out)
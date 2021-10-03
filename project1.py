from translate import Translator

T=Translator(
    from_lang="German",to_lang="Italian"
)

user_input=input("Enter a Sentence:")

translated_sentence=T.translate(user_input)

print(translated_sentence)
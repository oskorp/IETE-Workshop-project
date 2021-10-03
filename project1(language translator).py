#Language translator 
#imported translate module 
from translate import Translator

#created variable T which convert tect from one language to another language
T=Translator(
    from_lang="German",to_lang="Italian"
)

#created variable for user input
user_input=input("Enter a Sentence:")

#created variable that convert user input to other langauge
translated_sentence=T.translate(user_input)

#print the translated text
print(translated_sentence)

"'Module to interface with Watson'"

import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator )
language_translator.set_service_url(url)

def translate(input_text, lang):
    "'Wrapper method to handle the translation step'"
    if input_text=='':
        return ''
    response=language_translator.translate(text=input_text,model_id=lang).get_result()
    # Parse response from: { translations: [ {translation:'response text'... }   ]}
    return_text = response['translations'][0]['translation']
    return return_text

def englishToFrench(english_text):
    "'Interface method to handle the specific translation case'"
    french_text = translate(english_text, 'en-fr')
    return french_text

def frenchToEnglish(french_text):
    "'Interface method to handle the specific translation case'"
    english_text = translate(french_text, 'fr-en')
    return english_text

#print(englishToFrench('hello'))
#print(frenchToEnglish('bonjour'))

#translation = language_translator.translate(
#    text='Hello, how are you today?',
#    model_id='en-fr').get_result()
#print(json.dumps(translation, indent=2, ensure_ascii=False))

""" This code is for translation """
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('4QgW948br6jpbuqWS_SSy4ZLmJ-dMWyNOSx7V3TSdwUl')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/'\
    'instances/f76a44ba-60a8-41ad-b024-88874e9c5c09')

languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

def english_to_french(english_text):
    """Translation from English to French"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #french_text=json.dumps(translation, indent=2, ensure_ascii=False)
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translation from French to English"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    #english_text=json.dumps(translation, indent=2, ensure_ascii=False)
    english_text=translation['translations'][0]['translation']
    return english_text

#print(english_to_french("Hello"))
#print(french_to_english("Bonjour"))

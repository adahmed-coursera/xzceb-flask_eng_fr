"""Module that connect to IBM Language Translator to provide text translation
languages translation available in this module:
1- English to French
2- French to English
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()


APIKEY = os.environ['apikey']
URL = os.environ['url']
authenticator = IAMAuthenticator(f'{APIKEY}')
language_translator = LanguageTranslatorV3(version='2018-05-01',
authenticator=authenticator)
language_translator.set_service_url(f'{URL}')

def english_to_french(englishtext):
    """function that take english text and translate it into french text

    Args:
        englishText (_type_): _description_

    Returns:
        str: frenchText
    """
    try:
        translation = language_translator.translate(
        text=englishtext,model_id='en-fr').get_result()
        frenchtext = translation.get('translations')[0]['translation']
        return frenchtext
    except ApiException as ex:
        return ex.message

def french_to_english(frenchtext):
    """function that take french text and translate it into english text

    Args:
        frenchText

    Returns:
        str: englishText
    """
    try:
        translation = language_translator.translate(
        text=frenchtext,model_id='fr-en').get_result()
        englishtext = translation.get('translations')[0]['translation']
        return englishtext
    except ApiException as ex:
        return ex.message

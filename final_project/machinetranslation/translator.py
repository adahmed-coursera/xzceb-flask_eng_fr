"""Module that connect to IBM Language Translator to provide text translation
languages translation available in this module:
1- English to French
2- French to English
"""
import os
import json
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import warnings;
warnings.simplefilter('ignore')
from dotenv import load_dotenv
load_dotenv()


apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']
authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(version=f'{version}',authenticator=authenticator)
language_translator.set_service_url(f'{url}')


def englishToFrench(englishtext):
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

def frenchToEnglish(frenchtext):
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

import os
import logging
from gtts import gTTS

def generate_speech(text, language, shloka_id):
    """
    Generate speech using Google Text-to-Speech
    
    Args:
        text (str): The text to convert to speech
        language (str): The language of the text (english, hindi, marathi, kannada)
        shloka_id (str): ID of the shloka for file naming
    
    Returns:
        str: Path to the generated audio file
    """
    try:
        # Map our language options to gTTS language codes
        language_map = {
            'english': 'en',
            'hindi': 'hi',
            'marathi': 'mr',
            'kannada': 'kn'
        }
        
        # Get the correct language code
        lang_code = language_map.get(language, 'en')
        
        # Create filename
        filename = f"{shloka_id}_{language}.mp3"
        filepath = os.path.join(os.getcwd(), 'temp', filename)
        
        # Generate speech
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(filepath)
        
        logging.info(f"Generated speech audio saved to {filepath}")
        return filepath
        
    except Exception as e:
        logging.error(f"Error generating speech: {str(e)}")
        raise e
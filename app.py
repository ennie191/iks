import os
import logging
from flask import Flask, render_template, jsonify, request, send_file
from utils.tts import generate_speech
from data.shlokas import get_shlokas

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page with all shlokas"""
    try:
        # Get all shlokas categorized from the data module
        categories = get_shlokas()
        return render_template('index.html', categories=categories)
    except Exception as e:
        logging.error(f"Error loading index page: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    """Generate audio explanation for a shloka in the selected language"""
    try:
        # Get request data
        data = request.get_json()
        shloka_id = data.get('shlokaId')
        language = data.get('language')
        
        if not shloka_id or not language:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        # Find the shloka and its explanation in the selected language
        categories = get_shlokas()
        explanation_text = None
        
        for category in categories:
            for shloka in category['shlokas']:
                if shloka['id'] == shloka_id:
                    explanation_text = shloka['explanations'].get(language)
                    break
            if explanation_text:
                break
        
        if not explanation_text:
            return jsonify({'error': f'No explanation found for shloka {shloka_id} in {language}'}), 404
        
        # Generate audio file
        audio_path = generate_speech(explanation_text, language, shloka_id)
        
        # Extract filename from path
        filename = os.path.basename(audio_path)
        
        return jsonify({
            'success': True,
            'audioUrl': f'/audio/{filename}',
            'message': f'Generated audio for {language} explanation'
        })
    
    except Exception as e:
        logging.error(f"Error generating audio: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/audio/<filename>')
def serve_audio(filename):
    """Serve the generated audio files"""
    try:
        # The audio files will be stored in a temporary directory
        filepath = os.path.join(os.getcwd(), 'temp', filename)
        
        # Set the appropriate mimetype based on file extension
        mimetype = 'audio/mpeg' if filename.endswith('.mp3') else 'audio/wav'
        return send_file(filepath, mimetype=mimetype)
    except Exception as e:
        logging.error(f"Error serving audio file: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Create temp directory for audio files if it doesn't exist
if not os.path.exists(os.path.join(os.getcwd(), 'temp')):
    os.makedirs(os.path.join(os.getcwd(), 'temp'))
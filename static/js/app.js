document.addEventListener('DOMContentLoaded', function() {
    // Current shloka ID for audio generation
    let currentShlokaId = null;
    
    // Audio buttons click handlers
    document.querySelectorAll('.audio-btn').forEach(button => {
        button.addEventListener('click', function() {
            currentShlokaId = this.dataset.shlokaId;
            const languageModal = new bootstrap.Modal(document.getElementById('languageModal'));
            languageModal.show();
        });
    });
    
    // Language selection handlers
    document.querySelectorAll('.language-btn').forEach(button => {
        button.addEventListener('click', function() {
            const language = this.dataset.language;
            
            // Close language modal
            bootstrap.Modal.getInstance(document.getElementById('languageModal')).hide();
            
            // Show audio modal with loading state
            const audioModal = new bootstrap.Modal(document.getElementById('audioModal'));
            resetModalState();
            audioModal.show();
            
            // Generate the audio file
            generateAudio(currentShlokaId, language);
        });
    });
    
    // Function to generate audio for selected shloka and language
    function generateAudio(shlokaId, language) {
        // Show loading state
        document.getElementById('loading-spinner').classList.remove('d-none');
        document.getElementById('audio-player-container').classList.add('d-none');
        document.getElementById('error-message').classList.add('d-none');
        
        // Update modal title
        document.getElementById('audioModalLabel').textContent = 
            `Listening to ${language.charAt(0).toUpperCase() + language.slice(1)} Explanation`;
        
        // Make API request to generate audio
        fetch('/generate-audio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                shlokaId: shlokaId,
                language: language
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            
            // Hide spinner, show audio player
            document.getElementById('loading-spinner').classList.add('d-none');
            document.getElementById('audio-player-container').classList.remove('d-none');
            
            // Set audio source and play
            const audioPlayer = document.getElementById('audio-player');
            audioPlayer.src = data.audioUrl;
            audioPlayer.load();
            audioPlayer.play();
        })
        .catch(error => {
            // Hide spinner, show error
            document.getElementById('loading-spinner').classList.add('d-none');
            const errorElement = document.getElementById('error-message');
            errorElement.textContent = `Error: ${error.message}`;
            errorElement.classList.remove('d-none');
            console.error('Error generating audio:', error);
        });
    }
    
    // Reset modal state between uses
    function resetModalState() {
        document.getElementById('loading-spinner').classList.remove('d-none');
        document.getElementById('audio-player-container').classList.add('d-none');
        document.getElementById('error-message').classList.add('d-none');
        document.getElementById('audioModalLabel').textContent = 'Listening to Explanation';
    }
});
import os
from pocketsphinx import LiveSpeech, get_model_path
from logging_module import log

# Placeholder for the message handler function, set by main_controller.py
message_handler = None

def set_message_handler(handler):
    global message_handler
    message_handler = handler

def setup_keyword_detection():
    model_path = get_model_path()
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    kws_path = os.path.join(script_dir, 'keywords.kws')  # Path to your keywords.kws file

    log('info', f"Model Path: {model_path}")
    log('info', f'Model Path: {model_path}')
    log('info', f'Keywords File Path: {kws_path}')
    log('info', f'Keywords File Path: {kws_path}')

    try:
        speech = LiveSpeech(
            verbose=False,  # Set to True for detailed logs from PocketSphinx
            sampling_rate=16000,
            buffer_size=256,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(model_path, 'en-us/en-us'),
            lm=None,
            kws=kws_path
        )
        log('info', 'PocketSphinx initialized successfully.')
        log('info', 'Listening for keywords...')
    except Exception as e:
        log('error', f'Failed to initialize PocketSphinx: {e}')
        return

    for phrase in speech:
        detected_words = [seg[0] for seg in phrase.segments(detailed=True)]
        log('info', f'Detected words: {detected_words}')  # Extract words
        log('info', f'Detected words: {detected_words}')  # Log for debugging
        
        # If a message handler is set, call it with the detected words
        if message_handler:
            message_handler(detected_words)

if __name__ == "__main__":
    setup_keyword_detection()
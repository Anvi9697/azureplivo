from flask import Flask, request
app = Flask(__name__)
@app.route('/answer', methods=['GET'])
def stream_audio_to_whispe1r(word=''):
    if word =='':
        word = request.args.get('word') 
    print(word)
    return 'hello world'
stream_audio_to_whispe1r('hiii')
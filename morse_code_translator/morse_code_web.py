from flask import Flask, request, render_template

alphabet_to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

morse_to_alphabet = {v: k for k, v in alphabet_to_morse.items()}

app = Flask(__name__)

def translate_to_morse(text):
    output = ''
    for character in text:
        if character.lower() in alphabet_to_morse:
            output += alphabet_to_morse[character.lower()] + ' '
        else:
            output += ' '
    return output.strip()
    

def translate_to_text(morse_code):
    morse_words = morse_code.split('/')
    output = ''
    for morse_word in morse_words:
        morse_characters = morse_word.split()
        for morse_character in morse_characters:
            if morse_character in morse_to_alphabet:
                output += morse_to_alphabet[morse_character]
            else:
                output += '?'
        output += ' '
    return output.strip()

@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        input_text = request.form.get('input', '')  
        if '-' in input_text or '.' in input_text:
            dynamic_data = translate_to_text(input_text)
        else:
            dynamic_data = translate_to_morse(input_text)
        return render_template("index.html", dynamic_data=dynamic_data) 
    return render_template("index.html", dynamic_data="")

if __name__ == "__main__":
    app.run()
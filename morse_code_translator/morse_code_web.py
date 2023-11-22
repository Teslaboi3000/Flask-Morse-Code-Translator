from flask import Flask, request
from flask import render_template

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
def morse_translation():
    if request.method == 'POST':
        input_text = request.form['input']
        if '-' in input_text or '.' in input_text:
            output = translate_to_text(input_text)
        else:
            output = translate_to_morse(input_text)
        return """
            <h1>Welcome to Maxjustuniversal's and Teslaboi's Morse Code Translator!<h1>
            <form method="post">
            <label for="input">Enter text or Morse code:</label><br>
            <input type="text" id="input" name="input" value="{}"><br>
            <input type="submit" value="Translate">
            </form>
            <p>{}</p>    
        """.format(input_text, output)
    return """
    <h1>Welcome to Maxjustuniversal's and Teslaboi's Morse Code Translator!<h1>
    <form method="post">
        <label for="input">Enter text or Morse code:</label><br>
        <input type="text" id="input" name="input"><br>
        <input type="submit" value="Translate">
    </form>
    """

if __name__ == "__main__":
    app.run()
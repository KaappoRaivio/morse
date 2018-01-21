import subprocess, time

speed = 30

class Morse(object):
    morsechars  = {
                      '0': '-----',
                      '1': '.----',
                      '2': '..---',
                      '3': '...--',
                      '4': '....-',
                      '5': '.....',
                      '6': '-....',
                      '7': '--...',
                      '8': '---..',
                      '9': '----.',
                      'a': '.-',
                      'b': '-...',
                      'c': '-.-.',
                      'd': '-..',
                      'e': '.',
                      'f': '..-.',
                      'g': '--.',
                      'h': '....',
                      'i': '..',
                      'j': '.---',
                      'k': '-.-',
                      'l': '.-..',
                      'm': '--',
                      'n': '-.',
                      'o': '---',
                      'p': '.--.',
                      'q': '--.-',
                      'r': '.-.',
                      's': '...',
                      't': '-',
                      'u': '..-',
                      'v': '...-',
                      'w': '.--',
                      'x': '-..-',
                      'y': '-.--',
                      'z': '--..',
                      '.': '.-.-.-',
                      ',': '--..--',
                      '?': '..--..',
                      '!': '-.-.--',
                      '-': '-....-',
                      '/': '-..-.',
                      '@': '.--.-.',
                      '(': '-.--.',
                      ')': '-.--.-'
                    }

    def __init__(self, string):
        self.string = string
        self.chars = list(self.string)
        self.morse_chars = Morse.MorseChar(self.chars)

    def MorseChar(self):
        morse_chars = []
        for i in self:
            morse_chars.append(Morse.morsechars[i])
        return morse_chars

    def PlayMorse(self):
        for i in self.morse_chars:
            for a in list(i):
                if a == '.':
                    pulse_length = 1 / speed
                elif a == '-':
                    pulse_length = 3 / speed
                else:
                    raise Exception('Fatal: not a morse character.')
                sound(1000, pulse_length, 128000)
                time.sleep(5 / speed)
            time.sleep(2 / speed)

def sound(frequency, length, bitrate):
    python3_command = 'python2 sound.py {} {} {}'.format(frequency, length, bitrate)  # launch your python2 script using bash
    process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()  # receive output from the python2 script
    if output != None or error != None:
        return output, error

user_input = input('string: ').lower()
chartest = Morse(user_input)
print(chartest.morse_chars)
chartest.PlayMorse()

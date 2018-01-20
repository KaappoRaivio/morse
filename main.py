import subprocess

class MorseCharacter(object):
    morsechars  = {
                      "0": "-----",
                      "1": ".----",
                      "2": "..---",
                      "3": "...--",
                      "4": "....-",
                      "5": ".....",
                      "6": "-....",
                      "7": "--...",
                      "8": "---..",
                      "9": "----.",
                      "a": ".-",
                      "b": "-...",
                      "c": "-.-.",
                      "d": "-..",
                      "e": ".",
                      "f": "..-.",
                      "g": "--.",
                      "h": "....",
                      "i": "..",
                      "j": ".---",
                      "k": "-.-",
                      "l": ".-..",
                      "m": "--",
                      "n": "-.",
                      "o": "---",
                      "p": ".--.",
                      "q": "--.-",
                      "r": ".-.",
                      "s": "...",
                      "t": "-",
                      "u": "..-",
                      "v": "...-",
                      "w": ".--",
                      "x": "-..-",
                      "y": "-.--",
                      "z": "--..",
                      ".": ".-.-.-",
                      ",": "--..--",
                      "?": "..--..",
                      "!": "-.-.--",
                      "-": "-....-",
                      "/": "-..-.",
                      "@": ".--.-.",
                      "(": "-.--.",
                      ")": "-.--.-"
                    }

    def __init__(self, char):
        self.char = char
    def morseChar(self):
        return MorseCharacter.morsechars[]


def sound(frequency, length, bitrate):
    python3_command = "python2 sound.py {} {} {}".format(frequency, length, bitrate)  # launch your python2 script using bash

    process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()  # receive output from the python2 script
    if output != None or error != None:
        return output, error
chartest = MorseCharacter('a')
print(chartest.morseChar())

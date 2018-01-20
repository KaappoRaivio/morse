import math
import pyaudio
import sys

PyAudio = pyaudio.PyAudio

frequency = int(sys.argv[1]) * 2
length = int(sys.argv[2])
bitrate = int(sys.argv[3])
if 2 * frequency > bitrate:
    bitrate = frequency+100

NUMBEROFFRAMES = int(bitrate * length)
RESTFRAMES = NUMBEROFFRAMES % bitrate
WAVEDATA = ''

#generating wawes
for i in range(NUMBEROFFRAMES):
    WAVEDATA = WAVEDATA + chr(int(math.sin(i / ((bitrate / frequency) / math.pi)) * 127 + 128))

for i in range(RESTFRAMES):
    WAVEDATA = WAVEDATA + chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = bitrate,
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()

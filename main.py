import numpy as np
import matplotlib.pyplot as plt
import time
import sys
# from scipy.signal import find_peaks, peak_widths
from scipy.io.wavfile import write
import random
import sounddevice as sd
import soundfile as sf
import datetime
sd.default.device = 0

fs = 48000  # frequency
chno = 2  # no of channels
duration = 2


def rem_empty(wave):
    wave2 = wave.astype('int32')
    return [np.array(wave),-np.array(wave),np.bitwise_xor(np.array(wave2),-np.array(wave2))]

def rem_empty_2(wave):
    return np.array([x for x in wave if x != 0.0])

def open_wav():
    data, fs = sf.read("test.wav", dtype='float32')
    return rem_empty(data)

def wave_peaker(data, fn):
    plt.plot(data)
    plt.savefig("{}.png".format(fn))
    write('{}.wav'.format(fn), fs, data)

def main():
    temp = open_wav()
    print(temp)
    wave_peaker(temp[0],"orig")
    wave_peaker(temp[1],"neg")
    wave_peaker(temp[2],"xr")


main()


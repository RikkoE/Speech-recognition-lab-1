# DT2118, Lab 1 Feature Extraction
# Functions to be implemented ----------------------------------

import scipy.signal as sig
import scipy.fftpack as ft
import tools
import numpy as np 

def enframe(samples, winlen, winshift):
    """
    Slices the input samples into overlapping windows.

    Args:
        winlen: window length in samples.
        winshift: shift of consecutive windows in samples
    Returns:
        numpy array [N x winlen], where N is the number of windows that fit
        in the input signal
    """

    prev = 0
    nxt = int(winlen)               # 400 samples in one frame (20 ms)

    step = int(winshift)    # 200 samples per step (10 ms)

    num_frames = int(((samples.size - winshift) // winlen) * 2)  # 80 frames fit in the signal

    print num_frames
    print samples.shape

    result = np.zeros(shape=(num_frames,winlen))

    for i in range(0,num_frames):
        result[i] = samples[prev:nxt]
        prev += step
        nxt += step

    return result

def preemp(inp, p=0.97):
    """
    Pre-emphasis filter.

    Args:
        input: array of speech frames [N x M] where N is the number of frames and
               M the samples per frame
        p: preemhasis factor (defaults to the value specified in the exercise)

    Output:
        output: array of pre-emphasised speech samples
    Note (you can use the function lfilter from scipy.signal)
    """

    np.set_printoptions(suppress=True)

    b = np.array([1,-p])
    a = np.array([1])

    filtered_signal = sig.lfilter(b, a, inp)

    return filtered_signal


def windowing(inp):
    """
    Applies hamming window to the input frames.

    Args:
        input: array of speech samples [N x M] where N is the number of frames and
               M the samples per frame
    Output:
        array of windowed speech samples [N x M]
    Note (you can use the function hamming from scipy.signal, include the sym=0 option
    if you want to get the same results as in the example)
    """

    M = 400

    winfunc = sig.hamming(M, sym = False)

    win = inp * winfunc

    return win

def powerSpectrum(inp, nfft):
    """
    Calculates the power spectrum of the input signal, that is the square of the modulus of the FFT

    Args:
        input: array of speech samples [N x M] where N is the number of frames and
               M the samples per frame
        nfft: length of the FFT
    Output:
        array of power spectra [N x nfft]
    Note: you can use the function fft from scipy.fftpack
    """

    spec = ft.fft(inp, nfft)

    spec = abs(spec)**2

    return spec

def logMelSpectrum(inp, samplingrate):
    """
    Calculates the log output of a Mel filterbank when the input is the power spectrum

    Args:
        input: array of power spectrum coefficients [N x nfft] where N is the number of frames and
               nfft the length of each spectrum
        samplingrate: sampling rate of the original signal (used to calculate the filterbanks)
    Output:
        array of Mel filterbank log outputs [N x nmelfilters] where nmelfilters is the number
        of filters in the filterbank
    Note: use the trfbank function provided in tools.py to calculate the filterbank shapes and
          nmelfilters
    """



    trf = tools.trfbank(samplingrate, 512)

    res = np.dot(inp, trf.T)

    res = np.log10(res)

    return res

def cepstrum(inp, nceps):
    """
    Calulates Cepstral coefficients from mel spectrum applying Discrete Cosine Transform

    Args:
        input: array of log outputs of Mel scale filterbank [N x nmelfilters] where N is the
               number of frames and nmelfilters the length of the filterbank
        nceps: number of output cepstral coefficients
    Output:
        array of Cepstral coefficients [N x nceps]
    Note: you can use the function dct from scipy.fftpack.realtransforms
    """

    cosine = ft.dct(inp, norm = 'ortho')

    res = cosine[:,0:nceps]

#    res = tools.lifter(res)

    return res

def dtw(localdist):
    """Dynamic Time Warping.

    Args:
        localdist: array NxM of local distances computed between two sequences
                   of length N and M respectively

    Output:
        globaldist: scalar, global distance computed by Dynamic Time Warping
    """

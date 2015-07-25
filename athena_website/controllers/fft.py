#!/usr/bin/env python

import numpy

#computes 1D fft
def fftcompute(data):
    #print(data)
    result = numpy.fft.fft(data,32)
    #print(result)
    return result

#computes 2D fft
def fft2compute(data):
    result = numpy.fft.fft2(data,32)
    return result

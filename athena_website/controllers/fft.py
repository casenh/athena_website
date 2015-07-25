#!/usr/bin/env python

import numpy

def fftcompute(data):
    print(data)
    result = numpy.fft.fft(data,32)
    print(result)
    return result

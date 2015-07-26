import numpy as np

def processFFT(byteMe):
    fftOut = np.fft.fft(byteMe, 32)
    Mean = fftOut[0]
    fftOut[0] = 0 
    return (fftOut, Mean)
    
def func(a, b, c):
    mag = (np.absolute(a) ** 2 + np.absolute(b) ** 2 + np.absolute(c) ** 2) ** 0.5
    return mag    
    
def main():
    sum2nd = 0
    array = np.genfromtxt("someData.csv", delimiter = ",")
    dummyfftOut = func(processFFT(array[:,0])[0], processFFT(array[:,1])[0], processFFT(array[:,2])[0])  
    dummyMean = func(processFFT(array[:,0])[1], processFFT(array[:,1])[1], processFFT(array[:,2])[1])
    x = type (dummyfftOut)
    for i in range (32):
        if i >= 16 and i < 32:
            sum2nd += dummyfftOut[i]
    print (dummyfftOut, dummyMean)
    print sum2nd

main()
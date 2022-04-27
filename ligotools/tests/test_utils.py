import numpy as np
import os
import fnmatch
from scipy.io import wavfile
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from ligotools import readligo as rl 

#def test_whiten():

#def test_write_wavfile():
#	
#def test_reqshift():
#	
#def test_plot_det():
#	assert 
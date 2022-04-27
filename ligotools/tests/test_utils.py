import matplotlib
matplotlib.use('Agg')
import numpy as np
import h5py
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
from ligotools import utils as ut 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from ligotools import readligo as rl
from os.path import exists
from os import remove
import os

def test_whiten():
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
	time = time_H1
	dt = time[1] - time[0]
	fs = 4096
	NFFT = 4*fs
	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
	psd_H1 = interp1d(freqs, Pxx_H1)
	
	assert ut.whiten(strain_H1,psd_H1,dt)[1] == -307.1400565342336	
	
def test_write_wavfile():
	ut.write_wavfile("audio/test.wav", 10, np.array([1,0,-1,-1.3,-1.9,-0.5]))
	assert exists("audio/test.wav")
	remove("audio/test.wav")
	
def test_reqshift():
	assert np.sum(ut.reqshift(np.arange(0,100,0.5), 400, 4096)) == -2.4158453015843406e-13
	
def test_plot():
	det = "L1"
	time = np.arange(1000,5000, 2)
	SNR = np.arange(1, 5, 0.002)
	template_match = np.arange(1, 5, 0.002)
	eventname = "temp"
	plottype = 'png'
	tevent = 2502
	template_fft = np.arange(1020,5020, 2)
	datafreq = np.arange(1, 5, 0.002)
	d_eff = 100
	freqs = np.random.uniform(1, 40, 400)
	data_psd = np.arange(2000, 4000, 5)
	strain_H1_whitenbp = np.random.uniform(1, 500, 2000)
	fs = 4000
	strain_L1_whitenbp = np.random.uniform(1, 500, 2000)
	ut.plot_det(1, "L1", time, 5000, SNR, template_match, eventname, plottype, tevent,       template_fft, strain_L1_whitenbp, datafreq, d_eff, freqs, data_psd, strain_H1_whitenbp, fs)
	plot_path = "figures/" + eventname + "_" + det + "_" + "matchfreq." + plottype
	assert os.path.exists(plot_path)
	os.remove(plot_path)

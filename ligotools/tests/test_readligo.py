from ligotools import readligo as rl
import numpy as np
import json

def test_read_hdf5():
    assert len(rl.read_hdf5("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", True)) == 7

def test_loaddata():
    assert len(rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")[1]) == 131072

def test_dq2segs():
    channel_dict = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")[2]
    assert rl.dq2segs(channel_dict['CBC_CAT3'], 0).__class__ == rl.SegmentList

def test_dq_channel_to_seglist():
    channel = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")[2]
    assert np.array_equal(rl.dq_channel_to_seglist(channel['CBC_CAT3']), [slice(0,131072,None)])
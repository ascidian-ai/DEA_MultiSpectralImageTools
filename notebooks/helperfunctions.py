import os
import time
import sys
import pickle

######################################################################
# Begin Timer
#---------------------------------------------------------------------
# Returns current time as seconds since beginning of epoch.
def begin_timer(info=True):
    stime = time.time()
    stime_f = time.ctime(stime)
    if info: print('[ Begin timer at %s ]'%(stime_f))
    return stime

######################################################################
# End Timer
#---------------------------------------------------------------------
# Takes start time from begin_timer() function as input.
# Returns end time as seconds since beginning of epoch.
# Returns duration between start and end time in seconds.
def end_timer(stime, info=True):
    etime = time.time()
    durn = etime - stime
    etime_f = time.ctime(etime)
    if info: print('[ End timer at   %s | Duration: %f s ]'%(etime_f,durn))
    return etime, durn

######################################################################
# Save dataset
#---------------------------------------------------------------------
# Saves a data structure in a binary file in pickle format.
# Takes absolute or relative path to file as input.
# Takes data structure as input.
def saveDataset(filepath, dataset):
    with open(filepath, 'wb') as f: pickle.dump(dataset, f)
    return None

######################################################################
# Load dataset
#---------------------------------------------------------------------
# Loads a data structure from a binary file in pickle format.
# Takes absolute or relative path to file as input.
# Returns data structure from file.
def loadDataset(filepath):
    with open(filepath, 'rb') as f:
        dataset = pickle.load(f)
    return dataset

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:23:44 2018

@author: willy
"""

import os
import re
import bisect
import numpy as np
import matplotlib.pyplot as plt

# Some useful functions

def compute_t_vector(start, end, number_of_values, vector_type):
    if vector_type == 'linear':
        x_vector = np.linspace(start, end, number_of_values)
    elif vector_type == 'log':
        n = number_of_values
        x_vector = [0.1*(np.exp(i * np.log(1+10*end)/n)-1)
                    for i in range(n+1)]
        x_vector[0] = x_vector[0]+start
    else:
        # For the moment, the default output is a linspace distribution
        x_vector = np.linspace(start, end, number_of_values)
    return np.array(x_vector)

def generate_MS_t2(ms_command):
    """
    Simulate T2 values using MS.
    The input is a string containing the ms-command
    The output is a list of float containing independent values of T2
    Note that the T2 values of ms are scaled by 4*N0
    """
    o = os.popen(ms_command).read()
    o = o.split('\n')
    t_obs = []
    for l in o:
        if l[:6] == 'time:\t':
            temp = l.split('\t')
            t_obs.append(float(temp[1]))
    return t_obs


def compute_empirical_dist(obs, x_vector=''):
    """
    This method computes the empirical distribution given the
    observations.
    The functions are evaluated in the x_vector parameter
    by default x_vector is computed as a function of the data
    by default the differences 'dx' are a vector
    """
    if x_vector == '':
        actual_x_vector = np.arange(0, max(obs)+0.1, 0.1)
    elif x_vector[-1] <= max(obs):  # extend the vector to cover all the data
        actual_x_vector = list(x_vector)
        actual_x_vector.append(max(obs))
        actual_x_vector = np.array(x_vector)
    else:
        actual_x_vector = np.array(x_vector)
    actual_x_vector[0] = 0  # The first element of actual_x_vector should be 0
    half_dx = np.true_divide(actual_x_vector[1:]-actual_x_vector[:-1], 2)
    # Computes the cumulative distribution and the distribution
    x_vector_shift = actual_x_vector[:-1] + half_dx
    x_vector_shift = np.array([0] + list(x_vector_shift) +
                              [actual_x_vector[-1] + half_dx[-1]])
    counts = np.histogram(obs, bins=actual_x_vector)[0]
    counts_shift = np.histogram(obs, bins=x_vector_shift)[0]
    cdf_x = counts.cumsum()
    cdf_x = np.array([0]+list(cdf_x))
    # now we compute the pdf (the derivative of the cdf)
    dy_shift = counts_shift
    dx_shift = x_vector_shift[1:] - x_vector_shift[:-1]
    pdf_obs_x = np.true_divide(dy_shift, dx_shift)
    return (cdf_x, pdf_obs_x)

##################  Functions for creating the ms command #################


def createCmd(modelParams):
    """
    Create a ms command based on some parameters under a structured model
    modelParams: dictionary,
        nbLoci: integer, how many independent loci to simulate
        samplingVector: list of integer, how many sequences to sample from each islands
        scenario: list of dictionaries. Each dictionary contains:
                'time': real, the time to start with the configuration (from present to past)
                the first dictionary of the list has always 'time': 0
                'migMatrix': matrix of real, the migration rate from deme i to deme j
                'demeSizeVector': list of real, the size of each deme
    """
    nbLoci = modelParams['nbLoci']
    sampling = ' '.join(str(i) for i in modelParams['samplingVector'])
    nbSequences = sum(modelParams['samplingVector'])
    initialParams = modelParams['scenario'][0]
    nbIslands = len(initialParams['migMatrix'][0])
    initialDemeSizes = initialParams['demeSizes']
    migMatrix0 = initialParams['migMatrix']
    msCmd = "./ms {nSeq} {nRep} -T -L -I {nbIslands} {samplingV}".format(
        nSeq=nbSequences, nRep=nbLoci, nbIslands=nbIslands, samplingV=sampling)
    # Add initial migration matrix
    migCmd = " -ma"
    for i in range(nbIslands):
        migMatrix0[i][i] = "x"
        l = [str(elm) for elm in migMatrix0[i]]
        migCmd += " " + " ".join(l)
    msCmd += migCmd
    # Add initial deme sizes
    for i in range(nbIslands):
        if (initialDemeSizes[i] != 1):
            msCmd += " -n {deme} {size}".format(deme=i+1,
                                                size=initialDemeSizes[i])
    # Add changes in the migration matrix and deme sizes
    for s in modelParams['scenario'][1:]:
        t = s['time'] * 0.5  # The time is scalled by 4N0 in ms
        if 'migMatrix' in s:
            # Add new migration parameters
            migMatrix = s['migMatrix']
            migCmd = " -ema {time} {nbPop}".format(time=t, nbPop=nbIslands)
            for i in range(nbIslands):
                migMatrix[i][i] = "x"
                l = [str(elm) for elm in migMatrix[i]]
                migCmd += " " + " ".join(l)
            msCmd += migCmd
        if 'demeSizes' in s:
            # Add initial deme sizes
            sizeVector = s['demeSizes']
            for i in range(nbIslands):
                msCmd += " -en {time} {deme} {newSize}".format(
                    time=t, deme=i+1, newSize=sizeVector[i])
    return(msCmd)


def readScenario(textFile):
    f = open(textFile, 'r')
    t = f.read()
    params = t.split('\n\n')
    # Defining some regex
    valuesPattern = re.compile("[0-9./*+-]+")
    samplingVectorPattern = re.compile("[0-9]+")
    mig_matrix_lines = re.compile("[0-9./+*-]+[0-9./+* -]*")
    # Creating the dictionnary
    d = {}
    d['nbLoci'] = eval(params[0].split('\n')[1])
    sampling = params[1].split('\n')[1]
    values = samplingVectorPattern.findall(sampling)
    d['samplingVector'] = [eval(v) for v in values]
    scenario = []
    initialConf = {}
    initialConf['time'] = 0
    initialDemeSizes = params[2].split('\n')[1]
    values = valuesPattern.findall(initialDemeSizes)
    initialConf['demeSizes'] = [eval(v) for v in values]
    initialMigMatrix = []
    initialM = params[3].split('\n')[1:]
    for line in initialM:
        values = valuesPattern.findall(line)
        initialMigMatrix.append([eval(v) for v in values])
    initialConf['migMatrix'] = initialMigMatrix
    scenario.append(initialConf)
    d['scenario'] = scenario
    changes = params[4:]
    nbOfChanges = int(len(changes)/3)
    for i in range(nbOfChanges):
        newConf = {}
        newConf['time'] = round(eval(changes[i*3].split('\n')[1]), 4)
        demeSizes = changes[i*3+1].split('\n')[1]
        values = valuesPattern.findall(demeSizes)
        newConf['demeSizes'] = [eval(v) for v in values]
        migMatrix = []
        M = mig_matrix_lines.findall(changes[i*3+2])
        for line in M:
            values = valuesPattern.findall(line)
            migMatrix.append([eval(v) for v in values])
        newConf['migMatrix'] = migMatrix
        d['scenario'].append(newConf)
    return(d)

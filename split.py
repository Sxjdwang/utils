"""
Randomly pick some files of LRS2 and generate a new set of list files compatible with wav2vec2.0

inputs: train_path: find a set of original files according to this directory
        target_dir: a set of target files
"""


import soundfile as sf
import math
import random

train_path = 'data/LRS2/train'
target_dir = 'data/LRS2part/train'

tsv = open(train_path+'.tsv', 'r')
ltr = open(train_path+'.ltr', 'r')
wrd = open(train_path+'.wrd', 'r')

tsv_lines = tsv.readlines()
ltr_lines = ltr.readlines()
wrd_lines = wrd.readlines()
prefix = tsv_lines[0].replace('\n', '')

total_sec = 0
total_count = 0

with open(target_dir+'.tsv', "w") as tsv_out, \
        open(target_dir + ".ltr", "w") as ltr_out,\
        open(target_dir + ".wrd", "w") as wrd_out:
    print(prefix, file=tsv_out)
    for i in range(len(tsv_lines) - 1):

        if random.uniform(0, 1) > 0.1:
            continue

        total_count += 1

        file = tsv_lines[i+1].split('\t')[0]
        inputAudio, sampFreq = sf.read(prefix + '/' + file)

        total_sec += inputAudio.size / float(sampFreq)

        print(tsv_lines[i + 1].replace('\n', ''), file=tsv_out)
        print(ltr_lines[i].replace('\n', ''), file=ltr_out)
        print(wrd_lines[i].replace('\n', ''), file=wrd_out)

print('Totally select %d files'%(total_count))
print('Total hours is %f'%(total_sec/60/60))










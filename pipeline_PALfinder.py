# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import subprocess
import time

def pipeline_PALfinder(GenomeFastaDir = '/home/lab/Dropbox/projects/micRocounter/benchmark.files/blackmon.test', Primer3Path = '/mnt/genomes/scripts/primer3-2.0.0-alpha/src/primer3_core', PALfinderPath = '/mnt/genomes/scripts/pal_finder_v0.02.04', twomerMin = '6', threemerMin = '4',
                       fourmerMin = '3', fivemerMin = '3', sixmerMin = '3'):
    output_dir = '/mnt/genomes/bm.PALfinder.results'
        
    input_files= listdir(path = GenomeFastaDir)
    input_files.sort()
    num_files = len(input_files)
    start = time.time()
    
    for i in range(num_files):
        start = time.time()
        cur_file = input_files[i]
        output_microsat = cur_file.strip('.fa' '.fna' '.fsa_nt' '.fa.txt' '.fas.txt') +'_microsat.txt'
        output_PAL = cur_file.strip('.fa' '.fna' '.fsa_nt' '.fa.txt' '.fas.txt') +'_PAL.txt'
        config_file = open('/mnt/genomes/scripts/pal_finder_v0.02.04/config_PALfinder.txt', mode = 'w')
        config_file.write(   'findPrimers 0 '
                          + '\nplatform 454'
                          + '\ninputFormat fasta'
                          + '\npairedEnd 0'
                          + '\ninput454reads '+GenomeFastaDir + '/' + cur_file 
                          + '\ninputReadFile '
                          + '\npairedReadFile'
                          + '\nMicrosatSumOut /mnt/genomes/bm.PALfinder.results/' +output_microsat
                          + '\nPALsummaryOut /mnt/genomes/bm.PALfinder.results/' + output_PAL
                          + '\n2merMinReps '+twomerMin
                          + '\n3merMinReps ' +threemerMin 
                          + '\n4merMinReps ' +fourmerMin
                          + '\n5merMinReps ' +fivemerMin 
                          + '\n6merMinReps ' + sixmerMin
                          + '\nprimer3input test/output/pr3in.txt'
                          + '\nprimer3output test/output/pr3out.txt'
                          + '\nkeepPrimer3files 0'
                          + '\nprimer3executable ' + Primer3Path 
                          + '\nprNamePrefix test_' 
                          + '\nPRIMER_TASK pick_pcr_primers'
                          + '\nPRIMER_OPT_SIZE 20' 
                          + '\nPRIMER_MIN_SIZE 18' 
                          + '\nPRIMER_MAX_SIZE 30'
                          + '\nPRIMER_MAX_NS_ACCEPTED 0' 
                          +'\npr3ProductSizeRangeMinVal  60'
                          + '\npr3ProductSizeRangeMaxVal  500' 
                          + '\nPRIMER_OPT_SIZE  20'
                          + '\nPRIMER_MIN_GC  30.0' 
                          + '\nPRIMER_MAX_GC  80.0' 
                          + '\nPRIMER_GC_CLAMP  2' 
                          + '\nPRIMER_MAX_END_GC  5'
                          + '\nPRIMER_MIN_TM  58.0' 
                          + '\nPRIMER_MAX_TM  65.0'
                          + '\nPRIMER_OPT_TM  62.0' 
                          + '\nPRIMER_PAIR_MAX_DIFF_TM  2.0'
                          + '\nPRIMER_TM_FORMULA  0' 
                          + '\nPRIMER_MAX_SELF_ANY  8.00'
                          + '\nPRIMER_PAIR_MAX_COMPL_ANY  8.00' 
                          +'\nPRIMER_MAX_SELF_END  3.00'
                          + '\nPRIMER_PAIR_MAX_COMPL_END  3.00' 
                          + '\nPRIMER_MAX_POLY_X  4'
                          + '\nPRIMER_LOWERCASE_MASKING  0' 
                          + '\nPRIMER_NUM_RETURN  1'
                          + '\nPRIMER_MISPRIMING_LIBRARY  simple.ref' 
                          + '\nPRIMER_MAX_LIBRARY_MISPRIMING  10.00'
                          + '\nPRIMER_LIB_AMBIGUITY_CODES_CONSENSUS   0')
        prog1 = subprocess.call('perl pal_finder_v0.02.04.pl config_PALfinder.txt',shell = True, cwd = '/mnt/genomes/scripts/pal_finder_v0.02.04')
        end = time.time()
        time_file = open('/mnt/genomes/bm.PALfinder.results/bm.PALfinder.txt', mode = 'a')
        time_file.write(cur_file + ',' + str(end-start) + '\n')
        print(end-start)











































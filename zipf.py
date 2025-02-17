# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:07:56 2019
Last Updated: Sun Jun 21 2020

@author: seth_cattanach
"""

# Hypothesis testing of Zipf's Law on natural and non-natural (i.e. randomly generated) language
# for analysis and discussion, see "README.md"

import pylab
from nltk.probability import FreqDist
import random
import string

# ----------------------------------------------------------------------------
# Create a frequency distribution of the given text and plot in order 
# to visualize Zipf's Law
# ----------------------------------------------------------------------------
def zipf(text, name, new_figure=False, log=True):
    fdis = dict(FreqDist(text))
    freq = [item[1] for item in sorted(fdis.items(), key=lambda kv: kv[1], reverse=True)]
    rank = [item+1 for item in range(len(sorted(fdis.items(), key=lambda kv: kv[1], reverse=True)))]
    
    # plot freq vs rank using pylab
    # (plotting will occur on the same plot unless 'new_figure' parameter is 'True')
    if new_figure:
        pylab.figure()
    pylab.plot(rank,freq, label=name)
    
    # change plot to log scale to visually confirm Zipf's Law
    # see discussion in README.md
    if log:
        pylab.xscale("log")
        pylab.yscale("log")
    
    # add axis labels, title, and legend
    pylab.xlabel('Rank')
    pylab.ylabel('Frequency')
    if log:
        pylab.title('Logarithmic Frequency vs Rank for Words in a Text')
    else:
        pylab.title('Frequency vs Rank for Words in a Text')
        
    pylab.legend(loc='upper right')
  
    
# -----------------------------------------------------------------------------
# Function to generate random text 
# -----------------------------------------------------------------------------
def generate_text(subset=8, text_len=1000000, approx_word_len=5, log=True):
    if subset>26:
        subset=26     # max chars in alphabet
    if subset<1:
        subset=8     # default chars (a-h, plus the space character) to use in random string generation
      
    if approx_word_len>subset:
        approx_word_len=subset

    # generate random string of 'words'
    chars = list(string.ascii_lowercase)[:subset]
    for i in range(int(subset/approx_word_len)):
        chars.append(' ')               # add the number of spaces required to maintain an approx. word length (specified)
    zipf(''.join(random.choice(chars) for _ in range(text_len)).split(' '),'Randomly-Generated String, avg word len='+str(approx_word_len), new_figure='True', log=log)

from nltk.book import *
from .zipf import *

def main():
    # call zipf for natural language sample(s)
    zipf(text1, "Moby Dick")         
    zipf(text2, "Sense and Sensibility")        
    zipf(text3,"The Book of Genesis")        
    zipf(text4, "Inaugural Address Corpus")         
    zipf(text5, "Sample Chat Corpus")         
    # call zipf for random language sample(s)
    generate_text(approx_word_len=6)
    
if __name__ == "__main__":
    main()

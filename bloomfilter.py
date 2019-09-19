import mmh3
from bitarray import bitarray
import math

class BloomFilter:

    def __init__(self, false_positive_rate, estimated_word_count):

        #find size and number of hashes desired for false positive rate and word count
        self.size = int((-estimated_word_count * math.log(false_positive_rate)) / (math.log(2) **2))
        self.hash_count = int((self.size / estimated_word_count) * math.log(2))
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    #Insert a word into the bloom filter
    def insert(self, item):
        for i in range(self.hash_count):
            location = mmh3.hash(item, i) % self.size
            self.bit_array[location] = 1

    #check if the filter contains the desired word
    def contains(self, item):
        for i in range(self.hash_count):
            if self.bit_array[mmh3.hash(item, i) % self.size] == 0:
                return("This is not a real world")
        return("This is a real word")

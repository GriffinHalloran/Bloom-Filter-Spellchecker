from bloomfilter import BloomFilter
import math 

def main():
    #Bloom filter takes two argument: desired false positive rate and number of words in the dictionary 
    my_bloom_fil = BloomFilter(0.01, 466000)
    lines = open("./words.txt").read().splitlines()
    for line in lines:
        my_bloom_fil.insert(line)
    item_to_check = 'test'
    while(True):
        item_to_check = raw_input("Which word you want to search: ")
        if item_to_check == ':!':
            break
        print(my_bloom_fil.contains(item_to_check))

if __name__ == '__main__':
    main()

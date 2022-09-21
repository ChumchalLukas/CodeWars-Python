'''
Kata instructions:

Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the numebr of sheep present in the array (true means present).

'''

#Result with while loop: Counting how many Trues (sheep in flock) are

def count_sheeps(sheep):
    flock_size = len(sheep)
    sheepsin = 0
    
    while flock_size > 0:
        for i in range(0,flock_size):
            if sheep[i] == True:
                sheepsin += 1
                packsize = packsize - 1
            else:
                packsize = packsize - 1
                continue
            
    return sheepsin

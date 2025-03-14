"""Counting Point Mutations"""


filepath = ("/mnt/c/Users/jsml6/Downloads/rosalind_hamm.txt")

sequences = [text for text in open(filepath).read().rstrip().split('\n')]

distance = 0
for num in range(len(sequences[0])):
    if sequences[0][num] != sequences[1][num]:
        distance += 1
        
print(distance)
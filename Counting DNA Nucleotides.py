input_DNA = "AAATC"
ATGC = [0,0,0,0]

for base in input_DNA:
    if base == "A":
        ATGC[0] += 1
    elif base == "T":
        ATGC[1] += 1
    elif base == "G":
        ATGC[2] += 1
    elif base == "C":
        ATGC[3] += 1
    else:
        print("염기가 아닙니다")

    # ATGC[0] += 1 if (base == "A") else ATGC[1] += 1 if (base == "T") else ATGC[2] += 1 if (base == "G") else ATGC += 1 if (base == "C")
    
print(ATGC)
    
def count_bits(n):
    X = bin(n)
    count = 0
    for i in X:
        if i == "1":
            count+=1
        else:
            pass
    print(count)
    return count

count_bits(5)


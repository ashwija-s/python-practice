def fibonacci(n):
    sequence = [0,1]
    if n < 2:
        return n
    for i in range(2, n + 1):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[n]
print(fibonacci(13))  #233
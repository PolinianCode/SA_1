def MSE(original, data):
    N = len(original)
    sum = 0
    for i in range(0, N):
        if data[i] is not None:
            sum += (original[i]-data[i])**2

    result = sum/N

    return result
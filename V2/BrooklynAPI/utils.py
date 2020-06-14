def decTo256(n):
    data_array = [0, 0]
    data_array[0] = n % 255
    data_array[1] = n // 255
    return data_array
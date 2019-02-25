def moving_average(y, x):
    window_size = 5
    mv_avg = {}
    for i in range(0, len(y)-window_size):
        avg = sum(y[i:window_size+i]) / window_size
        mv_avg[x[i-1]] = avg
    return mv_avg

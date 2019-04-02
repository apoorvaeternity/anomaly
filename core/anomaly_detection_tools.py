from statsmodels.tsa.arima_model import ARIMA


def moving_average(y, x):
    window_size = 5
    mv_avg = {}
    for i in range(0, len(y) - window_size):
        avg = sum(y[i:window_size + i]) / window_size
        mv_avg[x[i - 1]] = avg
    return mv_avg


def arima(series):
    num_of_train = 20
    predicted = {}
    X = series.values
    Y = series.keys()
    train, test = X[0:num_of_train], X[num_of_train:len(X)]
    history = [x for x in train]
    n = num_of_train
    for t in range(len(test)):
        model = ARIMA(history, order=(5, 1, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        obs = test[t]
        history.append(obs)
        predicted[Y[n + t]] = yhat
    return predicted

import numpy as np
from sklearn.linear_model import LinearRegression

def load_model():
    X = np.array([[10,8,6],[5,5,4],[2,2,2],[8,7,5]])
    y = np.array([40,60,85,50])

    model = LinearRegression()
    model.fit(X,y)
    return model

model = load_model()

def predict(c,w,e):
    return int(model.predict([[c,w,e]])[0])
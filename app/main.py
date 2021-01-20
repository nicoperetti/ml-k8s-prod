import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


# define model for post request.
class ModelParams(BaseModel):
    pclass: int
    sex: str


# load model
model = pickle.load(open("models/model.pkl", 'rb'))


def get_prediction(pclass, sex):
    """Get predictions

    :param pclass: pclass
    :type pclass: int
    :param sex: sex
    :type sex: str
    :return: predictions
    :rtype: dict
    """
    x = [[pclass, sex]]
    dfp = pd.DataFrame(x, columns=["Pclass", "Sex"])
    survived = model.predict(dfp)[0]
    return {'survived': int(survived)}


# API instance
app = FastAPI()


@app.get("/")
def health_check():
    """Helth Check

    :return: helth check status
    :rtype: dict
    """
    return {"Check": "Ok!"}


@app.get("/predict")
def predict(params: ModelParams):
    """Predict endpoint

    :param params: model features
    :type params: ModelParams
    :return: predictions
    :rtype: dict
    """
    pclass, sex = params.pclass, params.sex

    pred = get_prediction(pclass, sex)

    return {"preds": pred, "feats": [pclass, sex]}

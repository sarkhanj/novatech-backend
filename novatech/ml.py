from __future__ import print_function
from novatech.models import Dataset, Regions, Records
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd  # data analysis
import numpy as np  # linear algebra
from sklearn.metrics import classification_report
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')


dataset = Dataset.objects.all()

RF = None
x = None


def train():
    global RF, x
    # crop = pd.read_csv('Crop_recommendation.csv')
    crop = pd.DataFrame(list(dataset.values()))
    crop.head()
    features = crop[['N', 'P', 'K', 'temperature',
                     'humidity', 'ph', 'rainfall']]
    target = crop['label']

    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=2)

    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    RF.fit(x_train, y_train)

    predicted_values = RF.predict(x_test)
    x = metrics.accuracy_score(y_test, predicted_values)


def predict_(record):
    global RF, x
    data = [record.N, record.P, record.K, record.temperature,
            record.humidity, record.ph, record.rainfall]

    print(record.N)
    prediction_RF = RF.predict_proba(np.array([data]))[0]
    print(prediction_RF)
    print(RF.classes_)
    probs = []
    types = []
    for count, i in enumerate(prediction_RF):
        if i > 0:
            probs.append([list(prediction_RF).index(i), i])
            # prediction_RF = np.delete(prediction_RF, count-2)
            prediction_RF[list(prediction_RF).index(i)] = 0
    for item in probs:
        types.append([RF.classes_[item[0]], item[1]])

    return [x, types]

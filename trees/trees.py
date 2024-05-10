import scipy.stats
import os
import librosa
import mlflow
import optuna
import numpy
import string
import pandas

from collections import Counter
from mlflow.models import infer_signature
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score, make_scorer, confusion_matrix, log_loss, precision_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate, StratifiedKFold
from pathlib import Path
from sklearn.model_selection import train_test_split

# Setting mlflow track
mlflow.set_tracking_uri(uri="http://127.0.0.1:7000")

# Setting mlflow experiment
mlflow.set_experiment("DecTreeGini")

# Setting database dir
databaseDir=os.path.join(os.getcwd(), "dataset")

# Labeling and sorting through data
f=open("dataset/train.txt", "r")
train_data_unclean=f.read()
train_data=train_data_unclean.split("\n")
for num, item in enumerate(train_data):
    train_data[num]=item.split(";")

data=[]
labels=[]
for item in train_data:
    data.append(item[0])
    labels.append(item[1])
    
# Labeling and sorting through data (test_data)
f=open("dataset/test.txt", "r")
test_data_unclean=f.read()
test_data=test_data_unclean.split("\n")
for num, item in enumerate(test_data):
    test_data[num]=item.split(";")

test_dataset=[]
test_labels=[]
for item in test_data:
    test_dataset.append(item[0])
    test_labels.append(item[1])


# Converting simple arrays to DataFrame
train_database=pandas.DataFrame(data=data)
train_database["sentiment"]=labels
train_database.columns=["text_data", "sentiment"]

with mlflow.start_run():
    # Manually setting train_test sets (not with sklearn train_test_split because train/test sets are prepared in dataset)
    X_train=data
    y_train=labels
    X_test=test_dataset
    y_test=test_labels

    params={
        "criterion": "entropy",
        "splitter": "best",
    }

    # Model creation
    model=DecisionTreeClassifier(**params)

    # Vectorizing of text data
    count_vec=CountVectorizer()
    X_train_counts=count_vec.fit_transform(X_train)
    X_test_counts=count_vec.transform(X_test)

    # Train fit and prediction of model
    model.fit(X_train_counts, y_train)
    preds_test=model.predict(X_test_counts)

    # Accuracy score
    accuracy=accuracy_score(y_test, preds_test)
    print(accuracy)

    mlflow.log_params(params)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.set_tag("Training Info", "Basic DecTree for text sentiment")
    signature=infer_signature(X_train, preds_test)
    model_info=mlflow.sklearn.log_model(
        sk_model=DecisionTreeClassifier,
        artifact_path="sentiment_model",
        signature=signature,
        input_example=X_train_counts,
        registered_model_name="logging_quickstart",
    )
    mlflow.log_artifacts()

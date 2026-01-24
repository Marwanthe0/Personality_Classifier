# Importing Necessary Modules
import numpy as np
import pandas as pd
import pickle

# Importing Necessary Models for ML
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, recall_score, classification_report

# Importing Dataset
data = pd.read_csv("Personality_Test_Project\data\personality_dataset.csv")
# Defining Target Variable
target = "Personality"
# Defining Features and target column
X = data.drop([target], axis=1)
Y = data[target]

print(X.shape)
print(Y.shape)
# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
# defining Numerical and CAtegorical Columns
num_features = X.select_dtypes(exclude=["object"]).columns
cat_features = X.select_dtypes(include=["object"]).columns


#Creating Numerical and Categorical Pipeline
cat_pipe = Pipeline(
    [
        ("imputing", SimpleImputer(strategy="most_frequent")),
        ("encoding", OneHotEncoder()),
    ]
)
num_pipe = Pipeline(
    [
        ("imputing", SimpleImputer(strategy="mean")),
        ("scaling", StandardScaler()),
    ]
)

transformer = ColumnTransformer(
    [
        ("cat_pipe", cat_pipe, cat_features),
        ("num_pipe", num_pipe, num_features),
    ]
)



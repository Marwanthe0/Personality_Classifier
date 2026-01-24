# Importing Necessary Modules
import numpy as np
import pandas as pd
import pickle

# Importing Necessary Models for ML
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Importing Dataset
data = pd.read_csv("personality_dataset.csv")
# Defining Target Variable
target = "Personality"
# Defining Features and target column
X = data.drop([target], axis=1)
Y = data[target]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
# defining Numerical and CAtegorical Columns
num_features = X.select_dtypes(exclude=["object"]).columns
cat_features = X.select_dtypes(include=["object"]).columns


# Creating Numerical and Categorical Pipeline
cat_pipe = Pipeline(
    [
        ("imputing", SimpleImputer(strategy="most_frequent")),
        ("encoding", OneHotEncoder(handle_unknown="ignore")),
    ]
)
num_pipe = Pipeline(
    [
        ("imputing", SimpleImputer(strategy="mean")),
        ("scaling", StandardScaler()),
    ]
)
# Creating The actual Column Transformer
transformer = ColumnTransformer(
    [
        ("cat_pipe", cat_pipe, cat_features),
        ("num_pipe", num_pipe, num_features),
    ]
)

# Model Creation
rf_model = RandomForestClassifier(random_state=42)

# Actual Pipeline of the Model
rf_pipe = Pipeline(
    [
        ("Transformer", transformer),
        ("Model", rf_model),
    ]
)

# Defining parameters for Gridsearchcv
param_grid = {
    'Model__n_estimators': [50, 100, 150, 200],
    'Model__max_depth': [None, 10, 20, 30],
    'Model__min_samples_split': [2, 5, 10],
    'Model__criterion': ['gini', 'entropy']
}

# Create GridSearchCV
grid_search = GridSearchCV(
    estimator=rf_pipe,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
)

# Model Training
grid_search.fit(X_train, y_train)

# Getting the best model
best_rf_pipe = grid_search.best_estimator_

# Printing best parameters
print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", grid_search.best_score_)

# Predicting
y_predict = best_rf_pipe.predict(X_test)

# Metrices Calculation and printing
accuracy = accuracy_score(y_test, y_predict)
report = classification_report(y_test, y_predict)
print("Accuracy Score:", accuracy)
print("Classification Report:", report)

# Saving the model using pickle file
with open("RF_Model.pkl", "wb") as file:
    pickle.dump(best_rf_pipe, file)

print("🎉Model is saved Successfully.✅")

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score
import xgboost as xgb
import os
import pickle

def load_penguins_data() -> pd.DataFrame:
    """Load and clean the penguins dataset."""
    data = sns.load_dataset('penguins').dropna()
    return data

def preprocess_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, LabelEncoder]:
    """Apply one-hot encoding to categorical features and label encoding to target."""
    # Separate features and target
    X = data.drop(columns=['species'])  # Remove species column from features
    y = data['species']
    # One-hot encode categorical features (sex, island)
    X = pd.get_dummies(X, columns=['sex', 'island'], dtype=int)
    # Encode the target variable
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    os.makedirs('app/data', exist_ok=True)
    with open('app/data/label_encoder.pkl', 'wb') as f:
        pickle.dump(le, f)
    return X, y_encoded, le

def split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42) -> tuple:
    """Split data into training and test sets with stratification."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> xgb.XGBClassifier:
    """Train XGBoost model with parameters to prevent overfitting."""
    model = xgb.XGBClassifier(max_depth=3, n_estimators=100, random_state=42, eval_metric='mlogloss')
    model.fit(X_train, y_train)
    return model

def evaluate_model(model: xgb.XGBClassifier, X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series) -> tuple[float, float]:
    """Evaluate model using F1-score on train and test sets."""
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    train_f1 = f1_score(y_train, y_train_pred, average='weighted')
    test_f1 = f1_score(y_test, y_test_pred, average='weighted')
    print(f"Train F1-score: {train_f1:.4f}")
    print(f"Test F1-score: {test_f1:.4f}")
    return train_f1, test_f1

def save_model(model: xgb.XGBClassifier) -> None:
    """Save the trained model to app/data/model.json."""
    os.makedirs('app/data', exist_ok=True)
    model.save_model('app/data/model.json')

if __name__ == "__main__":
    data = load_penguins_data()
    X, y, le = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    train_f1, test_f1 = evaluate_model(model, X_train, y_train, X_test, y_test)
    save_model(model)
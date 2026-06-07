import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_and_evaluate():
    # Load sample data
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target

    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)

    # Calculate metric
    accuracy = model.score(X_test, y_test)
    
    # Save the deployment artifact (metrics log)
    with open("metrics.txt", "w") as f:
        f.write(f"Accuracy: {accuracy:.4f}")
    
    print(f"Model trained successfully. Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    train_and_evaluate()
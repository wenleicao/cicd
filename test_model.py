import os

def test_metrics_exist():
    # Assert that the training pipeline successfully produced the metric asset
    assert os.path.exists("metrics.txt")

def test_model_accuracy_threshold():
    # Read the accuracy and assert it passes production requirements (> 80%)
    with open("metrics.txt", "r") as f:
        content = f.read()
        accuracy = float(content.split(": ")[1])
    
    assert accuracy >= 0.80
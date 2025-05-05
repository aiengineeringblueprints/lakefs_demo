from sklearn.datasets import load_iris
import pandas as pd
import os


def get_iris_data():
    """
    Load the iris dataset from sklearn and save it as a CSV file.
    """
    # Load the iris dataset
    iris = load_iris()
    iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_data['target'] = iris.target

    # Save the dataset to a CSV file
    if not os.path.exists('data'):
        os.makedirs('data')
    iris_data.to_csv('data/iris.csv', index=False)


if __name__ == "__main__":
    # Load the iris dataset and save it as a CSV file
    get_iris_data()

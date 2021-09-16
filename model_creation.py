from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

import argparse

def get_data():
    return load_iris()

def split_data(data):
    return train_test_split(
        data.data, 
        data.target, 
        test_size=.2,
        random_state=42
    )

def train_model(X_train, X_test, y_train, y_test):
    clf = SGDClassifier(
        max_iter=1000, 
        tol=1e-3
    ).fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)

    return clf, y_test, y_pred

def evaluate_model(clf, y_test, y_pred):
    print('Accuracy: ', accuracy_score(y_test, y_pred))
    return clf

def save_model(clf):
    dump(clf, 'data/model_v1.1.joblib') 

def main(should_save_model=False):
    clf = (
        evaluate_model(
            *train_model(
                *split_data(
                    get_data()
                )
            )
        )
    )
    
    if should_save_model:
        save_model(clf)

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(
        description='Flag to set if model will be persisted.'
    )
    
    my_parser.add_argument(
        '-s',
        '--save',
        action='store_true',
        help='Persist model to disk.'
    )

    args = my_parser.parse_args()
    
    main(args.save)
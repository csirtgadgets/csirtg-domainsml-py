from __future__ import print_function
import numpy as np
from sklearn import tree, ensemble
from sklearn.metrics import accuracy_score, recall_score
import pickle
from pprint import pprint
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys
import textwrap
from csirtg_domainsml.domain import _extract_features
import os

PYVERSION = 2
if sys.version_info > (3,):
    PYVERSION = 3
    basestring = (str, bytes)

me = os.path.dirname(__file__)

MODEL = os.getenv('CSIRTG_DOMAINSML_MODEL', '%s/../data/model.pickle' % me)
if PYVERSION == 2:
    MODEL = os.getenv('CSIRTG_DOMAINSML_MODEL', '%s/../data/model_py2.pickle' % me)


def accuracy(classifier, test_inputs, test_outputs):
    # Use the trained classifier to make predictions on the test data
    predictions = classifier.predict(test_inputs)
    print("Predictions on testing data computed.")

    # Print the accuracy (percentage of phishing websites correctly predicted)
    accuracy = 100.0 * accuracy_score(test_outputs, predictions)
    recall = 100.0 * recall_score(test_outputs, predictions)
    print("The recall score of your decision tree on testing data is: " + str(recall))
    print("The accuracy of your decision tree on testing data is: " + str(accuracy))


def load_data(handle):
    lines = []
    for l in handle:
        l = l.rstrip("\n")
        lines.append(l.split(','))

    training_data = np.array(lines, dtype=int)
    print("Training data loaded.")

    return training_data


def train_model(training_data):
    inputs = training_data[:, :-1]
    outputs = training_data[:, -1]

    n = int(len(inputs) * .7)
    train_inputs = inputs[:n]
    train_outputs = outputs[:n]

    test_inputs = inputs[n:]
    test_outputs = outputs[n:]
    print("Training data loaded.")

    # Create a decision tree classifier model using scikit-learn
    classifier = ensemble.RandomForestClassifier()
    print("classifier created.")

    print("Beginning model training.")
    # Train the decision tree classifier
    classifier.fit(train_inputs, train_outputs)
    print("Model training completed.")

    return classifier, test_inputs, test_outputs


def model_save(cls, filename):
    print("Saving model to %s" % filename)
    print(filename, pickle.dumps(cls))


def main():
    import sys
    p = ArgumentParser(
        description=textwrap.dedent('''\
                    example usage:
                        $ csirtg-domainsml --training data/training.csv -i badsite-paypal.com
                    '''),
        formatter_class=RawDescriptionHelpFormatter,
        prog='csirtg-phish'
    )

    p.add_argument('-d', '--debug', dest='debug', action="store_true")
    p.add_argument('--save')
    p.add_argument('--load')
    p.add_argument('--training')
    p.add_argument('-i', '--indicator')

    args = p.parse_args()

    if args.load:
        with open(args.load) as FILE:
            classifier = pickle.load(FILE)

    else:
        handle = sys.stdin
        if args.training:
            handle = open(args.training)

        training_data = load_data(handle)
        classifier, test_inputs, test_outputs = train_model(training_data)
        accuracy(classifier, test_inputs, test_outputs)

    if args.save:
        with open(args.save, 'wb') as OUTFILE:
            # print(pickle.dump(classifier), file=OUTFILE)
            pickle.dump(classifier, OUTFILE)

        raise SystemExit

    if args.indicator:
        feats = _extract_features(args.indicator)
        feats = np.array([feats], dtype=int)
        pprint(feats)
        p = classifier.predict(feats)
        print(p)


if __name__ == '__main__':
    main()

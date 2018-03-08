from argparse import ArgumentParser, RawDescriptionHelpFormatter
import textwrap
import os
import pickle
from csirtg_domainsml.domain import predict as predict_domain
from pprint import pprint
from .constants import PYVERSION

me = os.path.dirname(__file__)

MODEL = os.getenv('CSIRTG_DOMAINSML_MODEL', '%s/../data/model.pickle' % me)

CLS = None
if os.path.exists(MODEL):
    with open(MODEL, 'rb') as F:
        CLS = pickle.load(F)


def predict(i, classifier=CLS):
    if not classifier:
        with open(MODEL) as FILE:
            classifier = pickle.load(FILE)

    return predict_domain(i, classifier)[0]


def main():
    p = ArgumentParser(
        description=textwrap.dedent('''\
            example usage:
                $ csirtg-domainsml --model model.pickle -i paypal-badsite.com
            '''),
        formatter_class=RawDescriptionHelpFormatter,
        prog='csirtg-domainsml'
    )

    p.add_argument('-i', '--indicator', help="specify indicator")

    args = p.parse_args()

    p = predict(args.indicator)
    if p:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
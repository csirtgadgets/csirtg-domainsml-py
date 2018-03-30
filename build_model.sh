#!/bin/bash

# https://github.com/vaseem-khan/URLcheck/blob/master/URL.txt
rm data/model.pickle
cat tmp/training.csv | python csirtg_domainsml/train.py --save data/model.pickle

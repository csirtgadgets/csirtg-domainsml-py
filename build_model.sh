#!/bin/bash

# https://github.com/vaseem-khan/URLcheck/blob/master/URL.txt
cat tmp/training.csv | python csirtg_domainsml/train.py --save data/model.pickle
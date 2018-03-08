#!/bin/bash

cat tmp/training.csv | python csirtg_domainsml/train.py --save data/model.pickle
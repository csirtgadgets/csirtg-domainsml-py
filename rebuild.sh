#!/bin/bash

rm -rf tmp
mkdir -p tmp

echo "creating whitelist"
cat data/whitelist.txt | python csirtg_domainsml/domain.py --good > tmp/good.csv

echo "creating blacklist"
cat data/blacklist.txt | python csirtg_domainsml/domain.py > tmp/bad.csv

echo "merging lists"
cat tmp/good.csv tmp/bad.csv | gshuf > tmp/training.csv

TESTS="google.com g00gle.com aws.amazon.com ringcentral.com security.duke.edu gallery.mailchimp.com csirtg.io \
bankwest.com.au"


for T in $TESTS; do
  echo "Testing $T"
  cat tmp/training.csv | python csirtg_domainsml/train.py -i $T
done

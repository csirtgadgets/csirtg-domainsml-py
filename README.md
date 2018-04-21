# csirtg-domainsml
simple library for detecting suspicious domains

https://csirtgadgets.com/commits/2018/3/8/hunting-for-suspicious-domains-using-python-and-sklearn
https://csirtgadgets.com/commits/2018/4/20/predicting-attacks-with-python-and-sklearn
https://csirtgadgets.com/commits/2018/3/30/hunting-for-threats-like-a-quant

```bash
$ pip install -r dev_requirements.txt
$ python setup.py develop
$ bash rebuild.sh
$ bash build_model.sh

$ csirtg-domainsml -i paypal-ate-my-lunch.com
Yes
$ csirtg-domainsml -i paypal.com
No
```

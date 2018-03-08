# csirtg-domainsml
simple library for detecting suspicious domains

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

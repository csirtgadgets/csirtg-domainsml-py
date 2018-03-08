import math
import string

# Stolen from Ero Carrera
# http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html
# https://www.splunk.com/blog/2015/10/01/random-words-on-entropy-and-dns/


def range_bytes():
    return range(256)


def range_printable():
    return (ord(c) for c in string.printable)


def entropy(data, iterator=range_bytes):
    if not data:
        return 0

    val = 0
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            val += - p_x*math.log(p_x, 2)

    return val

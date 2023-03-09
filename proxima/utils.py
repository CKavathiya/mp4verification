from datetime import time

def cast(klass, obj):
    obj.__class__ = klass


def to_secs(ts: time):
    return (ts.hour * 60 + ts.minute) * 60 + ts.second


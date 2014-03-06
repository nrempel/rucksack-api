# -*- coding: utf-8 -*-

from datetime import datetime


def unix_time(dt):
    epoch = datetime.fromtimestamp(0, dt.tzinfo)
    utc = dt - epoch
    return int(utc.total_seconds())

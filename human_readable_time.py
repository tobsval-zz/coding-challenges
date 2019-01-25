#https://www.codewars.com/kata/human-readable-time/train/python

def make_readable(seconds : int):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    readable_time = '{:d}:{:02d}:{:02d}'.format(hours, mins, secs)
    return readable_time


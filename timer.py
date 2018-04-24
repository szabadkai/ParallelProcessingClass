#!/usr/bin/env python
#
#  Python Timer Class - Context Manager for Timing Code Blocks
#  Corey Goldberg - 2012
#


from timeit import default_timer


class Timer(object):
    def __init__(self, verbose=False, name=None):
        self.verbose = verbose
        self.timer = default_timer
        self.name = name

    def __enter__(self):
        self.start = self.timer()
        return self

    def __exit__(self, *args):
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs * 1000  # millisecs
        if self.verbose:
            if self.name:
                print('{0}: %f ms'.format(self.name) % self.elapsed)
            else:
                print('elapsed time: %f ms' % self.elapsed)

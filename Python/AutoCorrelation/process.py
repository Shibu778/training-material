#!/usr/bin/env python

from argparse import ArgumentParser
import random
import sys
from functions import w


def next_value(x, max_delta):
    delta_x = random.uniform(-max_delta, max_delta)
    x_new = x + delta_x
    while x_new < 0.0 or x_new > 1.0:
        delta_x = random.uniform(-max_delta, max_delta)
        x_new = x + delta_x
    if w(x_new)/w(x) >= random.random():
        x = x_new
    return x


def monte_carlo(w, nr_steps, burn_in=0, skip=1, max_delta=0.01):
    x = random.random()
    for _ in range(burn_in):
        x = next_value(x, max_delta)
    for step in range(nr_steps):
        x = next_value(x, max_delta)
        if step % skip == 0:
            yield x
    return


def main():
    arg_parser = ArgumentParser(description='create Monte Carlo sequence')
    arg_parser.add_argument('--steps', type=int, default=10,
                            help='number of steps for process')
    arg_parser.add_argument('--max-delta', type=float, default=0.01,
                            dest='max_delta',
                            help='number of steps for process')
    arg_parser.add_argument('--burn-in', type=int, default=0,
                            dest='burn_in',
                            help='number of steps for process')
    arg_parser.add_argument('--skip', type=int, default=1,
                            help='''number of steps to skip to avoid
                                    autocorrelation''')
    arg_parser.add_argument('--time', action='store_true',
                            help='print time step colomn')
    options = arg_parser.parse_args()
    if options.time:
        print('\n'.join(('{0:d}\t{1:.8f}'.format(t, x) for t, x in
                         enumerate(monte_carlo(
                             w, options.steps,
                             burn_in=options.burn_in,
                             skip=options.skip,
                             max_delta=options.max_delta)))))
    else:
        print('\n'.join(('{0:.8f}'.format(x) for x in
                         monte_carlo(w, options.steps,
                                     burn_in=options.burn_in,
                                     skip=options.skip,
                                     max_delta=options.max_delta))))

if __name__ == '__main__':
    status = main()
    sys.exit(status)

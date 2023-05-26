#!/usr/bin/env python3

import fibonacci


def main():
    print('Testing external module...')

    print()
    print('Fibonacci Series by function:')
    for i in range(0, 11):
        print(f'\t{i} -> {fibonacci.calc_externally(i)}')

    print()
    print('Fibonacci Series by class:')
    calculator = fibonacci.ExternalSeriesCalculator()
    for i in range(0, 11):
        calculator.put_index(index=i)
    print(f'\t{calculator.calc()}')

    print()
    print('Testing variables:')
    print(f'\tthe_answer = {fibonacci.the_answer}')
    print(f'\twhat = "{fibonacci.what}"')


if __name__ == '__main__':
    main()

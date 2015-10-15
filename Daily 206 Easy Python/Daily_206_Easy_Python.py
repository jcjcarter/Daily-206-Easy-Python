from functools import reduce

def recurrence(ops, a0, n):
    def transform(x, op):
        return eval(repr(x) + op)

    ops = ops.split()
    m = reduce(transform, [op for op in ops if op[0] in ('*', '/')], 1)

    b = reduce(transform, ops, 0)

    for k in range(n + 1):
        print('Term 0: ', a0 * m ** k + b * (m ** k - 1) / (m - 1))
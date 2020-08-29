#!/usr/bin/env pypy3

import ast
import inspect
import types

class Rewrite(ast.NodeTransformer):
    pass

def transform_ast(f):
    source = inspect.getsource(f)
    source = '\n'.join(source.splitlines()[1:]) # remove the decorator first line.
    print(f"source={source.encode('unicode_escape').decode('utf-8')}")

    old_code_obj = f.__code__
    old_ast = ast.parse(source)
    new_ast = Rewrite().visit(old_ast)
    new_code_obj = compile(new_ast, old_code_obj.co_filename, 'exec')
    f = types.FunctionType(new_code_obj.co_consts[0], f.__globals__)
    return f

# @transform_ast
def foo(x):
    return range(10)
    return x


def bootstrap(f, stack=[]):
    from collections import defaultdict
    from types import GeneratorType

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def square(x):
    return x*x

@bootstrap
def sum_n(x):
    if x == 0: yield (yield square(0))
    yield (x + (yield sum_n(x-1)))

print(sum_n(5))
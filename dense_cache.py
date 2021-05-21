def dense_cache(func):
    cache = []
    for _ in range(H+10):
        cache += [[-1]*(W+10)]

    def memoized_func(i, j):
        if cache[i+5][j+5] != -1:
            return cache[i+5][j+5]
        result = func(i,j)
        cache[i+5][j+5] = result
        return result

    return memoized_func

# for GCJ pypy2

def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper
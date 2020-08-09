import sys
print('\n'.join([f"Uh! {b}-{a}!" for a, b in zip(*[iter([l.split()[3] for l in sys.stdin.readlines()[1:]])]*2)]))

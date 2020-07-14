import std.stdio, std.algorithm, std.range, std.functional;
 
bool[] sieve(in uint limit) nothrow @safe {
    if (limit < 2)
        return [];
    auto composite = new bool[limit];
 
    foreach (immutable uint n; 2 .. cast(uint)(limit ^^ 0.5) + 1)
        if (!composite[n])
            for (uint k = n * n; k < limit; k += n)
                composite[k] = true;
    return composite;
}

void main() {
    static composite = 1_000_000.sieve;
    composite.writeln;
}

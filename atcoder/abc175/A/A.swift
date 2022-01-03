#!/usr/bin/env swift

import Foundation

let S = Array(readLine()!)

func ans(_ a: Bool, _ b: Bool, _ c: Bool) -> Int {
    if a && b && c { return 3; }
    if a && b { return 2; }
    if b && c { return 2; }
    if a || b || c { return 1; }
    return 0;
}

print(ans(S[0] == "R", S[1] == "R", S[2] == "R"))
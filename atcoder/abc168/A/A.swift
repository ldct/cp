#!/usr/bin/env swift

import Foundation

func ans(_ N: Int) -> String {
    if N == 3 { return "bon" }
    if [0, 1, 6, 8].contains(N) { return "pon" }
    return "hon"
}

let N = Int(readLine()!)! % 10
print(ans(N))

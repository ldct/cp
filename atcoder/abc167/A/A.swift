#!/usr/bin/env swift

import Foundation

func ans(_ A: String, _ B: String) -> String {
    if A.count + 1 != B.count { return "No" }
    if B.starts(with: A) { return "Yes" }
    return "No"
}

let A = readLine()!
let B = readLine()!

print(ans(A, B))
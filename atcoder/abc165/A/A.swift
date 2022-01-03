#!/usr/bin/env swift

import Foundation

func ans(_ K: Int, _ A: Int, _ B: Int) -> String {
    for i in A...B {
        if i % K == 0 { return "OK" }
    }
    return "NG"
}

let K = Int(readLine()!)!
let AB = readLine()!.components(separatedBy: " ")
let A = Int(AB[0])!
let B = Int(AB[1])!
print(ans(K, A, B))
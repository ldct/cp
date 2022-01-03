#!/usr/bin/env swift

import Foundation

extension Array {
    typealias E = Element
    func splat() -> (E,E) { return (self[0],self[1]) }
    func splat() -> (E,E,E) { return (self[0],self[1],self[2]) }
    func splat() -> (E,E,E,E) { return (self[0],self[1],self[2],self[3]) }
    func splat() -> (E,E,E,E,E) { return (self[0],self[1],self[2],self[3],self[4]) }
}

func readInts() -> [Int] {
    readLine()!.split(separator: " ").map { Int($0)! }
}

func readInt() -> Int {
    Int(readLine()!)!
}

extension Int {
    func times(_ f: () -> ()) {
        if self > 0 { for _ in 0..<self { f() } }
    }
}

let (N, Q) = readInts().splat()

let S = Array(readLine()!)

var prefixes = [0, 0]

for i in 1..<S.count {
    var n = prefixes.last!

    if S[i-1] == "A" && S[i] == "C" {
        n += 1
    }

    prefixes.append(n)
}

Q.times {
    var (l, r) = readInts().splat()
    l -= 1
    if S[l] == "C" { l += 1}
    print(prefixes[r] - prefixes[l])
}

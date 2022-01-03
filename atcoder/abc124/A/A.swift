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

extension Int {
    func times(_ f: () -> ()) {
        if self > 0 { for _ in 0..<self { f() } }
    }
}

var (A, B) = readInts().splat()

var ret = 0

2.times {
    if B > A { swap(&A, &B) }
    ret += A
    A -= 1
}

print(ret)
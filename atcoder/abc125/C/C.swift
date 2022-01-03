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

extension Collection {
    func count(where test: (Element) throws -> Bool) rethrows -> Int {
        return try self.filter(test).count
    }
}

extension Sequence where Element: Numeric {
    /// Returns the sum of all elements in the collection
    func sum() -> Element { return reduce(0, +) }
}

func input() {
    let _ = readLine()
}

func gcd(_ a: Int, _ b: Int) -> Int {
    if (a == 0) { return b }
    if (b == 0) { return a }
    let r = a % b
    if r != 0 {
        return gcd(b, r)
    } else {
        return b
    }
}

func gcdPrefix(_ arr: [Int]) -> [Int] {
    var ret = [0]
    for a in arr {
        let p = gcd(ret.last!, a)
        ret.append(p)
    }
    return ret
}

input()
let A = readInts()

let front = gcdPrefix(A)
let back = Array(gcdPrefix(A.reversed()).reversed())

let candidates = (0..<A.count).map { gcd(front[$0], back[$0+1]) }

print(candidates.max()!)

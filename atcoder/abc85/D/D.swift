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

func cdiv(_ x: Int, _ y: Int) -> Int {
    if x % y == 0 {
        return x / y
    } else {
        return x / y + 1
    }
}

var (N, H) = readInts().splat()

var choices = [(Int, Int)]()

N.times {
    let (a, b) = readInts().splat()
    choices.append((a, 0))
    choices.append((b, 1))
}

var ret = 0

choices.sort(by: >)

for p in choices {
    let (d, t) = p
    if t == 0 {
        ret += cdiv(H, d)
        break
    } else {
        ret += 1
        H -= d
    }
    if H <= 0 {
        break
    }
}

print(ret)
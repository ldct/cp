#!/usr/bin/env swift

import Foundation

extension Array {
    typealias E = Element
    func splat() -> (E,E) { return (self[0],self[1]) }
    func splat() -> (E,E,E) { return (self[0],self[1],self[2]) }
    func splat() -> (E,E,E,E) { return (self[0],self[1],self[2],self[3]) }
    func splat() -> (E,E,E,E,E) { return (self[0],self[1],self[2],self[3],self[4]) }
}

func input() {
    let _ = readLine()
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
    func sum() -> Element { return reduce(0, +) }
}

input()
let arr = readInts()

let num_neg = arr.count { $0 < 0 } % 2
let abs_arr = arr.map { abs($0) }.sorted()

if num_neg == 0 {
    print(abs_arr.sum() )
} else {
    print(abs_arr.sum() - 2*abs_arr.min()!)
}

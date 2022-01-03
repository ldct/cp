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

let (A, B, T) = readInts().splat()
print(B * (T / A))
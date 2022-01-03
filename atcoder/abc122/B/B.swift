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

func ok(_ S: String) -> Bool {
    for c in S {
        if !("ATCG".contains(c)) { return false }
    }
    return true
}

let S = Array(readLine()!)

var ret = ""

for i in 0...S.count {
    for j in i...S.count {
        let s = String(S[i..<j])
        if ok(s) && s.count > ret.count {
            ret = s
        }
    }
}

print(ret.count)
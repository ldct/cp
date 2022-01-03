#!/usr/bin/env swift

import Foundation

let S = readLine()!.components(separatedBy: " ").map { Int($0)! }
if S.sum() >= 22 {
    print("bust")
} else {
    print("win")
}

extension Sequence where Element: AdditiveArithmetic {
    func sum() -> Element { reduce(.zero, +) }
}
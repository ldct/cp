#!/usr/bin/env swift

import Foundation

func cdiv(_ x: Int, _ y: Int) -> Int {
    if x % y == 0 {
        return x / y
    } else {
        return x / y + 1
    }
}

let AB = readLine()!.components(separatedBy: " ")
var A = Int(AB[0])!
var B = Int(AB[1])!
print(cdiv(A, B))
#!/usr/bin/env swift

import Foundation

let ST = readLine()!.components(separatedBy: " ")
let S = ST[0]
let T = ST[1]
let AB = readLine()!.components(separatedBy: " ")
var A = Int(AB[0])!
var B = Int(AB[1])!
let U = readLine()!

if U == S {
    A -= 1
} else {
    B -= 1
}

print(A, B)
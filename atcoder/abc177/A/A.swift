#!/usr/bin/env swift

import Foundation

let X = readLine()!.components(separatedBy: " ")
let D = Int(X[0])!
let T = Int(X[1])!
let S = Int(X[2])!

if S*T >= D {
    print("Yes")
} else {
    print("No")
}
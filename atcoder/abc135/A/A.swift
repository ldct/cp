#!/usr/bin/env swift

import Foundation

let AB = readLine()!.components(separatedBy: " ")
var A = Int(AB[0])!
var B = Int(AB[1])!

let K = (A + B) / 2

if abs(A - K) == abs(B - K) {
    print(K)
} else {
    print("IMPOSSIBLE")
}
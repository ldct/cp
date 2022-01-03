#!/usr/bin/env swift

import Foundation

let AB = readLine()!.components(separatedBy: " ")
var A = Int(AB[0])!
var B = Int(AB[1])!

if (A <= 9 && B <= 9) {
    print(A*B)
} else {
    print(-1)
}
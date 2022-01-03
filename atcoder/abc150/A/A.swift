#!/usr/bin/env swift

import Foundation

let KX = readLine()!.components(separatedBy: " ")
var K = Int(KX[0])!
var X = Int(KX[1])!

if K * 500 >= X {
    print("Yes")
} else {
    print("No")
}

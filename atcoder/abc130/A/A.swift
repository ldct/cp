#!/usr/bin/env swift

import Foundation

let XA = readLine()!.components(separatedBy: " ")
var X = Int(XA[0])!
var A = Int(XA[1])!

if X < A {
    print(0)
} else {
    print(10)
}
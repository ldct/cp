#!/usr/bin/env swift

import Foundation

let XYZ = readLine()!.components(separatedBy: " ")
var X = Int(XYZ[0])!
var Y = Int(XYZ[1])!
var Z = Int(XYZ[2])!

swap(&X, &Y)
swap(&X, &Z)

print(X, Y, Z)
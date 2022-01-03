#!/usr/bin/env swift

import Foundation

let NAB = readLine()!.components(separatedBy: " ")
var N = Int(NAB[0])!
var A = Int(NAB[1])!
var B = Int(NAB[2])!

print(min(B, N*A))
#!/usr/bin/env swift

import Foundation

let ab = readLine()!.components(separatedBy: " ")
let n = Int(ab[0])!
let a = Int(ab[1])!
let b = Int(ab[2])!
print(n + b - a)

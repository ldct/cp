#!/usr/bin/env swift

import Foundation

let NM = readLine()!.components(separatedBy: " ")
let N = Int(NM[0])!
let M = Int(NM[1])!
print((N*(N-1) + M*(M-1)) / 2)
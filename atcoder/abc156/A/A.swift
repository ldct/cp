#!/usr/bin/env swift

import Foundation

let KR = readLine()!.components(separatedBy: " ")
let K = min(10, Int(KR[0])!)
let R = Int(KR[1])!

print(R + 100*(10 - K))
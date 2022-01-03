#!/usr/bin/env swift

import Foundation

let ABC = readLine()!.components(separatedBy: " ")
var A = Int(ABC[0])!
var B = Int(ABC[1])!
var C = Int(ABC[2])!

C -= (A - B)
print(max(0, C))
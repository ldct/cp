#!/usr/bin/env swift

import Foundation

let AB = readLine()!.components(separatedBy: " ")
var A = Int(AB[0])!
var B = Int(AB[1])!

print(max(0, A - 2*B))
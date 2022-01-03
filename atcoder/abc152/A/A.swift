#!/usr/bin/env swift

import Foundation

let AB = readLine()!.components(separatedBy: " ")
var A = Int(AB[0])!
var B = Int(AB[1])!

if A == B {
    print("Yes")
} else {
    print("No")
}
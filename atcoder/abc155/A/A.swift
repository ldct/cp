#!/usr/bin/env swift

import Foundation

let elems = Set(readLine()!.components(separatedBy: " ").map { Int($0)! })

if elems.count == 2 {
    print("Yes")
} else {
    print("No")
}
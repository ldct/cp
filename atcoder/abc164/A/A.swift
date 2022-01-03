#!/usr/bin/env swift

import Foundation

let SW = readLine()!.components(separatedBy: " ")
let S = Int(SW[0])!
let W = Int(SW[1])!
if S <= W {
    print("unsafe")
} else {
    print("safe")
}

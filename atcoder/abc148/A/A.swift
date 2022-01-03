#!/usr/bin/env swift

import Foundation

let A = Int(readLine()!)!
let B = Int(readLine()!)!

print(Array(Set([1, 2, 3]).symmetricDifference(Set([A, B])))[0])
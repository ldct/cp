#!/usr/bin/env swift

import Foundation

let S = Array(readLine()!)

if S[0] == S[1] || S[1] == S[2] || S[2] == S[3] {
    print("Bad")
} else {
    print("Good")
}
#!/usr/bin/env swift

import Foundation

var S = Array(readLine()!)
S.sort()
if (S[0] == S[1] && S[2] == S[3] && S[0] != S[3]) {
    print("Yes")
} else {
    print("No")
}

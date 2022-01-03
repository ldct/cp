#!/usr/bin/env swift

import Foundation

let S = readLine()!
if S.last == "s" {
    print(S + "es")
} else {
    print(S + "s")
}

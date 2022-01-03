#!/usr/bin/env swift

import Foundation

let days = "SUN,MON,TUE,WED,THU,FRI,SAT".components(separatedBy: ",")
let i = days.firstIndex(of: readLine()!)!
print(7-i)
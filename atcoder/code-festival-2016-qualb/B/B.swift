import Foundation

let NAB = readLine()!.components(separatedBy: " ")
let S = readLine()!

let N = Int(NAB[0])!
let A = Int(NAB[1])!
let B = Int(NAB[2])!

var curr_passed = 0
var curr_b_rank = 0

for c in S {
    switch c {
    case "a": do {
        if curr_passed < A + B {
            print("Yes")
            curr_passed += 1
        } else {
            print("No")
        }
    }
    case "b": do {
        curr_b_rank += 1
        if curr_passed < A + B, curr_b_rank <= B {
            print("Yes")
            curr_passed += 1
        } else {
            print("No")
        }
    }
    case "c": do {
        print("No")
    }
    default:
        assert(false)
    }
}

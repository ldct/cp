import Foundation

let NMC = readLine()!.components(separatedBy: " ")

let N = Int(NMC[0])!
let M = Int(NMC[1])!
let C = Int(NMC[2])!

let B = readLine()!.components(separatedBy: " ").map { Int($0)! }

func passes(_ A: Array<Int>) -> Bool {
    var sum = 0
    for i in 0..<M {
        sum += A[i]*B[i]
    }
    sum += C
    return sum > 0
}


var ret = 0

for _ in 0..<N {
    let A = readLine()!.components(separatedBy: " ").map { Int($0)! }
    // print(A, B, passes(A))
    if passes(A) {
        ret += 1
    }
}

print(ret)
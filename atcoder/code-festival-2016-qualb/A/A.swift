import Swift

let S = readLine()!
let correct = "CODEFESTIVAL2016"

var ret = 0

for i in correct.indices {
    if correct[i] != S[i] {
        ret += 1
    }
}


print(ret)
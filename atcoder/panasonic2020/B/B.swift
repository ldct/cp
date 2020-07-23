import Foundation

let HW = readLine()!.components(separatedBy: " ")

let H = Int(HW[0])!
let W = Int(HW[1])!

let (W1, _) = W.quotientAndRemainder(dividingBy: 2)
let (W2, _) = (W+1).quotientAndRemainder(dividingBy: 2)

if (H == 1 || W == 1) {
    print(1)
} else if (H % 2 == 0) {
    let HH = UInt64(H/2)
    print(HH*UInt64(W1+W2))
} else {
    let HH = UInt64((H-1)/2)
    print(HH*UInt64(W1+W2) + UInt64(W2))
}

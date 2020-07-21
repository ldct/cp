import Foundation

let N = Int(readLine()!)!

func ans(N: Int) -> String {
    for i in 0..<50001 {
        if Int((Double(i)*1.08).rounded(.down)) == N {
            return String(i)
        }
    }
    return ":("
}

print(ans(N: N))

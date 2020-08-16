import Foundation

let T = Int(readLine()!)!

func ans(_ trees : [(Int, Int)]) -> Int {
    var tree_at = Dictionary<Int, Int>()

    for (p, h) in trees {
        tree_at[p] = h
    }

    var lr = Dictionary<Int, Int>()
    for p in tree_at.keys.sorted() {
        let h = tree_at[p]!
        lr[p+h] = max((lr[p+h] ?? 0), (lr[p] ?? 0) + h)
    }

    var ll = Dictionary<Int, Int>()
    for p in tree_at.keys.sorted().reversed() {
        let h = tree_at[p]!
        ll[p-h] = max((ll[p-h] ?? 0), (ll[p] ?? 0) + h)
    }

    for p in lr.keys {
        ll[p] = (ll[p] ?? 0) + lr[p]!
    }

    return ll.values.max() ?? 0
}

for t in 0..<T {
    let N = Int(readLine()!)!

    var trees = [(Int, Int)]()

    for _ in 0..<N {
        let PH = readLine()!.components(separatedBy: " ")
        let P = Int(PH[0])!
        let H = Int(PH[1])!
        trees.append((P, H))
    }
    print("Case #\(t+1): \(ans(trees))")
}

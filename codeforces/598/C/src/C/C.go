package main

import "fmt"
import "math/big"

func main() {
  var n int
  fmt.Scanf("%d\n", &n)

  var tanθs [100]big.Rat

  for i := 0; i < n; i++ {
    var a int64
    var b int64
    fmt.Scanf("%d %d\n", &a, &b)
    var tanθ big.Rat
    tanθ = *big.NewRat(a, b)

  }
  fmt.Printf("%d\n", n)
}

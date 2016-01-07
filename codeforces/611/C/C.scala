import scala.collection.mutable.ArrayBuffer
import scala.collection.mutable.Map
import java.util.Scanner

object C {

  def main(args: Array[String]): Unit = {

    val sc = new Scanner(System.in)

    val h = sc.nextInt()
    val w = sc.nextInt()

    sc.nextLine()

    val grid = ArrayBuffer[String]();

    (0 until h).foreach((i) => {
      grid += sc.nextLine()
    })

    def isHGood(r:Int, c:Int) = {
      if (c == w)
        false
      else
        grid(r-1)(c-1) == '.' && grid(r-1)(c) == '.'
    }

    def isVGood(r: Int, c:Int) = {
      if (r == h)
        false
      else
        grid(r-1)(c-1) == '.' && grid(r)(c-1) == '.'
    }

    var numHGoodMemo = Map[(Int, Int), Int]()

    def numHGood(r: Int, c: Int):Int = {

      val key = (r, c)
      if (numHGoodMemo.isDefinedAt(key)) {
        numHGoodMemo.get(key).get
      } else if (r <= 1) {
        var ans = 0
        (1 to r).foreach(x => {
          (1 to c).foreach(y => {
            if (isHGood(x, y)) ans += 1
          })
        })
        numHGoodMemo.update(key, ans)
        ans
      } else {
        var ans = numHGood(r-1, c);
        (1 to c).foreach(y => {
          if (isHGood(r, y)) ans += 1
        })
        numHGoodMemo.update(key, ans)
        ans
      }
    }

    var numVGoodMemo = Map[(Int, Int), Int]()

    def numVGood(r: Int, c: Int):Int = {

      val key = (r, c)
      if (numVGoodMemo.isDefinedAt(key)) {
        numVGoodMemo.get(key).get
      } else if (r <= 1) {
        var ans = 0
        (1 to r).foreach(x => {
          (1 to c).foreach(y => {
            if (isVGood(x, y)) ans += 1
          })
        })
        numVGoodMemo.update(key, ans)
        ans
      } else {
        var ans = numVGood(r-1, c)
        (1 to c).foreach(y => {
          if (isVGood(r, y)) ans += 1
        })
        numVGoodMemo.update(key, ans)
        ans
      }


    }

    def numHGood4(r1:Int, c1:Int, r2:Int, c2:Int):Int = {
      numHGood(r2, c2) - numHGood(r1-1, c2) - numHGood(r2, c1-1) + numHGood(r1-1, c1-1)
    }

    def numVGood4(r1:Int, c1:Int, r2:Int, c2:Int):Int = {
      numVGood(r2, c2) - numVGood(r1-1, c2) - numVGood(r2, c1-1) + numVGood(r1-1, c1-1)
    }

    def numDominoes(r1:Int, c1:Int, r2:Int, c2:Int):Int = {
      numHGood4(r1, c1, r2, c2-1) + numVGood4(r1, c1, r2-1, c2)
    }

    val q = sc.nextInt()

    (0 until q).foreach(_ => {
      val r1 = sc.nextInt()
      val c1 = sc.nextInt()
      val r2 = sc.nextInt()
      val c2 = sc.nextInt()
      println(numDominoes(r1, c1, r2, c2))
    })

  }

}

object Solution extends App {

  def f(n: Int) = {
    for(i <- 0 to n - 1)
    {
      println("Hello World")
    }
  }

  var n = scala.io.StdIn.readInt
  f(n)
}

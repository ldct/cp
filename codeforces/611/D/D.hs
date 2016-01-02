module Main where

import Data.Function (fix)

p::Integer
p = 10^9 + 7

slice from to xs = take (to - from) (drop from xs)

ways::Integer->Int
ways x = numWays (show x) 0 1

numWays::String->Int->Integer->Int
-- number of ways to split s[a:] where the first thing is at least minimumStarting
numWays s a minimumStarting
  | length s == a = 1
  | s !! a == '0' = 0
  | otherwise = sum (map f [(a+1)..(length s)])
  where
    f i
      | firstPart >= minimumStarting = numWays s i (minimumStarting + 1)
      | otherwise = 0
      where firstPart = read (slice a i s)


main = do
  print (slice 1 2 "abcdef")
  _ <- getLine
  s <- readLn
  print (ways s)

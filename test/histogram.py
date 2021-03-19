#!/usr/bin/env pypy3

def largestRectangleArea(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        print(stack)
        while height[i] < height[stack[-1]]:
            print("hi")
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans

largestRectangleArea([1,2,3,4,5])
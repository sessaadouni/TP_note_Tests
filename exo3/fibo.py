def fibo_r(n: int) -> int:
  if n == 0: return 1
  elif n == 1: return 1
  else: return fibo_r(n - 2) + fibo_r(n - 1)

def fibo_i(n: int) -> int:
  stack = [1, 1]
  for i in range(2, n+1):
    fib_i = stack[i - 2] + stack[i -1]
    stack.append(fib_i)
  return stack[-1]
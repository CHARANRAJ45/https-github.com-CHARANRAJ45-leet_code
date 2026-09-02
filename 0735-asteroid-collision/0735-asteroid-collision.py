class Solution:

  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    for ast in asteroids:
      alive = True
      while alive and ast < 0 and stack and stack[-1] > 0:
        if stack[-1] < abs(ast):
          stack.pop()  # Top asteroid explodes, keep checking against the next one
        elif stack[-1] == abs(ast):
          stack.pop()  # Both explode
          alive = False  # Current asteroid is also destroyed
        else:
          alive = False  # Current asteroid explodes against a larger positive one

      if alive:
        stack.append(ast)

    return stack
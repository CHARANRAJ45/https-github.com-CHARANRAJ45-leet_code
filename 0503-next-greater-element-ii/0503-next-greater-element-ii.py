class Solution:

  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    stack = []
    n = len(nums)
    ans = [-1] * n

    for i in range(2 * n - 1, -1, -1):
      # Compare stack's top value using its index: nums[stack[-1]] <= nums[i % n]
      while len(stack) != 0 and nums[stack[-1]] <= nums[i % n]:
        stack.pop()

      if i < n:
        if len(stack) != 0:
          ans[i] = nums[stack[-1]]  # Assign the actual greater value

      stack.append(i % n)  # Store the index in the stack

    return ans
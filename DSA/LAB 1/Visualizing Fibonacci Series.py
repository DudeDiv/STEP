class RecursionVisualizer:
  def __init__(self):
    self.indent = 0

  def log(self, message):
    print(" " * self.indent + message)

  # Add the fibonacci method
  def fibonacci(self, n):
    self.log(f"fibonacci({n}) called")
    self.indent += 2
    if n == 0:
      self.log("Return 0 (base case)")
      self.indent -= 2
      return 0
    elif n == 1:
      self.log("Return 1 (base case)")
      self.indent -= 2
      return 1
    res = self.fibonacci(n-1) + self.fibonacci(n-2)
    self.indent -= 2
    self.log(f"Return {res} from fibonacci ({n})")
    return res

  # Add the visualize_fibonacci method
  def visualize_fibonacci(self, n):
    self.indent = 0
    print(f"\n--- Visualizing Fibonacci({n}) ---")
    result = self.fibonacci(n)
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
  visualizer = RecursionVisualizer()
  visualizer.visualize_fibonacci(5) # Example call for Fibonacci

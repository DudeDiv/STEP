class RecursionVisualizer:
  def __init__(self):
    self.indent = 0

  def log(self, message):
    print(" " * self.indent + message)

  # Define factorial as a method within the class
  def factorial(self, n):
    self.log(f"factorial({n}) called")
    self.indent += 2
    if n==0 or n==1:
      self.log("Return 1 (base case)")
      self.indent -= 2
      return 1
    # Call the factorial method using self.factorial
    res = n*self.factorial(n-1)
    self.indent -= 2
    self.log(f"Return {res} from factorial ({n})")
    return res

  # Define visualize_factorial as a method within the class
  def visualize_factorial(self, n):
    self.indent = 0
    print(f"\n--- Visualizing Factorial({n}) ---")
    # Call the factorial method using self.factorial
    result = self.factorial(n)
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
  visualizer = RecursionVisualizer()
  # Now visualize_factorial is a method of the visualizer object
  visualizer.visualize_factorial(3)

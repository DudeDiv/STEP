class RecursionVisualizer:
  def __init__(self):
    self.indent = 0

  def log(self, message):
    print(" " * self.indent + message)

  def sum_array(self, arr, index):
    self.log(f"sum_array({arr}, {index}) called")
    self.indent += 2
    if index >= len(arr):
      self.log("Return 0 (base case)")
      self.indent -= 2
      return 0
    res = arr[index] + self.sum_array(arr, index+1)
    self.indent -= 2
    self.log(f"Return {res} from sum_array ({arr}, {index})")
    return res

  def visualize_sum_array(self, arr, start_index):
    self.indent = 0
    print(f"\n--- Visualizing Sum of Array({arr}, starting from index {start_index}) ---")
    result = self.sum_array(arr, start_index)
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
  visualizer = RecursionVisualizer()
  # Example call for Sum of Array
  my_array = [1, 2, 3, 4, 5]
  visualizer.visualize_sum_array(my_array, 0)

class RecursionVisualizer:
  def __init__(self):
    self.indent = 0
  def log(self, message):
    print(" " * self.indent + message)

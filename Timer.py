import time

def count_down(timer):
  start_time = time.time()

  # The thing to time. Using sleep as an example
  time.sleep(timer)

  end_time = time.time()
  elapsed_time = end_time - start_time

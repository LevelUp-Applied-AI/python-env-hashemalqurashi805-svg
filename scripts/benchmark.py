import time
import platform
import os

def simple_benchmark():
    print(f"--- System Info ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"--- Running Benchmark ---")
    
    start_time = time.time()
    # عملية حسابية بسيطة للقياس
    _ = [x**2 for x in range(10**7)]
    end_time = time.time()
    
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    simple_benchmark()

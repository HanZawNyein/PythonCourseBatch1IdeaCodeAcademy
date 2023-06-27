from time import sleep as tsp,perf_counter
from fake_package import sleep as sp


if __name__ == "__main__":
    start = perf_counter()
    tsp(1)
    result = perf_counter() - start
    print(f"result : {result} seconds")
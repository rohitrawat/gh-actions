import time
import aiohttp


def func():
    print(time.time())
    print(dir(aiohttp))
    print("Hello world!")


if __name__ == "__main__":
    func()

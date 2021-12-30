from hoopoe import Hoopoe

hoopoe = Hoopoe(
    api_key="vi3xJh7R.rYtoTgLi2SeQP8GCCjxNjBHJjMEeiSUy",
    version=1,
    base_url="http://localhost:8000/api",
)
print(hoopoe.timestamp())
print(hoopoe.upupa("Hello World!"))

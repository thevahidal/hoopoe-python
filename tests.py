from hoopoe import Hoopoe

hoopoe = Hoopoe(
    api_key="123456789",
    version=1,
    base_url="http://localhost:8000/api",
)
print(hoopoe.timestamp())
print(hoopoe.upupa("Hello World!"))

from decouple import config

from hoopoe import Hoopoe

hoopoe = Hoopoe(
    api_key=config("API_KEY"),
    version=config("VERSION", default="1"),
    base_url=config("BASE_URL", default="https://api.hoopoe.com"),
)
print(hoopoe.timestamp())
print(hoopoe.upupa("Hello World!"))

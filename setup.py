import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="hoopoe-python",
    version="0.0.2",
    description="Python SDK for Hoopoe",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/thevahidal/hoopoe-python",
    author="Vahid Al",
    author_email="thevahidal@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["requests",],
    entry_points={
        "console_scripts": [
        ]
    },
)
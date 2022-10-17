from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calculator",
    version="0.0.3",
    description="Simple python calculator",
    long_description=long_description,
    author="dqmis <dom.seputis@gmail.com>",
    url="https://github.com/dqmis/simple_python_project",
    python_require=">=3.9",
    install_requires=["numpy>=1.23.4"],
)

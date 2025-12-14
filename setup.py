"""Setup file for the power-bi-python-api library."""

from setuptools import setup
from setuptools import find_namespace_packages

# Open the README file.
with open(file="README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-power-bi",

    # Define Author Info.
    author="Alex Reed",
    author_email="coding.sigma@gmail.com",

    # Define Version Info.
    version="0.1.2",

    # Define descriptions.
    description="The Unofficial Python API wrapper for the Microsoft Power BI REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Define repo location.
    url="https://github.com/areed1192/power-bi-python-api.git",

    # Define dependencies.
    install_requires=["msal>=1.31.1", "requests>=2.32.3"],

    # Specify folder content.
    packages=find_namespace_packages(include=["powerbi"]),

    # Define the python version.
    python_requires=">3.7"
)

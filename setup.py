import setuptools
from setuptools import find_packages


requirements = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name = "deepcheck",
    version = "0.0.1",
    author = "PhospheneAI",
    author_email = "sanjith.kumar@phospheneai.com",
    description = "baseline deepcheck module",
    url = "https://github.com/SANJITH-KUMAR-20/SizeInvariantTransformer-for-Deepfake-detection",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
    classifiers = [
        "Programming Language :: Python :: 3.11"
    ],
    python_requires = ">=3.11"
)
import setuptools

setuptools.setup(
    name = "deepcheck",
    version = "0.0.1",
    author = "PhospheneAI",
    author_email = "sanjith.kumar@phospheneai.com",
    description = "baseline deepcheck module",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.11"
)
from setuptools import setup, find_packages

setup(
    name="chroma-log",
    version="0.1.0",
    author="volksgeistt",
    author_email="unrealvolksgeist@gmail.com",
    description="A good and flexible text color logging module for your productivity and a better coding experience.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/volksgeistt/chroma-log",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

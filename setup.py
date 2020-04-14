import setuptools

with open("README.md", "r") as r:
    long_description = r.read()
long_description = ""

setuptools.setup(
    name="pandasbt",
    version="0.1.0",
    author="Janderson FFerreira",
    author_email="ffjanderson@gmail.com",
    description="Simple framework to test your strategies ideias with pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6',
)

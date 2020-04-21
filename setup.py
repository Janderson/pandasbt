import setuptools

with open("README.md", "r") as r:
    long_description = r.read()

setuptools.setup(
    name="pandasbt",
    version="0.2.0",
    author="Janderson FFerreira",
    author_email="ffjanderson@gmail.com",
    description="Simple framework to test your strategies ideias with pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Janderson/pandasbt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BinHexDenOctConversions-TBowen",
    version="1.0",
    author="TBowen",
    author_email="autisticgamelover@gmail.com",
    description="A package that converts between binary, hexadecimal, decimal and octal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
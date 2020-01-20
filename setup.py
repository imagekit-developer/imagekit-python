import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imagekitio",
    version="2.0.0",
    description="Python wrapper for the ImageKit API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests==2.20.1'],
    url="https://github.com/imagekit-developer/imagekit-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

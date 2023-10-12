import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements/requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="imagekitio",
    version="3.2.0",
    description="Python wrapper for the ImageKit API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    url="https://github.com/imagekit-developer/imagekit-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

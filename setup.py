import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locations",
    version="1.1.1",
    author="Ashish Mishra",
    author_email="ashishmishra.dev04@gmail.com",
    description="This library will be used to extract usa location",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Coderboy004/locations",
    project_urls={
        "Homepage": "https://github.com/Coderboy004/locations",
        "Bug Tracker": "https://github.com/Coderboy004/locations/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "locations"},
    packages=setuptools.find_packages(where="locations"),
    python_requires=">=3.7"
)

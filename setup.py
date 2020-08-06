

import setuptools

REQUIRED = [
    "numpy",
    "pandas",
    "datetime"
]

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
setuptools.setup(
    name="lambdata-dondreojordan",
    version="0.0.7",
    author="dondreojordan",
    author_email="dondreojordan@gmail.com",
    description="A Collection of Data Science Helper Functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/dondreojordan/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
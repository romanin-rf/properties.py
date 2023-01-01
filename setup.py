import setuptools

setuptools.setup(
    name="properties.py",
    keywords=["properties", "java"],
    version="1.0.1",
    description="Module for reading and writing properties-files.",
    long_description=open("README.md", "r", errors="ignore").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/romanin-rf/properties.py",
    author="Romanin",
    author_email="semina054@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9"
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AVMSpeechMath",
    version="0.0.5",
    author="AlejandroV",
    author_email="avmmodules@gmail.com",
    description="Perform voice operations in Spanish with Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avmmodules/AVMSpeechMath",
    project_urls={
        "Bug Tracker": "https://github.com/avmmodules/AVMSpeechMath/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
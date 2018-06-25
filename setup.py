import setuptools

# Read in the README file, for the long_description.
with open("README.markdown", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="letterboxd",
    packages=setuptools.find_packages(),
    version="0.1.0",
    description="Python 3.6+ wrapper for the Letterboxd API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mark Boszko",
    author_email="mboszko@mac.com",
    copyright="Copyright (c) 2018 Mark Boszko",
    url="https://github.com/bobtiki/letterboxd/",
    download_url="",
    keywords=[
        "api",
        "movies",
    ],  # movie, the movie database, movie database, tmdb, wrapper, database, themoviedb, moviedb, api
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    license="MIT",
)

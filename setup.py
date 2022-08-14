from setuptools import setup
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="iclib",
    version="1.0.0",
    description="Islamic Calculation Library (ICLib) contains calculations for prayer (salat) times, qibla direction, and Hijri conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DwcTeam/iclib-python",
    author="DwcTeam (forked from Fikr4n)",
    author_email="hazemmeqdad@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="islamic, prayer, salat, qibla, hijri",
    packages=["iclib", "iclib.hijri"],
    install_requires=[],
    project_urls={
        "Bug Reports": "https://github.com/fikr4n/iclib-python/issues",
        "Source": "https://github.com/fikr4n/iclib-python",
        "Documentation": "https://github.com/fikr4n/iclib-python#readme"
    },
)

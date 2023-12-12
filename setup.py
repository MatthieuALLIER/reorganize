from setuptools import find_packages, setup

setup(
    name="reorganize",
    version="0.1.0",
    description="Reorganize Python project",
    author="Matthieu ALLIER",
    author_email="alrmatth@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "reorganize = reorganize:main",
        ],
    },
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
)

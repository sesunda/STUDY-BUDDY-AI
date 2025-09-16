from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="study_buddy_ai",
    version="0.1",
    author="Senthilkumar",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
)

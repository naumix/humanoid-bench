from pathlib import Path
from setuptools import find_packages, setup


long_description = (Path(__file__).parent / "README.md").read_text()

core_requirements = [
    "rich==13.7.1",
    "tqdm==4.66.4",
    "ipdb==0.13.13",
    "natsort==8.4.0",
]

setup(
    name="humanoid_bench",
    version="0.2",
    author="RLL at UC Berkeley",
    url="https://github.com/carlosferrazza/humanoid-bench",
    description="Humanoid Benchmark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">3.7",
    install_requires=core_requirements,
)

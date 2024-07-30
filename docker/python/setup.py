from setuptools import find_packages, setup

setup(
    name="get-image-size",
    version="0.0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["get-image-size=src.get_image_size:main"]},
)

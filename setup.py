from setuptools import find_packages, setup

packages = [
    'lift'
]

setup(
    name="lift",
    version=f"14.0.2",
    packages=packages,
    include_package_data=True,
    license="MIT License",
    description="lift",
    keywords="lift",
    url="https://github.com/bytebuildz/liftcord.py-tools/",
    author=".drmr",
    author_email="hi@icey.fr",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
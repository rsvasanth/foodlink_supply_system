from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in foodlink_supply_system/__init__.py
from foodlink_supply_system import __version__ as version

setup(
	name="foodlink_supply_system",
	version=version,
	description="Foodlink supply system",
	author="rsvasanth",
	author_email="rsvasanth@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tshotel/__init__.py
from tshotel import __version__ as version

setup(
	name="tshotel",
	version=version,
	description="hotel management",
	author="sibi",
	author_email="sibikumar@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

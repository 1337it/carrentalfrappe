from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in car_reservation/__init__.py
from car_reservation import __version__ as version

setup(
	name="car_reservation",
	version=version,
	description="Vehicle & Car Reservation System Manages Vehicle Reservations and tracks locations on Google map.",
	author="Solufy",
	author_email="contact@solufy.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

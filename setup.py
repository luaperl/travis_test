from setuptools import setup, find_packages

setup(
	name = 'ngh_func',
	version = '0.0.1',
	author = 'ngh',
	packages = find_packages(exclude=['test']),
	zip_safe = False,
)

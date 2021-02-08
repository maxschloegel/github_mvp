import setuptools

with open("README.md, "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="example-pkg-max_mustermann_1337",
	version="0.0.1",
	author="Max Mustermann",
	author_mail="maxmustermann@example.com",
	description="Testing packaging",
	long_description=long_description,
	url="",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
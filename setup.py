# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lamdata-deja", # the name that you will install via pip
    version="1.01",
    author="Jake Dennis",
    author_email="jakedennis877@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/imdeja/lamdata-imdeja",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
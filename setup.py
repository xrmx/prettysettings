import os
from setuptools import setup, find_packages

def read(fname):
    desc = ''
    try:
        desc = open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        pass

    return desc

setup(
    name = "prettysettings",
    version = "1.2",
    packages = find_packages(),
    long_description=read('README.md'),
    # metadata for upload to PyPI
    author = "Stefano Terna",
    author_email = "stefano.terna@tomorrowdata.io",
    description = "This package provides a minimal class for pretty settings management.",
    license = "Apache License, Version 2.0",
    keywords = "pretty settings management",
    url = "https://github.com/iottly/prettysettings",   

)
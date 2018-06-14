from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    package_data={
        'quotesbot': ['resources/*.txt']
    },
    entry_points={
        'scrapy': ['settings = quotesbot.settings']
    },
    zip_safe=False,
)

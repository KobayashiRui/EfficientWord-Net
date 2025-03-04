from setuptools import setup
from glob import glob

setup(
    name = 'EfficientWord-Net',
    version = '1.0.2',
    description = 'Few Shot Learning based Hotword Detection Engine',
    long_description = open("./README.md",'r').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Ant-Brain/EfficientWord',
    #py_modules = ['efficientword'],
    packages = ['eff_word_net'],
    install_requires = open("./requirements.txt",'r').read().split("\n"),
    classifiers = [
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    include_package_data=True,
)


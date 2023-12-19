from setuptools import setup, find_namespace_packages

setup(
    name='CLI_BOT_CC23',
    version='0.0.1',
    description='Command bot that do operations with storing contacts and notes.',
    url='https://github.com/DmytroSDV/code_crafters_core.git',
    author='Code Crafters',
    author_email='code_crafters@python.ua',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License"],
    license='MIT',
    packages=find_namespace_packages(),
    data_files=[("code_crafters_core23", ['code_crafters_core23\database.bin', 'code_crafters_core23\notebase.bin'])],
    include_package_data = True,
    install_requires=['emoji', 'tabulate', 'unidecode', 'prompt_toolkit'],
    entry_points={'console_scripts': ['codecrafters = code_crafters_core23.main:main']}
)
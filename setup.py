from setuptools import setup, find_namespace_packages


setup(
    name='Bot_Jul_CC23',
    version='1.3.130',
    description='Command bot that do operations with storing contacts and notes.',
    url='https://github.com/DmytroSDV/code_crafters_core.git',
    author='Code Crafters',
    author_email='code_crafters@python.ua',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License"],
    license='MIT',
    packages=find_namespace_packages(),
    data_files=[("CODE_CRAFTERS_CORE", ['CODE_CRAFTERS_CORE\database.bin', 'CODE_CRAFTERS_CORE\notebase.bin'])],
    include_package_data = True,
    install_requires=['emoji', 'tabulate', 'unidecode', 'prompt_toolkit'],
    entry_points={'console_scripts': ['jul_run = CODE_CRAFTERS_CORE.main:main']}
)
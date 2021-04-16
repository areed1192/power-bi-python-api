from setuptools import setup
from setuptools import find_namespace_packages

# Open the README file.
with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(

    name='python-power-bi',

    # Define Author Info.
    author='Alex Reed',
    author_email='coding.sigma@gmail.com',

    # Define Version Info.
    version='0.1.1',

    # Define descriptions.
    description='The Unofficial Python API wrapper for the Microsoft Power BI REST API.',
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Define repo location.
    url='https://github.com/areed1192/power-bi-python-api.git',

    # Define dependencies.
    install_requires=[
        'msal==1.5.0',
        'requests==2.24.0'
    ],

    # Specify folder content.
    packages=find_namespace_packages(
        include=['powerbi']
    ),

    # Define the python version.
    python_requires='>3.7',

    # Define our classifiers.
    classifiers=[

        # Phase of development my library is in.
        'Development Status :: 3 - Alpha',

        # Audience this library is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',

        # License that guides my library.
        'License :: OSI Approved :: MIT License',

        # Package was written in English.
        'Natural Language :: English',

        # Operating systems.
        'Operating System :: OS Independent',

        # Programming Languages Used..
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        # Topics.
        'Topic :: Database',
        'Topic :: Education',
        'Topic :: Office/Business'
    ]

)

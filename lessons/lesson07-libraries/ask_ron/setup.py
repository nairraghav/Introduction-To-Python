from ask_ron import VERSION
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ask_ron",  # Replace with your own username
    version=VERSION,  # Don't forget to bump your version when making changes after deploying
    author="Raghav Nair",  # Replace with your name
    author_email="nairraghav@hotmail.com",  # Replace with your email
    description="A basic 8 ball library that generates random output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nairraghav/ron-cipher",  # this should be your github url
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',  # Mandates any requirements (Example: if using F-Strings, force 3.6+)
    entry_points={  # if you want CLI behavior, use this
        'console_scripts': ['ask_ron=ask_ron:main'],
    }
)
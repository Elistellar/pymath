from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pymath',
    author='Elistellar',
    author_email='elistellar.contact@gmail.com',
    version='0.0.1',
    description='A python lirbary adding some maths objects like lines, segments or polygons.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Elistellar/pymath',
    keywords=['math', 'intersection'],
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.7' # TODO: find the real version instead of a random one
)

# local install -> pip install .
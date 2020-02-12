from distutils.core import setup

setup(
    name='Tweetgenerator',
    version='0.1dev',
    packages=['tweetgen',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    package_dir={'': 'lib'},
    data_files=[('data', ['data/firstname.txt'], ['data/lastname.txt'])],
    url='https://github.com/hamelinboyerj/tweetgen',
)

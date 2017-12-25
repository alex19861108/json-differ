from setuptools import setup, find_packages
NAME = 'src'
PACKAGES = find_packages(NAME)
setup(
    name='json_differ',
    version='1.0',
    packages=PACKAGES,
    package_dir={'': 'src'},
    package_data={},
    setup_requires=[],
    install_requires=[],
    entry_points={},
    author='liuwei02',
    author_email='liuwei02@megvii.com',
    description='tool for json diff',
    keywords='json diff',
    url=''
)
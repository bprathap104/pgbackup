from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgpackup',
    version='0.1.0',
    author='Saran',
    author_email='bprathap104@gmail.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bprathap104/pgbackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_Requires=['boto3'],
    python_requires='>=3.6',
        entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ],
    }
)
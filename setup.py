from setuptools import setup, find_packages

setup(
    name='alex_nin_module',
    version='0.1',
    packages=find_packages(),
    description='Module finds statistical data',
    author='Alex Nin',
    author_email='1098493@uvu.edu',
    install_requires=[
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.12',
    
)
from setuptools import setup, find_packages

setup(
    name='cnn-classifier-industrial',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='An industrial-grade CNN classifier for image classification tasks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cnn-classifier-industrial',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tensorflow>=2.0.0',
        'numpy>=1.18.0',
        'matplotlib>=3.0.0',
        'pandas>=1.0.0',
        'scikit-learn>=0.22.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
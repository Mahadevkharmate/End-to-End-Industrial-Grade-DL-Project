# allows publishing your project to PyPi

from setuptools import setup, find_packages

#to show package related description like PyPi pkg we can read README.md file as long discription
with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

AUTHER_USER_NAME = "Mahadevkharmate"
SRC_REPO = "CNNClassifier"
AUTHER_EMAIL = "mahadev.mk294@gmail.com"

setup(
    name='End-to-End-Industrial-Grade-DL-Project',
    version='0.1.0', #version of your project/model
    author=AUTHER_USER_NAME,
    author_email=AUTHER_EMAIL,
    description='An industrial-grade CNN classifier for image classification tasks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Mahadevkharmate/End-to-End-Industrial-Grade-DL-Project',
    project_urls={
        "Bug Tracker": f"https://github.com/Mahadevkharmate/End-to-End-Industrial-Grade-DL-Project/issues"
    },
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
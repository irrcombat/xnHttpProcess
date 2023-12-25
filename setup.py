import os

from setuptools import setup, find_packages

install_requires = None
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       "requirements.txt"), 'r') as fp:
    install_requires = fp.readlines()


setup(
    name="xnHttpProcess",
    version="0.9",
    author="net.0xn",
    author_email="irrcombat@gmail.com",
    description="python Http Process",
    url="https://github.com/irrcombat/xnHttpProcess.git",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

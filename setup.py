from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()  # This removes \n automatically
    
    # Filter out empty lines and '-e .'
    requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Vinay Yadam',
    author_email='vinay.y21@iiits.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

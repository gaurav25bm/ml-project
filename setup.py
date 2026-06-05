from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

    

from setuptools import find_packages, setup

setup(
    name='mlproject', # Avoid hyphens in the package name string here
    version='0.0.1',
    author='Gaurav',
    packages=find_packages(),
    install_requires=[] # If you are parsing requirements.txt here, ensure it isn't reading a blank line or a '-e .' loop improperly
)
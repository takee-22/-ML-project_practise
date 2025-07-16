from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path :str)->List[str]:
    '''
    this fuch will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


from setuptools import setup, find_packages

setup(
    name="MLProject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List any dependencies here, or leave empty if not needed
    ],
)

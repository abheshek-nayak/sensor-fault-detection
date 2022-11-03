from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list


setup(
    name="sensor", # give a name to this package
    version="0.0.1", # give a version
    author="ineuron", # give the name of the autor
    author_email="avnish@ineuron.ai", # author email
    packages = find_packages(),#this will search for packages in your project folder
    install_requires= get_requirements() #Provide the list of external libraries required for the project ,e,g ["pymongo==4.2.0"],
)


# this file is able to build  and distribute end to end applications as a package

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirementst
    
    '''
    with open(file_path) as file_obj:
        requirements=[]
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith('#') and line !='-e .':
                requirements.append(line)
        return requirements



setup(
name = 'mlproject',
version='0.0.1',
author = 'Milan',
author_email = 'dangi.milan46@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt'),
description='ML project'
)
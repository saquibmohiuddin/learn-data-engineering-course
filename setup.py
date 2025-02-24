from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'


def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        requirements = [requirement for requirement in requirements if not requirement.startswith('#')]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name='learn_data_engineering',
    version='0.1',
    author='Saquib Siddiqui',
    author_email='ssiddiqui@educationcubed.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
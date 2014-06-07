from setuptools import find_packages, setup

setup(
    # Metadata
    name="mdma",
    version="0.1.4",
    description="ipython notebook markdown magic",
    url="",
    author="Erik Gafni",
    author_email="egafni@gmail.com",
    maintainer="Erik Gafni",
    maintainer_email="egafni@gmail.com",
    license="GPLv2",
    install_requires=["markdown", "docutils", "pygments"],
    # Packaging Instructions
    packages=find_packages(),
    include_package_data=True
)

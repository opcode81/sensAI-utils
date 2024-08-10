import functools
import re
from typing import Iterable, Dict
from glob import glob

from setuptools import setup, find_namespace_packages

# list of dependencies where ==/~= dependencies (used in requirements.txt) are relaxed:
# any later version is OK (as long as we are not aware of a concrete limitation - and once we are, we shall define
# the respective upper bound below)
DEPS_VERSION_LOWER_BOUND = [
    "typing-extensions",
]
# upper bound: map dependency name to lowest exluded version
DEPS_VERSION_UPPER_BOUND_EXCLUSIVE: Dict[str, str] = {}


def relaxed_requirements(deps: Iterable[str]):
    """
    :param deps: the set of requirements
    :return: the set of updated requirements with the relaxations defined above applied
    """
    updated_deps = []
    for dep in deps:
        dep = dep.strip()
        if dep.startswith("#"):
            continue
        m = re.match(r'([\w-]+)[=~]=', dep)  # match package with == or ~= version spec
        if m:
            package = m.group(1)
            if package in DEPS_VERSION_LOWER_BOUND:
                dep = dep.replace("==", ">=").replace("~=", ">=")
            elif package in DEPS_VERSION_UPPER_BOUND_EXCLUSIVE:
                dep = dep.replace("==", ">=").replace("~=", ">=")
                dep += ",<" + DEPS_VERSION_UPPER_BOUND_EXCLUSIVE[package]
        updated_deps.append(dep)
    return updated_deps


def relaxed_requirements_from_file(path):
    with open(path, "r") as f:
        return relaxed_requirements(f.readlines())


setup(
    name='sensai-utils',
    package_dir={"": "src"},
    license="MIT",
    url="https://github.com/opcode81/sensAI-utils",
    packages=find_namespace_packages(where="src"),
    include_package_data=True,
    version='1.2.1',
    description='Utilities from sensAI, the Python library for sensible AI',
    install_requires=relaxed_requirements_from_file("requirements.txt"),
    dependency_links=[],
    setup_requires=["wheel"],
    author='appliedAI Institute gGmbh & jambit GmbH',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License"
    ]
)

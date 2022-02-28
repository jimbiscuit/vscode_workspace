# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name="vscode-workspace",
    version="0.0.1",
    author="Jimbiscuit",
    author_email="julienchandelle@gmail.com",
    description="Generate vscode workspace file",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "vsc-init=vscode_workspace.script:main"
        ]
    }
)

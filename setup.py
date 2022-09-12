#!/usr/bin/env python

from distutils.core import setup

setup(
    name="exussum-pre-commit-jira-log",
    scripts=[
        "scripts/populate_message",
        "scripts/enforce_prefix_github",
        "scripts/verify_message",
    ],
    version="1.0.0",
    description="Pre-commit jira utilities",
    author="spencer portée",
    install_requires=["PyGithub==1.55", "docopt>=0.4.0,<0.5.0", "gitpython==3.1.27"],
)

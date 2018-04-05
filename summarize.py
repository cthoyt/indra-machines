#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script summarizes all of the INDRA machines in the current directory"""

import logging
import os

import click

from indra.tools.machine.machine import summarize_helper

log = logging.getLogger('indra-machines')
log.setLevel(logging.INFO)

HERE = os.path.dirname(os.path.realpath(__file__))


@click.command()
def main():
    """Summarizes the INDRA machines in all relevant subdirectories"""
    log.info('beginning INDRA machine summarizer')

    for subdirectory in sorted(os.listdir(HERE)):
        summarize_helper(os.path.join(HERE, subdirectory))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

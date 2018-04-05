#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script summarizes all of the INDRA machines in the current directory"""

import logging
import os

import click

from indra.tools.machine.machine import summarize_helper

logging.getLogger('rasmachine').setLevel(logging.WARNING)
log = logging.getLogger('indra-machines')
log.setLevel(logging.INFO)

HERE = os.path.dirname(os.path.realpath(__file__))


def directory_is_indra_machine(subdirectory):
    return (
            os.path.exists(os.path.join(subdirectory, 'config.yaml')) and
            os.path.exists(os.path.join(subdirectory, 'model.pkl'))
    )


@click.command()
def main():
    """Summarizes the INDRA machines in all relevant subdirectories"""
    log.info('beginning INDRA machine summarizer')

    for subdirectory in sorted(os.listdir(HERE)):
        click.echo('Summarizing {}'.format(subdirectory))
        if not directory_is_indra_machine(subdirectory):
            continue

        summarize_helper(os.path.join(HERE, subdirectory))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

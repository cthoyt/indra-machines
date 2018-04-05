#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script runs all of the INDRA machines in the current directory"""

import logging
import os

import click

from indra.tools.machine.machine import assemble_cx, get_config, get_ndex_cred, load_model

log = logging.getLogger('indra-machines')
log.setLevel(logging.INFO)

HERE = os.path.dirname(os.path.realpath(__file__))


def export(directory):
    """

    :param str directory:
    """
    if not os.path.isdir(directory):
        return

    if not os.path.exists(os.path.join(directory, 'config.yaml')):
        return  # Skip non-INDRA machine directories

    default_config_fname = os.path.join(directory, 'config.yaml')
    config = get_config(default_config_fname)

    ndex_cred = get_ndex_cred(config)
    if not ndex_cred:
        return

    name = ndex_cred.get('name')
    if not name:
        return

    model = load_model(directory)
    stmts = model.get_statements()
    cx_str = assemble_cx(stmts, name)

    with open(os.path.join(directory, '{}.cx'.format(name)), 'w') as f:
        click.echo(cx_str, f)


@click.command()
def main():
    """Runs the INDRA machine on all relevant subdirectories"""

    for subdirectory in sorted(os.listdir(HERE)):
        export(os.path.join(HERE, subdirectory))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

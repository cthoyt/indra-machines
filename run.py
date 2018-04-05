#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script runs all of the INDRA machines in the current directory"""

import logging
import os

import pybel
from indra.tools.machine.machine import assemble_cx, get_config, get_ndex_cred, load_model, run_with_search_helper

log = logging.getLogger('indra-machines')
log.setLevel(logging.INFO)

HERE = os.path.dirname(os.path.realpath(__file__))


def run_one(directory):
    """

    :param str directory:
    """
    if not os.path.isdir(directory):
        return

    if not os.path.exists(os.path.join(directory, 'config.yaml')):
        return  # Skip non-INDRA machine directories

    log.info('running in %s', directory)
    # Use config=None so it looks in the subdirectory
    run_with_search_helper(directory, config=None)

    default_config_fname = os.path.join(directory, 'config.yaml')
    config = get_config(default_config_fname)
    ndex_cred = get_ndex_cred(config)
    name = ndex_cred.get('name') if ndex_cred is not None else None

    model = load_model(directory)
    stmts = model.get_statements()

    if not stmts:
        log.warning('no statements')
        return

    # Output CX
    if name:
        cx_str = assemble_cx(stmts, name)
        with open(os.path.join(directory, 'output.cx'), 'w') as file:
            print(cx_str, file=file)

    # Output BEL gpickle
    bel_graph = pybel.from_indra_statements(stmts)
    pybel.to_pickle(bel_graph, os.path.join(directory, 'output.gpickle'))

    return True


def main():
    """Runs the INDRA machine on all relevant subdirectories"""
    log.info('beginning INDRA machine runner')

    for subdirectory in sorted(os.listdir(HERE)):
        run_one(os.path.join(HERE, subdirectory))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script runs all of the INDRA machines in the current directory"""

import logging
import os

import pybel
from indra.tools.machine.machine import assemble_cx, get_config, get_ndex_cred, load_model, run_with_search_helper

log = logging.getLogger('indra-machines')
log.setLevel(logging.INFO)

directory = os.path.dirname(os.path.realpath(__file__))


def main():
    """Runs the INDRA machine on all relevant subdirectories"""
    log.info('beginning INDRA machine runner')

    for subdirectory in sorted(os.listdir(directory)):
        absolute_subdirectory = os.path.join(directory, subdirectory)

        if not os.path.isdir(absolute_subdirectory):
            continue

        if not os.path.exists(os.path.join(absolute_subdirectory, 'config.yaml')):
            continue  # Skip non-INDRA machine directories

        log.info('running in %s', absolute_subdirectory)
        # Use config=None so it looks in the subdirectory
        run_with_search_helper(absolute_subdirectory, config=None)

        default_config_fname = os.path.join(absolute_subdirectory, 'config.yaml')
        config = get_config(default_config_fname)
        ndex_cred = get_ndex_cred(config)
        name = ndex_cred.get('name') if ndex_cred is not None else None

        model = load_model(absolute_subdirectory)
        stmts = model.get_statements()

        # Output CX
        if name:
            cx_str = assemble_cx(stmts, name)
            with open(os.path.join(absolute_subdirectory, 'output.cx'), 'w') as file:
                print(cx_str, file=file)

        # Output BEL gpickle
        bel_graph = pybel.from_indra_statements(stmts)
        pybel.to_pickle(bel_graph, os.path.join(absolute_subdirectory, 'output.gpickle'))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    main()

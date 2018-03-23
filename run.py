#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script runs all of the INDRA machines in the current directory"""

import logging
import os

from indra.tools.machine.machine import run_with_search_helper

log = logging.getLogger('indra-machines')
log.setLevel(logging.INFO)
directory = os.path.dirname(os.path.realpath(__file__))


def main():
    """Runs the INDRA machine on all relevant subdirectories"""
    log.info('beginning INDRA machine runner')
    
    for subdirectory in os.listdir(directory):
        absolute_subdirectory = os.path.join(directory, subdirectory)
        
        if not os.path.isdir(absolute_subdirectory):
            continue
        
        if not os.path.exists(os.path.join(absolute_subdirectory, 'config.yaml')):
            continue  # Skip non-INDRA machine directories
        
        log.info('running in %s', absolute_subdirectory)
        # Use config=None so it looks in the subdirectory
        run_with_search_helper(absolute_subdirectory, config=None)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    main()

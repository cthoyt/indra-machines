#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import os

import click
from ndex2.client import Ndex2 as Ndex
from requests.compat import urlsplit

from indra.tools.machine.machine import assemble_cx, get_config, get_ndex_cred, load_model

log = logging.getLogger(__name__)

#: The name of the environment variable to search or the NDEx username
NDEX_USERNAME = 'NDEX_USERNAME'

#: The name of the environment variable to search or the NDEx password
NDEX_PASSWORD = 'NDEX_PASSWORD'


def build_ndex_client(username=None, password=None, debug=False):
    """Builds a NDEx client by checking environmental variables.

    It has been requested that the :code:`ndex-client` has this functionality built-in by this GitHub
    `issue <https://github.com/ndexbio/ndex-python/issues/9>`_

    :param str username: NDEx username
    :param str password: NDEx password
    :param bool debug: If true, turn on NDEx client debugging
    :return: An NDEx client
    :rtype: Ndex
    """
    if username is None and NDEX_USERNAME in os.environ:
        username = os.environ[NDEX_USERNAME]
        log.info('got NDEx username from environment: %s', username)

    if password is None and NDEX_PASSWORD in os.environ:
        password = os.environ[NDEX_PASSWORD]
        log.info('got NDEx password from environment')

    return Ndex(username=username, password=password, debug=debug)


def cx_to_ndex(cx, username=None, password=None, debug=False):
    """Uploads a CX document to NDEx. Not necessarily specific to PyBEL.

    :param list cx: A CX JSON dictionary
    :param str username: NDEx username
    :param str password: NDEx password
    :param bool debug: If true, turn on NDEx client debugging
    :return: The UUID assigned to the network by NDEx
    :rtype: str
    """
    ndex = build_ndex_client(username=username, password=password, debug=debug)
    res = ndex.save_new_network(cx)

    url_parts = urlsplit(res).path
    network_id = url_parts.split('/')[-1]

    return network_id


@click.command()
@click.option('-d', '--directory', default=os.getcwd(), help='Directory to upload. Defaults to CWD')
def main(directory):
    """Upload the given directory to NDEx"""

    default_config_fname = os.path.join(directory, 'config.yaml')
    config = get_config(default_config_fname)
    ndex_cred = get_ndex_cred(config)
    name = ndex_cred.get('name') if ndex_cred is not None else None

    model = load_model(directory)
    stmts = model.get_statements()

    if not stmts:
        log.warning('no statements')
        return

    cx_str = assemble_cx(stmts, name)

    cx = json.loads(cx_str)

    cx_to_ndex(cx)


if __name__ == '__main__':
    main()

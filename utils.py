#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
import re
import logging
import pprint

logger = logging.getLogger(__name__)


def get_pretty_print(item, depth=None):
    pp = pprint.PrettyPrinter(indent=4, depth=depth)
    return pp.pformat(item)


PP = lambda x: get_pretty_print(x)

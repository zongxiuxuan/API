#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from core.utils import log

log.Logging()


def pytest_runtest_call(__multicall__):
	try:
		__multicall__.execute()
	except KeyboardInterrupt:
		raise
	except:
		logging.exception('pytest_runtest_call caught exception:')
		raise

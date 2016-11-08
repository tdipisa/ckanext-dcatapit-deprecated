import logging

from ckan.plugins.toolkit import Invalid
from datetime import datetime

log = logging.getLogger(__file__)


def isBlank (string):
    return not (string and string.strip())

def range_validator(value, context):
	if not isBlank(value):
		ranges = value.split(',')

		for r in ranges:
			if not r:
				raise Invalid('Invalid range, one value is missing')

	return value
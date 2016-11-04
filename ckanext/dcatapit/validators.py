import logging

from ckan.plugins.toolkit import Invalid
from datetime import datetime

log = logging.getLogger(__file__)

def range_validator(value, context):
	log.info("::::::::::::::::::::::::::::::::::: %r", value)
	if value:
		ranges = value.split(',')

		for r in ranges:
			if not r:
				raise Invalid('Invalid range, one or more value is missing')

	return value
import logging

from ckan.plugins.toolkit import Invalid

log = logging.getLogger(__file__)

def method(value, schema, context):
    return value
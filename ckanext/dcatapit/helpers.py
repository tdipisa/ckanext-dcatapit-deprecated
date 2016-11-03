import logging
import ckanext.dcatapit.schema as dcatapit_schema

log = logging.getLogger(__file__)


def get_dcatapit_schema():
    log.info('Retrieving DCAT-AP_IT schema fields...')
    return dcatapit_schema.get_json_schema()
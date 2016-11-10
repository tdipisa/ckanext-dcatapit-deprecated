import logging
import ckanext.dcatapit.schema as dcatapit_schema

log = logging.getLogger(__file__)


def get_dcatapit_package_schema():
    log.debug('Retrieving DCAT-AP_IT package schema fields...')
    return dcatapit_schema.get_custom_package_schema()

def get_dcatapit_organization_schema():
    log.debug('Retrieving DCAT-AP_IT organization schema fields...')
    return dcatapit_schema.get_custom_organization_schema()

def get_dict_field_index(list, key):
    log.debug('Retrieving dict fields index...')
    for element in list:
    	if element.get(key):
    		return True

    return False
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckan.plugins as plugins

import ckanext.dcatapit.validators as validators
import ckanext.dcatapit.schema as dcatapit_schema
import ckanext.dcatapit.helpers as helpers

import logging

log = logging.getLogger(__file__)


class DcatapitPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):

	# IDatasetForm
    plugins.implements(plugins.IDatasetForm)
	# IConfigurer
    plugins.implements(plugins.IConfigurer)
    # IValidators
    plugins.implements(plugins.IValidators)
    # ITemplateHelpers
    plugins.implements(plugins.ITemplateHelpers)
    
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'ckanext-dcatapit')
		
    def _modify_package_schema(self, schema):
        for field in dcatapit_schema.get_json_schema():

        	validators = []
        	for validator in field['validator']:
        		validators.append(toolkit.get_validator(validator))

        	schema.update({
                field['name']: validators + [
                    toolkit.get_converter('convert_to_extras')
                ]
            })

    	'''schema.update({
            'tag_string': [
            	toolkit.get_validator('not_empty'),
            	toolkit.get_validator('tag_string_convert')
            ]
        })

        log.info(":::::::::::::::::::::::::::::: %r", schema)'''

        return schema

    def create_package_schema(self):
        schema = super(DcatapitPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(DcatapitPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(DcatapitPlugin, self).show_package_schema()
        
        for field in dcatapit_schema.get_json_schema():

            validators = []
            for validator in field['validator']:
                validators.append(toolkit.get_validator(validator))

            schema.update({
                field['name']: [
                    toolkit.get_converter('convert_from_extras')
                ] + validators
            })

        '''schema.update({
            'tag_string': [
                toolkit.get_validator('not_empty'),
                toolkit.get_validator('tag_string_convert')
            ]
        })

        log.info(":::::::::::::::::::::::::::::: %r", schema)'''

        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True
		
    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def get_validators(self):
		return {
            'range_validator': validators.range_validator
        }

    def get_helpers(self):
        return {
            'get_dcatapit_schema': helpers.get_dcatapit_schema
        }
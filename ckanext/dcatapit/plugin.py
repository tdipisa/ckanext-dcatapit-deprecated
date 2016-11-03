import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckan.plugins as plugins

import ckanext.dcatapit.validators as validators
import ckanext.dcatapit.schema as dcatapit_schema
import ckanext.dcatapit.helpers as helpers

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
		
    def _modify_package_schema_for_edit(self, schema):
        for field in dcatapit_schema.get_json_schema():

        	validators = []
        	for validator in field['validator']:
        		validators.append(toolkit.get_validator(validator))

        	schema.update({
                field['name']: validators + [
                    toolkit.get_converter('convert_to_extras')
                ]
            })

        return schema

    def _modify_package_schema_for_read(self, schema):
        for field in dcatapit_schema.get_json_schema():

        	validators = []
        	for validator in field['validator']:
        		validators.append(toolkit.get_validator(validator))

        	schema.update({
                field['name']: [
                    toolkit.get_converter('convert_from_extras')
                ] + validators
            })

        return schema

    def create_package_schema(self):
        schema = super(DcatapitPlugin, self).create_package_schema()
        schema = self._modify_package_schema_for_edit(schema)
        return schema

    def update_package_schema(self):
        schema = super(DcatapitPlugin, self).update_package_schema()
        schema = self._modify_package_schema_for_edit(schema)
        return schema

    def show_package_schema(self):
        schema = super(DcatapitPlugin, self).show_package_schema()
        schema = self._modify_package_schema_for_read(schema)
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
            'method': validators.method
        }

    def get_helpers(self):
        return {
            'get_dcatapit_schema': helpers.get_dcatapit_schema
        }
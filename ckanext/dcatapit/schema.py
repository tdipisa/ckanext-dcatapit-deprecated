

def get_json_schema():
	return [
	    {
		    'name': 'dataset_identifier',
		    'validator': ['not_empty'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Dataset Identifier',
		    'placeholder': 'dataset identifier',
		    'is_required': True
	    },
	    {
		    'name': 'other_identifier',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Other Identifier',
		    'placeholder': 'other identifier',
		    'is_required': False
	    },
	    {
		    'name': 'publisher_uri',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Dataset Editor',
		    'placeholder': 'dataset editor',
		    'is_required': False
	    },
	    {
		    'name': 'issued',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'data',
		    'label': 'Release Date',
		    'placeholder': 'release date',
		    'is_required': False
	    }
	]
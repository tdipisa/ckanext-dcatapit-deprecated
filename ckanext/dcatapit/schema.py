

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
		    'name': 'theme',
		    'validator': ['not_empty'],
		    'element': 'select',
		    'type': 'list',
		    'label': 'Dataset Themes',
		    'placeholder': 'eg. economy, mental health, government',
		    'data_module_source': '/api/2/util/tag/autocomplete?incomplete=?',
		    'is_required': True
	    },
	    {
		    'name': 'sub_theme',
		    'validator': ['ignore_missing'],
		    'element': 'select',
		    'type': 'list',
		    'label': 'Sub Theme',
		    'placeholder': 'sub theme of the dataset',
		    'data_module_source': '/api/2/util/tag/autocomplete?incomplete=?',
		    'is_required': True
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
		    'type': 'date',
		    'label': 'Release Date',
		    'placeholder': 'release date',
		    'is_required': False
	    },
	    {
		    'name': 'modified',
		    'validator': ['not_empty'],
		    'element': 'input',
		    'type': 'date',
		    'label': 'Modification Date',
		    'placeholder': 'modification date',
		    'is_required': True
	    },
	    {
		    'name': 'geographical_coverage',
		    'validator': ['not_empty'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Geographical Coverage',
		    'placeholder': 'geographical coverage',
		    'is_required': True
	    },
	    {
		    'name': 'language',
		    'validator': ['not_empty'],
		    'element': 'select',
		    'type': 'list',
		    'label': 'Dataset Languages',
		    'placeholder': 'eg. italian, german, english',
		    'data_module_source': '/api/2/util/tag/autocomplete?incomplete=?',
		    'is_required': True
	    },
	    {
		    'name': 'temporal_coverage',
		    'validator': ['ignore_missing', 'range_validator'],
		    'element': 'range',
		    'type': 'date',
		    'label': 'Temporal Coverage',
		    'placeholder': 'temporal coverage',
		    'is_required': False,
		    'renges': [
		    	{
		    		'name': 'start_date',
		    		'label': 'Start Date'
		    	},
			    {
		    		'name': 'end_date',
		    		'label': 'End Date'
		    	}
		    ]
	    },
	    {
		    'name': 'accrual_periodicity',
		    'validator': ['not_empty'],
		    'element': 'select',
		    'type': 'list',
		    'label': 'Frequency',
		    'placeholder': 'accrual periodicity',
		    'data_module_source': '/api/2/util/tag/autocomplete?incomplete=?',
		    'is_required': True
	    },
	    {
		    'name': 'is_version_of',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Version Of',
		    'placeholder': 'is version of',
		    'is_required': False
	    },
	    {
		    'name': 'conforms_to',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Conforms To',
		    'placeholder': 'conforms to',
		    'is_required': False
	    },
	    {
		    'name': 'contact_point',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Point of Contact',
		    'placeholder': 'point of contact',
		    'is_required': False
	    },
	    {
		    'name': 'rights_holder',
		    'validator': ['not_empty'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Rights Holder',
		    'placeholder': 'rights holder of the dataset',
		    'is_required': True
	    },
	    {
		    'name': 'creator',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Creator',
		    'placeholder': 'creator of the dataset',
		    'is_required': False
	    }
	]
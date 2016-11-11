
def get_custom_organization_schema():
	return [
	    {
		    'name': 'email',
		    'validator': ['not_empty'],
		    'element': 'input',
		    'type': 'email',
		    'label': 'EMail',
		    'placeholder': 'organization email',
		    'is_required': True
	    },
	    {
		    'name': 'telephone',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'text',
		    'label': 'Telephone',
		    'placeholder': 'organization telephone',
		    'is_required': False
	    },
	    {
		    'name': 'site',
		    'validator': ['ignore_missing'],
		    'element': 'input',
		    'type': 'url',
		    'label': 'Site URL',
		    'placeholder': 'organization site url',
		    'is_required': False
	    }
	]

def get_custom_package_schema():
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
		    'is_required': False
	    },
	    {
		    'name': 'publisher',
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
		    'validator': ['ignore_missing'],
		    'element': 'select',
		    'type': 'list',
		    'label': 'Geographical Coverage',
		    'placeholder': 'geographical coverage',
		    'data_module_source': '/api/2/util/tag/autocomplete?incomplete=?',
		    'is_required': False
	    },
	    {
		    'name': 'language',
		    'validator': ['ignore_missing'],
		    'element': 'select',
		    'type': 'list',
		    'label': 'Dataset Languages',
		    'placeholder': 'eg. italian, german, english',
		    'data_module_source': '/api/2/util/tag/autocomplete?incomplete=?',
		    'is_required': True
	    },
	    {
		    'name': 'temporal_coverage',
		    'validator': ['ignore_missing', 'couple_validator'],
		    'element': 'couple',
		    'type': 'date',
		    'label': 'Temporal Coverage',
		    'placeholder': 'temporal coverage',
		    'is_required': False,
		    'couples': [
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
		    'name': 'rights_holder',
		    'validator': ['not_empty', 'couple_validator'],
		    'element': 'couple',
		    'type': 'text',
		    'label': 'Rights Holder',
		    'placeholder': 'rights holder of the dataset',
		    'is_required': True,
		    'couples': [
		    	{
		    		'name': 'holder_name',
		    		'label': 'Name'
		    	},
			    {
		    		'name': 'holder_code_identified',
		    		'label': 'IPA/IVA'
		    	}
		    ]
	    },
	    {
		    'name': 'creator',
		    'validator': ['ignore_missing', 'couple_validator'],
		    'element': 'couple',
		    'type': 'text',
		    'label': 'Creator',
		    'placeholder': 'creator of the dataset',
		    'is_required': False,
		    'couples': [
		    	{
		    		'name': 'creator_name',
		    		'label': 'Name'
		    	},
			    {
		    		'name': 'creator_code_identified',
		    		'label': 'IPA/IVA'
		    	}
		    ]
	    }
	]
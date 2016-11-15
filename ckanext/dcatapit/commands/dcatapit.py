
import logging
import urllib2

import xml.etree.ElementTree as etree
import ckan.plugins.toolkit as toolkit
import ckanext.dcatapit.interfaces as interfaces

from ckan.lib.cli import CkanCommand

class DCATAPITCommands(CkanCommand):
    '''
    '''

    summary = __doc__.split('\n')[0]
    usage = __doc__

    _ckan_locales_mapping = {
        'it': 'it',
        'de': 'de',
        'en': 'en_GB'
    }

    def __init__(self, name):
        self.parser.add_option('--filename', dest='filename', default=None,
                               help='Path to a file')
        self.parser.add_option('--url', dest='url', default=None,
                               help='URL to a resource')
        self.parser.add_option('--name', dest='name', default=None,
                               help='Name of the vocabulary to work with')

        super(DCATAPITCommands, self).__init__(name)

    def command(self):
        '''
        Parse command line arguments and call appropriate method.
        '''
        cmd = self.args[0]
        self._load_config()

        if cmd == 'load':
            self.load()
        else:
            print self.usage
            logging.error('Command "%s" not recognized' % (cmd,))
            return

    def load(self):
    	##
        # Checking command given options
        ##
        url = self.options.url
        filename = self.options.filename

        if not url and not filename:
            print "No URL or FILENAME provided and one is required"
            print self.usage
            return

        vocab_name = self.options.name

        if not vocab_name:
            print "No vocabulary name provided and is required"
            print self.usage
            return

        ##
        # Loading the RDF vocabulary
        ##
        print "Loading graph ..."

        RDF_URI = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
        XML_URI = 'http://www.w3.org/XML/1998/namespace'

        ABOUT_ATTRIB = '{' + RDF_URI + '}about'
        LANG_ATTRIB = '{' + XML_URI + '}lang'

        ns = {
            'rdf': RDF_URI,
            'foaf': 'http://xmlns.com/foaf/0.1/',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'dcterms': 'http://purl.org/dc/terms/',
            'skos': 'http://www.w3.org/2004/02/skos/core#'
        }

        try:
        	graph = urllib2.urlopen(url)
        except Exception,e:
            logging.error("Error retrieving the document %r", e)
            print self.usage
            return

        document = etree.parse(graph)
        root = document.getroot()

        concepts = []
        pref_labels = []

        for concept in root.findall('skos:Concept', ns):
            about = concept.attrib.get(ABOUT_ATTRIB)
            identifier = concept.find('dc:identifier', ns).text

            print 'Concept {} ({})'.format(about, identifier)
            concepts.append(identifier)

            for pref_label in concept.findall('skos:prefLabel', ns):
                lang = pref_label.attrib.get(LANG_ATTRIB)
                label = pref_label.text

                print u'    Label {}: {}'.format(lang, label)
                pref_labels.append({
                	'name': identifier,
                	'lang': lang,
                	'localized_text': label
               	})

        ##
        # Creating the Tag Vocabulary using the given name
        ##
        logging.info('Creating tag vocabulary %r ...', vocab_name)

        user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
        context = {'user': user['name']}

        try:
        	data = {'id': vocab_name}
        	toolkit.get_action('vocabulary_show')(context, data)

        	logging.info("Vocabulary %s already exists, skipping...", vocab_name)
        except toolkit.ObjectNotFound:
	        logging.info("Creating vocabulary '%s'", vocab_name)

	        data = {'name': vocab_name}
	        vocab = toolkit.get_action('vocabulary_create')(context, data)

	        for tag in concepts:
	            logging.info("Adding tag {0} to vocabulary '{1}'".format(tag, vocab_name))

	            data = {'name': tag, 'vocabulary_id': vocab['id']}
	            toolkit.get_action('tag_create')(context, data)

        ##
        # Persisting Multilag Tags or updating existing
        ##
        logging.info('Creating the corresponding multilang tags for vocab: %r ...', vocab_name)

        for pref_label in pref_labels:
        	if pref_label['lang'] in self._ckan_locales_mapping:
		        tag_name = pref_label['name']
		        tag_lang = self._ckan_locales_mapping[pref_label['lang']]
		        tag_localized_name = pref_label['localized_text']

	        	interfaces.persist_tag_multilang(tag_name, tag_lang, tag_localized_name, vocab_name)

    	print 'Vocabulary successfully loaded ({})'.format(vocab_name)


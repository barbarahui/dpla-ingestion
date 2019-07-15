from dplaingestion.mappers.marc_mapper import PyMARCMapper
from akara import logger

class SierraMARCMapper(PyMARCMapper):
    def __init__(self, provider_data):
        super(SierraMARCMapper, self).__init__(provider_data)
        self.mapping_dict.update({
            lambda t: t == "001": [(self.map_is_shown_at, None)]
        })

    def map_is_shown_at(self, _dict, tag, codes):
        prop = "isShownAt"
        if tag == '001':
            id = self._get_values(_dict, codes)[0]
            self.mapped_data[prop] = ''.join(
                ('https://sierramadre.biblionix.com/catalog/biblio/', id))

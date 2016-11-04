from dplaingestion.mappers.marc_mapper import PyMARCMapper
from akara import logger

class CSLMARCMapper(PyMARCMapper):
    def __init__(self, provider_data):
        super(CSLMARCMapper, self).__init__(provider_data)
        self.mapping_dict.update({
            lambda t: t == "001": [(self.map_is_shown_at, None)]
        })

    def map_is_shown_at(self, _dict, tag, codes):
        prop = "isShownAt"
        if tag == '001':
            id = self._get_values(_dict, codes)[0]
            self.mapped_data[prop] = ''.join(
                ('http://catalog.library.ca.gov/F/?func=find-b&request=', id,
                 '&find_code=SYS'))

    def map_is_shown_by(self, _dict, tag, codes):
        prop = "isShownBy"
        if prop not in self.mapped_data:
            urlString = self._get_values(_dict, 'b')[0]
            imgString = self._get_values(_dict, 't')[0]
            self.mapped_data[prop] = ''.join(
                ('http://catalog.library.ca.gov', urlString, '/', imgString))
class CodebookEntry:
    NUM_PROPERTIES = 3
    _name: str
    _description: str
    _source: str

    def __init__(self, name: str, description: str, source: str):
        self._name = name
        self._description = description
        self._source = source

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_source(self) -> str:
        return self._source

    def __str__(self):
        return self._name

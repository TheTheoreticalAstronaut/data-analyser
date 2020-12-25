from enum import Enum, auto
from typing import List
from src.codebook_entry import CodebookEntry
import csv

CodebookEntryList = List[CodebookEntry]


class CodebookParser:
    CODEBOOK_FILENAME = "co2-data/owid-co2-codebook.csv"
    _headers: List[str]
    _codebook: CodebookEntryList

    class FileType(Enum):
        CSV = auto()

    def __init__(self, file_type: FileType):
        self._headers = []
        self._codebook = []

        if file_type == self.FileType.CSV:
            self._read_csv_file()
        else:
            print("Unsupported file type")

    def get_codebook(self) -> CodebookEntryList:
        return self._codebook

    def _read_csv_file(self) -> None:
        with open(self.CODEBOOK_FILENAME, "r") as file:
            reader = csv.reader(file)

            self._headers = next(reader)
            if len(self._headers) != CodebookEntry.NUM_PROPERTIES:
                print("Unexpected number of headers: expected {0}, got {1}".format(CodebookEntry.NUM_PROPERTIES, len(self._headers)))
                return

            for line in reader:
                if len(line) != CodebookEntry.NUM_PROPERTIES:
                    print("Unexpected number of properties: expected {0}, got {1} ({2})".format(CodebookEntry.NUM_PROPERTIES, len(line), line))
                    print("Skipping entry")
                    continue
                self._codebook.append(CodebookEntry(line[0], line[1], line[2]))






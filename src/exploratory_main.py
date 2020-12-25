from src.codebook_parser import CodebookParser

if __name__ == '__main__':
    codebook_parser = CodebookParser(CodebookParser.FileType.CSV)
    for entry in codebook_parser.get_codebook():
        print("{0}: {1}".format(entry, entry.get_description()))

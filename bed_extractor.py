import pkg_resources
import argparse
import sys


def get_names(symbols_to_query):
    hgnc_name = pkg_resources.resource_filename('bed_extractor', 'resources/hgnc_complete_set.txt')
    symbols_to_query_expanded = set([])
    for line in open(hgnc_name):
        line = line.strip().split("\t")
        symbol = {line[1]}
        aliases = line[10].replace('"', "").split("|")
        if aliases == ['']:
            aliases = None
        else:
            symbol.update(aliases)

        if len(symbols_to_query.intersection(symbol)) > 0:
            symbols_to_query_expanded.update(symbol)

    if len(symbols_to_query.difference(symbols_to_query_expanded)) > 0:
        raise ValueError("could not find the following symbols [{0}]".format(
            symbols_to_query.difference(symbols_to_query_expanded)))
    return symbols_to_query_expanded


def get_query_symbols(csv_line):
    _s = set([])
    for i in csv_line.split(","):
        _s.add(i.strip())
    return _s


def main():
    parser = argparse.ArgumentParser(prog="returns bed lines with any matching genes symbols of alaises",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-i", "--input_bed_file", help="the input bed file", type=argparse.FileType("r"), required=True)
    parser.add_argument("-s", "--gene_symbol_list", help="comma separated list of gene_symbols", type=str,
                        required=True)

    args = parser.parse_args()
    bed_file = args.input_bed_file
    gene_symbol_list = args.gene_symbol_list

    symbols_to_query = get_query_symbols(gene_symbol_list)

    symbols_to_query_with_alaises = get_names(symbols_to_query)

    for line in bed_file:
        if any(symbol in line for symbol in symbols_to_query_with_alaises):
            sys.stdout.write(line)

if __name__ == "__main__":
    main()

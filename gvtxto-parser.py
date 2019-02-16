#!/usr/bin/python

import click
import re
import csv

# First regex try
# rex = re.compile('(?!(^[0-9]+:$))(?!^$)')
# IRC freenode #regex suggestions;
# regex101.com might be helpful
rexinfo = r"^(?:(?! *\d+:).*\n)*"
rexdata = r"(?<!\S)\d+(?!\S)"


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

# Fetching command line arguments, with click module
@click.command()
@click.option(
    '--version',
    '-v',
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Prints this script's version")
@click.option(
    '--input',
    '-i',
    prompt=True,
    help='Input file; absolute/relative path',
    type=click.File('r', encoding='latin-1'))
@click.option(          # ^^^^ Attention to input file characters set encoding
    '--output',
    '-o',
    prompt=True,
    help="Output file (you'll must add the file extenxion)",
    type=click.File('w', encoding='latin-1'))
@click.option(          # ^^^^ Attention to input file characters set encoding
    '--out-type',
    '-ot',
    type=click.Choice(['raw', 'enhanced', 'csv']),
    default='enhanced',
    help=('raw: only count per channel data \n'
          'enhanced: including GammaVision log info \n'
          'csv: comma-separated values'
          ),
)
# Core function. It is parsing the input file and writing an output new file
def parser(input, output, out_type):
    """
    This script allows you to convert GammaVision .txt output files into a
    much more treatable format, printing just one channel (and its respective
    count) per row, by-comma separated.

    You can see the available options using --help option.

        $ python gvtxto-parser.py [options] -i <inpfil.txt> -o <outfil.dat>

    Theoretically you are going to be able to choose the format what you
    want (.dat in this case).

    The core has been designed using regex, so it should keep working
    as long as GammaVision does preserve this kind of format for its output
    files.

    More info and practical examples about regex in www.regex101.com
    """
    # Important: all print() functions are intended to debug the code, so
    # they are disabled right now.
    # Loading raw-GammaVision data in an input string to parse with regex
    i_str = input.read()
    # print(i_str)
    # Parsingtreatable
    # First match created (when re.search() find rexinfo)
    info_matches = re.search(rexinfo, i_str)
    # Parsing info lines. In the case info_matches will be true, it will
    # take a decision accordign to user choice for --out-type parameter
    # Default: enhanced
    if info_matches:
        # print("{match}".format(match=info_matches.group()))
        # Storing file without GammaVision header in a new string
        # called noinf_str. re.sub() function is replacing nexinfo
        # match with blank spaces
        noinf_str = re.sub(rexinfo, ' ', i_str)
        # Second match created, using re.finditer() to iterate the
        # searching process. This iterative behavior is also useful
        # to print the channel number alongside his count, that's why
        # we have used below 'i' index and enumerate()
        data_matches = re.finditer(rexdata, noinf_str)
        if out_type == 'enhanced':
            # include metadata instead write in the file itself ?
            # writing enhanced GammaVision header
            output.write('{match}\n'.format(match=info_matches.group()))
            # writing columns headers
            output.write('channel,count\n')
            # writing relevant data
            for i, match in enumerate(data_matches, start=1):
                # print("{i} {match}".format(i=i, match=match.group()))
                output.write('{i},{match}\n'.format(i=i, match=match.group()))
        elif out_type == 'raw':
            for i, match in enumerate(data_matches, start=1):
                # print("{i} {match}".format(i=i, match=match.group()))
                output.write('{match}'.format(match=match.group()))
        elif out_type == 'csv':
            # writing columns headers. Using csv module
            col_nam = ['channel', 'count']
            writer = csv.DictWriter(output, fieldnames=col_nam)
            writer.writeheader()
            # writing relevant data
            for i, match in enumerate(data_matches, start=1):
                # print("{i} {match}".format(i=i, match=match.group()))
                output.write('{i},{match}\n'.format(i=i, match=match.group()))


if __name__ == '__main__':
    parser()

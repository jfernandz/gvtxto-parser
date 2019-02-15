#!/usr/bin/python

import click
import re
# first regex try
# rex = re.compile('(?!(^[0-9]+:$))(?!^$)')

# IRC #regex suggestion; regex101.com might be helpful
rexinfo = r"^(?:(?! *\d+:).*\n)*"
rexdata = r"(?<!\S)\d+(?!\S)"


# Fetching command line arguments, with click module
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('--version',
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
    type=click.File('r'),
    help='Input file; absolute/relative path')
@click.option(
    '--output',
    '-o',
    prompt=True,
    type=click.File('w'),
    help="Output file (you'll must add the file extenxion)")
@click.option(
    '--out-type',
    type=click.Choice(['raw', 'enhanced', 'treatable']),
    default='enhanced',
    help=('raw:\nonly count per channel data \n'
          'enhanced: including GammaVision log info \n'
          'tratable: csv by comma separated\nwith columns header'
          ),
)
# Core function. It is parsing the input file and writing an output new file
def parser(input, output, out_type, version):
    """
    This script allows you to convert GammaVision .txt output files into a
    much more treatable format, printing just one channel (and its respective
    count) per row, by-comma separated.

    It has no options for the momment (in addition to --help), maybe in a
    future. A practical usage would be:

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
    # Loading raw data in an input string to parse with regex
    i_str = input.read()
    # print(i_str)
    # Parsing
    # First match created (when re.search() found rexinfo)
    info_matches = re.search(rexinfo, i_str)
    # Parsing info lines. In the case info_matches will be true, it will
    # print the match in the first lines and then it will remove them from
    # the original string (i_str) with re.sub(). This will create
    # a new one string called (noinf_str)
    if info_matches:
        # print("{match}".format(match=info_matches.group()))
        # include metadata instead write in the file itself ?
        noinf_str = re.sub(rexinfo, ' ', i_str)
        # Second match created, using re.finditer() to iterate the
        # searching process. This iterative behavior is also useful
        # to print the channel number alongside his count, that's why
        # we have used 'i' index and enumerate()
        data_matches = re.finditer(rexdata, noinf_str)
        if out_type == 'enhanced':
            output.write('{match}\n'.format(match=info_matches.group()))
            output.write('channel,count\n')
            for i, match in enumerate(data_matches, start=1):
                # print("{i} {match}".format(i=i, match=match.group()))
                output.write('{i},{match}\n'.format(i=i, match=match.group()))
        elif out_type == 'treatable':
            output.write('channel,count\n')
            for i, match in enumerate(data_matches, start=1):
                # print("{i} {match}".format(i=i, match=match.group()))
                output.write('{i},{match}\n'.format(i=i, match=match.group()))
        elif out_type == 'raw':
            for i, match in enumerate(data_matches, start=1):
                # print("{i} {match}".format(i=i, match=match.group()))
                output.write('{match}\n'.format(match=match.group()))


if __name__ == '__main__':
    parser()

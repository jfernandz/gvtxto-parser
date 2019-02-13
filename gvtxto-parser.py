import click
import re


# first regex try
#rex = re.compile('(?!(^[0-9]+:$))(?!^$)')
# IRC #regex suggestion; regex101.com might be helpful
rexdata = r"(?<!\S)\d+(?!\S)"
rexinfo = r"^(?:(?! *\d+:).*\n)*"

@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))

def parser(input, output):
    i_str = input.read()
    #print(i_str)
    # Parsing
    # parse input file and writing an output file
    info_matches = re.search(rexinfo, i_str)
    if info_matches:
        #print("{match}".format(match=info_matches.group()))
        output.write('{match}\nchannel,count\n'.format(match=info_matches.group()))
        noinf_str = re.sub(rexinfo, ' ', i_str)
    data_matches = re.finditer(rexdata, noinf_str)
    for i, match in enumerate(data_matches, start=1):
        #print("{i} {match}".format(i=i, match=match.group()))
        output.write('{i},{match}\n'.format(i=i, match=match.group()))

if __name__ == '__main__':
    parser()

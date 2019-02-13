import click
import csv
import re


rex = re.compile('(?!(^[0-9]+:$))(?!^$)')

@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def parser(input, output):
    # Parsing
    # parse input file and writing an output file
    for _ in range(4):
        next(input)
    i = 1
    reader = csv.reader(input, delimiter=' ')
    for row in reader:
        for r in row:
            if rex.match(r):
                output.write('{},{} \n'.format(i, r))
                i = i + 1

if __name__ == '__main__':
    parser()

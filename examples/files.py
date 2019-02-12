import click
import csv


@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def parser(input, output):
    while True:
        # Parsing
        # parse input file and writing an output file
        with open('employee_birthday.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
            line_count = 0


if __name__ == '__main__':
    parser()

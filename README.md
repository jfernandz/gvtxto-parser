# [GammaVision](https://www.ortec-online.com/products/application-software/gammavision) output parser

This script parses output `.txt` files from GammaVision spectroscopy software, It does convert those files to a long format much more treatable from statistic point of view.

The more appropriate way to treat this output files should be using `R`, however this script does clean that info and rearrange the values in a long format. Then you are gonna be able to treat those values with any kind of statistical software.

## Usage
The general usage would be

```
$ ./gvtxto-parser.py [-i/--input <filename.txt>] [-o/--output <filename.DAT>]
                     [-ot/--out-type {enhanced|raw|csv}]
```

In the case you don't provide any option, you will be prompted about input and output files (tab-autocompletion has not been implemented, so **I recommend one-line mode to take advantage of shell native autocomplete**) and `--out-type` is set as `enhanced` by default.

  - `enhanced`

    It will parse also GammaVision `.txt` header. Which consist in info about date, time and a description previously provided by user in GammaVision.
  - `raw`

    It will parse the GammaVision output `.txt` to generate a file with raw channels data

  - `csv`

    This will produce a `.csv` file (comma separated values), this is the most appropriate format to treat with `R` or any spreadsheet. **You must use `.csv` extension to output file name in this case.**


## Dependencies
Further than `python`, you will need to install a few extra modules available in `pip`:

- `click` to handle/parse command line arguments.
- `regex` to parse data using regular expresions.

You can install this packages performing the following commands

##### Upgrade `pip`
```
$ sudo python -m pip install --upgrade pip
```
##### Install `click`
  - system-wide
  ```
  $ sudo python -m pip install click
  ```
  - user-side
  ```
  $ python -m pip install --user click
  ```
##### Install `regex`
  - system-wide
  ```
  $ sudo python -m pip install regex
  ```
  - user-side
  ```
  $ python -m pip install --user regex
  ```

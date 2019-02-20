# [GammaVision](https://www.ortec-online.com/products/application-software/gammavision) output parser

This script parses output `.txt` files from GammaVision spectroscopy software, It does convert those files to a long format much more treatable from statistic point of view.

The more appropriate way to treat this output files should be using `R`, however this script does clean that info and rearrange the values in a long format. Then you are gonna be able to treat those values with any kind of statistical software.


## Usage
A general usage would be

```
$ ./gvtxto-parser.py [-i/--input <filename.txt>] [-o/--output <filename.DAT>] [-ot/--out-type {enhanced|raw|csv}]
```

In the case you don't provide any option, you will be prompted about input and output files (tab-autocomplete has not been implemented in this prompting mode, so **I recommend in-line mode to take advantage of shell native autocomplete**) and `--out-type` is set as `enhanced` by default.

  - `enhanced`

    It will parse also GammaVision `.txt` header. Which consist in info about date, time and a description previously provided by user in GammaVision.
  - `raw`

    It will parse the GammaVision output `.txt` to generate a file with channels raw data

  - `csv`

    This will produce a `.csv` file (comma separated values), this is the most appropriate format to treat with `R` or any spreadsheet. **You must use `.csv` extension to output file name in this case.**


## Dependencies
Further than `python`, you will need to install a few extra modules available through `pip`:

- `click` to handle/parse command line arguments.
- `regex` to parse data using regular expresions.

You will be able to install these packages performing the following commands, depending on your OS.

### Windows

**Download** `python` **from their [official website](https://www.python.org/downloads/)**

Obviously on **Windows** you will not able to use sudo, but you can always **open a new terminal as admin** for a system-wide install. Then you will be able to perform the same commands than Linux, but obviously **omitting** `sudo`.

**However, you don't need to perform a system-wide install for `python`, since this script does not requires it, it is fully functional at user space. As much, you will be asked for some admin password to perform any software install, but this is normal, of course; it is related to any kind of software install process in the system.**

You also may want to [add `python` to your PATH environment variable,](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/) if you have not done during python install process.


### Linux

- ##### Upgrade `pip`
First update your `pip` module
```
$ sudo python -m pip install --upgrade pip
```

You will need to perform this operation as root.

- ##### Install `click`
  - system-wide / install as root
  ```
  $ sudo python -m pip install click
  ```
  - user-side
  ```
  $ python -m pip install --user click
  ```
- ##### Install `regex`
  - system-wide / install as root
  ```
  $ sudo python -m pip install regex
  ```
  - user-side
  ```
  $ python -m pip install --user regex
  ```

## License

This project is licensed under **GPLv3.** - see the [LICENSE.md](LICENSE.md) file for details.

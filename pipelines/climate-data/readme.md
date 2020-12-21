# climate-data

Making climate crisis data available to data scientists.  This package will download climate data into `$HOME/climate-data`.  Currently supported are the following datasets:
- CO2 concentration
- Global temperatures

For more background on this project read the [project page on Climate Code]().

## Setup

```bash
python setup.py install
```

## Usage

To download the entire dataset:

```bash
climate --datasets all
```

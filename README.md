# MultiPy

A powerful tool to research, build, and optimise multipliers.


# Why?

Generating and analysing multiplier designs by hand is labour intensive, even for small datasets. For entire [truth tables](https://en.wikipedia.org/wiki/Truth_table), this becomes close to impossible after 8-bits.

MultiPy aims to be a general tool for:

- Building partial product reduction layers
- Generate complete truth tables of custom multipliers
- Analyse and plot trends across entire datasets 
- Track bits, columns, rows of reduction stages


# Documentation

[link/to/documentation](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs)

???{

Use [typst](https://typst.app/)?

Use [sphinx](https://www.sphinx-doc.org/en/master/)?

}

# Setup


???{

-> Configure [TOML](https://toml.io/) file? and or use CLI to configure the TOML? -> main.py uses TOML to set variables

-> Choose default dataset or build own [Parquet](https://github.com/apache/parquet-format)?

-> import templates to /src/templates/
}

# Dependencies

| database | math    | visualization |
|:-------- |:------- |:------------- |
| [Parquet](https://github.com/apache/parquet-format)  | [NumPy](https://numpy.org/)   | [Matplotlib](https://matplotlib.org/ )   |
| [PyArrow](https://arrow.apache.org/docs/python/)     |                               | [Pillow](https://pillow.readthedocs.io/) |
| [Pandas](https://pandas.pydata.org/)                 |                               |                                          |

Full list TBD.

# Roadmap

- [ ] Manage dependencies and automatically resolve them -- [uv](https://docs.astral.sh/uv/)?
- [ ] Find optimal data structure for combinational multiply stages 
- [ ] Standardise templates
- [ ] Find optimal file format: parquet? postgre? json will not scale
- [ ] Custom reduction stage templates
- [ ] 8-bit unsaturated multiply
- [ ] 8-bit saturated multiply

Only after: optimal data structure, file formats and standardisation of loading and storing data, is a achieved can 16-bit can be attempted. The potential dataset of 16-bit+ multipliers becomes astronomical and the program must be rebust enough to deal with this efficiently.
- [ ] 16-bit unsaturated multiply
- [ ] 16-bit saturated multiply
- [ ] 32-bit saturated multiply

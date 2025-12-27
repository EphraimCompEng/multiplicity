# Multiplier Saturation
A project to aid research on multiplier saturation.
___

# Why?

Operations which do not need to exceed a ceiling, such as RGB and DSP calculations, saturate to a specific range of values.  

This project focuses on how [saturation](https://en.wikipedia.org/wiki/Saturation_arithmetic) effects the optimisation of a combinational [multiplier](https://en.wikipedia.org/wiki/Binary_multiplier). The goal is to find solutions for the saturation limit at the earliest point(s) in a multiplication stage, efficient partial product generation and reduction.


# Documentation

???

# Setup

-> Configure [TOML](https://toml.io/en/) file? and or use CLI to configure the TOML? -> main.py uses TOML to set variables

Choose an output format:

~json?~

parquet?



???

# Dependencies

???


# Roadmap

- [ ] Find optimal data structure for combinational multiply stages 
- [ ] Find optimal file format: parquet? postgre? json will not scale.
- [ ] Custom reduction stage templates
- [ ] 8-bit unsaturated multiply
- [ ] 8-bit saturated multiply

After optimal data structure, file formats and standardisation of loading and storing data, 16-bit can be attempted. The potential dataset of 16-bit+ multipliers becomes astronomical and the program must be rebust enough to deal with this efficiently.
- [ ] 16-bit unsaturated multiply
- [ ] 16-bit saturated multiply
# Roadmap


## Structures

The entire library functions via three structures: Algorithms which initialise a Matrix which are then subsequesntly reduced by templates.
- [x] Algorithm, Matrix and Template classes formalised
- [x] Correctly implement custom Types. (Templates need work -- Slices implemented)
- [x] simple templates 
- [ ] Complex templates 
- [ ] Simple reduction
- [ ] Complex reduction
- [x] Simple row map
- [ ] Complete map matrix
- [ ] Algorithm.state and .step()

## Algorithm
Wallace Tree multipliers will be the first focus of the library, before moving onto [Dadda](https://en.wikipedia.org/wiki/Dadda_multiplier) and signed multipliers.

Basic functionality; "simple templates", generate, analyse:

- [ ] 4-bit unsaturated multiplied [Built-in]\*
- [ ] 8-bit unsaturated multiplied [Built-in]
- [ ] 4-bit saturated multiplied [Built-in]
- [ ] 8-bit saturated multiplied [Built-in]
- [x] Truth table generation -> json
- [ ] Implement I/O via [Parquet](https://parquet.apache.org/)
- [ ] Truth table generation -> Parquet

\* Note: once built-in functions and classes are operational, hand crafted templates and maps will be be functional.
simple templates -> internally called patters, form -> complex templates.


## IO
- [ ] Basic analysis/visualisation of bit ranges
- [ ] Apply analytical functions to all stages
- [ ] Apply analytical functions to each stage
- [ ] Heatmaps? plots? Advanced visualisation


## Documentation

- [x] Sphinx implementation
- [x] Setup sphinx -> web based API reference
- [ ] Setup Github Wiki? For theory / internal systems
- [x] Improve API ref site with nicer HTML/CSS
- [ ] Add markdown(.md) Functionality to API ref
- [ ] Complete user guide
- [ ] Complete advanced guide
- [ ] Provide academic sources for algorithm docs

## Optimisation
The sheer amount of data produced for 16-bit+ multiplier truth tables becomes astronomical. The program must be robust enough to deal with this efficiently before tackling:
- [ ] Testing suite - Pytest
- [ ] Multiprocessing support to handle higher bit-widths
- [ ] 16-bit unsaturated multiplied
- [ ] 16-bit saturated multiplied
- [ ] Use [rust](https://github.com/PyO3/pyo3)? [numba](https://numba.pydata.org/)? for more performance?
- [ ] Research if 32/64/128-bit multipliers can be analysed in a reasonable time (1min? 5min? ???)


# Extend Built-in Algorithm Support 
Supported algoithms:
- [ ] [Wallace Tree](https://en.wikipedia.org/wiki/Wallace_tree)
- [ ] [Dadda multiplier](https://en.wikipedia.org/wiki/Dadda_multiplier)
- [ ] [Baugh–Wooley algorithm](https://www.researchgate.net/figure/llustration-of-an-8-bit-Baugh-Wooley-multiplication_fig2_224349123)
- [ ] [Booths Multiplication Algorithm](https://en.wikipedia.org/wiki/Booth%27s_multiplication_algorithm)

# Advanced Functionality
Once the library is stable and optimised:
- [ ] Decoder with custom encodings
- [ ] Optional Booth encoding instead of AND matrix
- [ ] "Timing" stages/templates/multipliers -- User defined latencies
- [ ] 32-bit ?
- [ ] 64-bit ?

# Implemented


### Starting point:

- [x] Manage dependencies and automatically resolve them -- [uv](https://docs.astral.sh/uv/)?
- [x] Find optimal data structure for reduction stages
- [x] Standardise templates 
- [x] Find optimal file format: [Parquet](https://parquet.apache.org/)
- [x] Custom reduction stage templates 
- [x] Automatic version control (MAJOR.MINOR.PATCH) -- uv
- [x] **Basic** testing

# Multiplier Saturation
A project to aid research in the saturation of multipliers.

# Why?

Operations which do not need to exceed a ceiling, such as RGB and DSP calculations, saturate to a specific range of values.  

This project focuses on how [saturation](https://en.wikipedia.org/wiki/Saturation_arithmetic) effects the optimisation of a combinational [multiplier](https://en.wikipedia.org/wiki/Binary_multiplier). The goal is to find solutions for the saturation limit at the earliest point(s) in a multiplication stage, efficient partial product generation and reduction.

## Combinational Multipliers

A combinational multiplier starts by creating all possible partial products. Then, reduces the number of partial products across multiple stages, eventually all products are reduced to one output.

For example, using a [Wallice tree](https://en.wikipedia.org/wiki/Wallice_tree)  to multiply 11 * 12: 

```
11 * 12 -> 0b1011 * 0b1100
```

Can be represented like so:
```
        1011
   [____0000] 0
   [___0000_] 0
   [__1011__] 1
   [_1011___] 1
   ----------
0b [10000100] -> 132
```

This is oversimplified and only 4-bit, but you get the idea.

Note that for any multiplication the output can be upto **2x** the input width.


## Saturation

Using the 11 * 12 example above, if the output was saturated to 4-bits, the result would be 15 since the maximum value is 0b1111 -> 15.
Typically, saturation restricts the output bit width to the input bit width. 

This project will work towards:
  - 8-bit with and without saturation 
  - 16-bit with saturation

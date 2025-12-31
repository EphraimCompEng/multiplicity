# Data Structure Overview
___
The representation of a combinational multiplier.


# AND Matrix
___
The AND matrix is a 2D array of bits that represents the AND operation between two input values. Each element in the matrix is the result of the AND operation between the corresponding bits of the two input values.

## Structure

[ Stage 0 ]

```
        b15-b8 | b7-b0
        -------+--------
        -------|00000000
        ------0|0000000-
        -----00|000000--
        ----000|00000---
        ---0000|0000----
        --00000|000-----
        -000000|00------
        0000000|0-------
```

# Partial Product Reduction
___
The partial product reduction stage reduces the number of partial products across multiple stages, eventually all products are reduced to one output.


## Stages

Each stage of a multiplier must reduce the number of partial products. 


A naive approach could look like this:


### [ Stage 0 ]


The AND matrix produces initial set of partial products, and the each template isolates 2 rows at a time:
```
        -------|00000000
        ------0|0000000-
```
```
        -----00|000000--
        ----000|00000---
```
```
        ---0000|0000----
        --00000|000-----
```
```
        -000000|00------
        0000000|0-------
```


### [ Stage 1 ]


Each group of partial products are reduced, via additions, and are grouped for the next stage:
```
        -----00|00000000
        ---0000|00000---
```
```
        -000000|0000----
       00000000|00------
```


### [ Stage n ]


The final reduction results in a single complete value:

```
       00000000|00000000
```


In the [original](first/init/) program data was stored in json and could easily be prettified. However, working the stored structures seemed impossible and the project ended there. This time round there will be a big focus on data structures, allowing for robust analytics, as well as human readable data using matplotlib.

- [ ] Find optimal data structure for combinational multiply stages

### Simple Templates

As mentioned above, each stage recieves a template to dictate how partial products are grouped and operated on. 

Templates need to be simple enough to configure, possibly in a CLI but the main focus is on a configuration file. 

- [ ] Standardise templates



### [ Adder: 2 -> 1 ]


The naive reduction layer used a simple array to define the reduction layer. Each letter identifies bits to be grouped into a "cells". In this case, these cells would represent:
```
  [ Template Gen. ] [ Array ] [ Output         ]
  --------|WWWWWWW0 [  "W",                
  ------#W|WWWWWWW-    "W"     ------#W|WWWWWWW-       
                                  
  ------XX|XXXXX0--    "X",              
  ----#XXX|XXXXX---    "X",    ----#XXX|XXXXX---       
                                  
  ----YYYY|YYY0----    "Y",              
  --#YYYYY|YYY-----    "Y",     -#YYYYY|YYY-----         
                                  
  --ZZZZZZ|Z0------    "Z",              
  #ZZZZZZZ|Z-------    "Z"  ]   ZZZZZZZ|Z-------           
```

Note that the "first" bit of each layer is ignored in the addition - these bits will never generate a carry as the input would be 1 + 0 or 0 + 0. Unlike the "last" bit which has the potential to carry from previous bits, with the final possible carry represented with "#". Also note that these caracters are only used for positional information. Other alphabetical characters can be used in the same style.



### [ CSA: 3 -> 2 ]


Another a reduction layer could use [CSAs](https://en.wikipedia.org/wiki/Carry-save_adder) used a simple array to define the reduction layer.
```
  [ Template      ] [ Array ] [ Output        ]
  --------|xXxXxXx0 [  "X",  
  ------#X|xXxXxXx-    "X",   ------0X|xXxXxXx-  
  ------0X|xXxXxX--    "X",   ------Xx|XxXxXx--  

  -----yYy|YyYy0---    "Y", 
  ---#YyYy|YyYy----    "Y",   ---0YyYy|YyYy----  
  ---0YyYy|YyY-----    "Y",   ---YyYyY|yYy-----

  --ZZZZZZ|Z0------    "Z",  
  #ZZZZZZZ|Z-------    "Z"  ] #ZZZZZZZ|Z-------
```

Here, each CSA reduced 3 inputs to 2. The output is reordered to mirror how each bit of the CSA calculation is distributed, plus swapping the leftover bit to fit the distribution. For more information see [reduction](link/to/reduction).


As you can see the MultiPy can distinguish between reduction using adder or CSAs by the run of a given string. However, these templates are very simple and offer little fine-grain control. To enable complex templates, matrices can be used. For more information see [templates](link/to/templates)

# Datasets

parquet
...

see [datasets](link/to/datasets)

# Simple Visualisation

ascii
matplotlib - heatmap

...

see [visualise](link/to/visualise)

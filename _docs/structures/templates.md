# Templates









As mentioned above, each stage recieves a template to dictate how partial products are grouped and operated on. 

Templates need to be simple enough to configure, possibly in a CLI but the main focus is on a configuration file. 

- [ ] Standardise templates



### [ Adder: 2 -> 1 ]


The adder reduction layer used a vector to define the reduction layer. Each letter identifies bits to be grouped into a "cells". In this case, these cells would represent:
```
  [ Template Gen. ] [ Vector ] [ Output        ]
  --------|WWWWWWW0 [  "W",                
  ------#W|WWWWWWW-    "W"     ------#W|WWWWWWW-       
                                  
  ------XX|XXXXX0--    "X",              
  ----#XXX|XXXXX---    "X",    ----#XXX|XXXXX---       
                                  
  ----YYYY|YYY0----    "Y",              
  --#YYYYY|YYY-----    "Y",    --#YYYYY|YYY-----         
                                  
  --ZZZZZZ|Z0------    "Z",              
  #ZZZZZZZ|Z-------    "Z"  ]  #ZZZZZZZ|Z-------           
```

Note that the "first" bit of each layer is ignored in the addition - these bits will never generate a carry as the input would be 1 + 0 or 0 + 0. Unlike the "last" bit which has the potential to carry from previous bits, with the final possible carry represented with "#". Also note that these caracters are only used for positional information. Other alphabetical characters can be used in the same style.



### [ CSA: 3 -> 2 ]


Another a reduction layer could use [CSA](https://en.wikipedia.org/wiki/Carry-save_adder)s. The utility of a CSA is the size and speed of it's circuit. Instead of wasting space using large full adders, many smaller CSAs will produce the same reduction, faster.

Once again, a vector can define the reduction layer.
```
  [ Template      ] [ Vector ] [ Output        ]
  --------|xXxXxXx0 [  "X",  
  ------#X|xXxXxXx-    "X",    ------0X|xXxXxXx-  
  ------0X|xXxXxX--    "X",    ------Xx|XxXxXx--  

  -----yYy|YyYy0---    "Y", 
  ---#YyYy|YyYy----    "Y",    ---0YyYy|YyYy----  
  ---0YyYy|YyY-----    "Y",    ---YyYyY|yYy-----

  --ZZZZZZ|Z0------    "Z",  
  #ZZZZZZZ|Z-------    "Z"  ]  #ZZZZZZZ|Z-------
```

Here, each CSA reduced 3 inputs to 2. The output is reordered to mirror how each bit of the CSA calculation is distributed, plus swapping the leftover bit to fit the distribution. For more information see [reduction](link/to/reduction).


As you can see the MultiPy can distinguish between reduction using adder or CSAs by the run of a given string. However, these templates are very simple and offer little fine-grain control. To enable complex templates, matrices can be used.




```
    FEDCBA9876543210| bit
    ----------------+-----
    ________00000000|  0
    _______00000000_|  1
    ______00000000__|  2
    _____00000000___|  3
    ____00000000____|  4
    ___00000000_____|  5
    __00000000______|  6
    _00000000_______|  7
```

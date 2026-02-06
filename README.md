# multiplied

A powerful tool to build, test, and analyse multiplier designs.

## Why?

Generating and analysing multiplier designs by hand is labour intensive, even
for small datasets, for entire [truth tables](https://en.wikipedia.org/wiki/Truth_table)
, this is close to impossible.

multiplied is built to streamline:

- Custom partial product reduction via [templates](https://github.com/EphraimCompEng/multiplied/blob/master/docs/structures/templates.md)
- Generating complete truth tables
- Analysis, plotting, and managing datasets
- Fine-grain access to bits, words or stages

## Setup

```sh
pip install multiplied
```

```Python
import multiplied as mp
```

## Algorithm Execution

A quick demo of a simple 8-bit multiplier executing 42*255:

```python
m = mp.Matrix(8) 
p = mp.Pattern(['a','a','b','b','c','c','d','d'])
alg = mp.Algorithm(m)
alg.push(p)
alg.auto_resolve_stage() 
a=42
b=255
for m in alg.exec(a=a, b=b).values():
    print(m)

# convert result to decimal
print(int("".join(alg.matrix.matrix[0]), 2))
print(a*b)
```

```text
________00101010
_______00101010_
______00101010__
_____00101010___
____00101010____
___00101010_____
__00101010______
_00101010_______

______0001111110
____0001111110__
__0001111110____
0001111110______
________________
________________
________________
________________

__00011001100110
___0001111110___
0001111110______
________________
________________
________________
________________
________________

0001101000010110
_00011111100____
________________
________________
________________
________________
________________
________________

0010100111010110
________________
________________
________________
________________
________________
________________
________________

10710
10710
```

## Pattern Based Algorithm

Multiplied assists in template generation to create reusable algorithm objects:

- Patterns are used to build simple templates
- Pseudo outputs help visualise where bits from a given arithmetic unit will land
- Automatic grouping/mapping based on empty rows or dadda style mappings
- Nonessential bits are hidden with underscores for visual clarity

Here's the algorithm from the previous example:

```python
# stage : {
#     "template" : mp.Template, -> template, result
#     "pseudo"   : mp.Matrix,
#     "map"      : mp.Map
# }
print(alg)
```

```text

0:{

template:{

________AaAaAaAa
_______aAaAaAaA_
______BbBbBbBb__
_____bBbBbBbB___
____CcCcCcCc____
___cCcCcCcC_____
__DdDdDdDd______
_dDdDdDdD_______

______AaAaAaAaAa
________________
____BbBbBbBbBb__
________________
__CcCcCcCcCc____
________________
DdDdDdDdDd______
________________
}

pseudo:{

______AaAaAaAaAa
____BbBbBbBbBb__
__CcCcCcCcCc____
DdDdDdDdDd______
________________
________________
________________
________________
}

map:{

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FE FE FE FE FE FE FE FE FE FE FE FE FE FE FE FE
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FD FD FD FD FD FD FD FD FD FD FD FD FD FD FD FD
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
}

1:{

template:{

______AaAaAaAaAa
____AaAaAaAaAa__
__AaAaAaAaAa____
BbBbBbBbBb______
________________
________________
________________
________________

__AaAaAaAaAaAaAa
___AaAaAaAaAa___
________________
BbBbBbBbBb______
________________
________________
________________
________________
}

pseudo:{

__AaAaAaAaAaAaAa
___AaAaAaAaAa___
BbBbBbBbBb______
________________
________________
________________
________________
________________
}

map:{

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
}

2:{

template:{

__AaAaAaAaAaAaAa
___aAaAaAaAaA___
AaAaAaAaAa______
________________
________________
________________
________________
________________

AaAaAaAaAaAaAaAa
_AaAaAaAaAaA____
________________
________________
________________
________________
________________
________________
}

pseudo:{

AaAaAaAaAaAaAaAa
_AaAaAaAaAaA____
________________
________________
________________
________________
________________
________________
}

map:{

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
}

3:{

template:{

AaAaAaAaAaAaAaAa
_aAaAaAaAaAa____
________________
________________
________________
________________
________________
________________

AaAaAaAaAaAaAaAa
________________
________________
________________
________________
________________
________________
________________
}

pseudo:{

AaAaAaAaAaAaAaAa
________________
________________
________________
________________
________________
________________
________________
}

map:{

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
}
```

## Documentation

Resources for usage, general theory and implementations can be found in [/docs/](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs).
For the API Reference head to Multiplied documentation [site](https://ephraimcompeng.github.io/multiplied/)

## Dependencies

Planned or currently in use.

| database                                           | visualization                        |
|:---------------------------------------------------|:-------------------------------------|
| [Parquet](https://github.com/apache/parquet-format)|[Matplotlib](https://matplotlib.org/ )|
| [Pandas](https://pandas.pydata.org/)               |                                      |

Full list TBD.

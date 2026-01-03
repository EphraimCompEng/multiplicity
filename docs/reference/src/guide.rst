.. _guide:
==========
User Guide
==========

soon™

(below is an incomplete guide which will grow with the project.)


setup:

- import multipy as mp
- define matrix size
- create algorithm object
- create and store templates in algorithm

Algorithm process:
0: Generate logical AND matrix
1: split matrix
2: apply template, update state
3: generate result
4: optionally apply map
5: update matrix
6: GOTO 1:

=====
Setup
=====

First, import multipy and decide on a bitwidth for our algorithm, to keep it simple let's pick 4-bits:

.. code-block:: python

    import multipy as mp
    matrix = mp.Matrix(4) # 4-bit logical AND matrix

Here's what it looks like:

.. code-block:: python

    print(matrix.matrix)

.. code-block:: python

    ____0000
    ___0000_
    __0000__
    _0000___


The ``matrix`` is a "structure" used to generate the logical AND matrix, aka partial products, for a given set of inputs. It also tells the algorithm *where* each partial product is located.

.. note::
    To populated an AND matrix without an Algorithm object use:

    .. code-block:: python

        matrix = mp.build_matrix(operand_a=0, operand_b=0, bits=4)



Next, create an algorithm object.

.. code-block:: python

    algorithm = mp.Algorithm(matrix)

The Algorithm object will hold the templates that define a given algorithm. It also holds an internal state to track which template it should use next.

Now let's make some templates. This involves figuring out where you want to place:

- Carry Save Adders -- CSA (Half Adders, HA, are automtically placed when using simple templates) [3 to 2]
- Adders -- [2 to 1]
and in the future:

- Decoders -- [n to n-k]
- Greedy Adders -- Adder which makes use of carry in (cin) [2 to 1]

All of which reduce a set of partial products by 1, each with their characteristics in latency, complexity and size. None of this applies to Multipy.
Decoders are an exception and can potentially reduce a set of partial products by more than 1.

To inform the algorithm on how a given template reduces groups of partial products, an array of characters, or pattern is used:

.. code-block:: python

    pattern = [
        a,      # +-
        a,      # | run of 3 == CSA [3 to 2]
        a,      # +-
        b,      # +- run of 1 == None -- no reduction needed
    ]

.. note::
    Multipy will allow you to make any algorithm, even if it's sub-optimal.

For this 4-bit multiplier algorithm it will take 3 rounds, minimum, of reductions to reach out final output:

.. code-block:: text

    1st:    2nd:    3rd:    output:
    a
    a       c
    a       c       d
    b       c       d       x

Each step needs a pattern or a template. Let's turn our first pattern into a template:

.. code-block:: python

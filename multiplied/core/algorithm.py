###########################################
# Algorithm Defined By Templates and Maps #
###########################################


"""
Algorithm process:
0: Generate logical AND matrix
1: split matrix
2: apply template, update state
3: generate result
4: optionally apply map
5: update matrix
6: GOTO 1:

"""

from typing import Any
import multiplied as mp

class Algorithm():
    """
    An algorithm is created with an initial matrix and an optinal map.
    Subsequent stages are defined by templates and maps. Built-in methods
    can automatically generate stages or assist in the creation of custom
    stages.
    """

    # pattern only implementation -- small steps:
    #
    #   > detect pattern inside Template object
    #   > Slice matrix(data) along pattern "runs"
    #   > reduce slices
    #   > unify slices
    #   > apply row map
    #   > update Algorithm object state


    def __init__(self, matrix: mp.Matrix) -> None:
        self.bits      = len(matrix)
        self.state     = 0
        self.matrix    = matrix
        self.algorithm = {}
        self.len       = len(self.algorithm)
        self.stage     = self.algorithm[self.state] if self.len > 0 else None

    def __str__(self) -> str:
        return mp.pretty(self.algorithm)

    def __repr__(self) -> str:
        return str(self.__str__())


    def __getitem__(self, index) -> dict:
        return self.algorithm[index]

    def __iter__(self):
        return iter(self.algorithm)

    def __next__(self):
        if self.index >= self.bits:
            raise StopIteration
        self.index += 1
        return self.algorithm[self.index - 1]





    def push(self, template: mp.Template | mp.Pattern, map_: Any = None
    ) -> None:
        """
        Populates stage of an algorithm based on template. Generates pseudo
        result to represent output matrix

        >>> self.algorithm[x] = {
        >>>     "template" : mp.Template,
        >>>     "pseudo"   : mp.Matrix,
        >>>     "map"      : mp.Map}
        """

        if not(isinstance(template, (mp.Template, mp.Pattern))):
            raise TypeError("Invalid argument type. Expected mp.Template")
        if template.bits != self.bits:
            raise ValueError("Template bitwidth must match Algorithm bitwidth.")
        if map_ and not(isinstance(map_, (mp.Map))):
            raise TypeError("Invalid argument type. Expected mp.Map")

        # -- [TODO] ------------------------------------------------- #
        if map_ and not map_.rmap:                                    #
            raise NotImplementedError("Complex map not implemented")  #
        # ----------------------------------------------------------- #

        if isinstance(template, mp.Pattern):
            template = mp.Template(template)

        stage_index = len(self.algorithm)
        result = mp.Matrix(template.result)

        if not map_ and result:
            map_ = result.resolve_rmap()
            result.apply_map(map_)
        else:
            result.apply_map(map_)

        stage = {
            'template': template,
            'pseudo': result,
            'map': map_,
        }
        self.algorithm[stage_index] = stage

        return


    # Mangled as execution order is sensitive and __reduce should only
    # be called by the algorithm itself via: self.step(), or self.exec()
    def __reduce(self) -> None:
        """
        use template or pattern to reduce a given matrix.
        """

        # -- pattern implementation ---------------------------------
        #
        # For a given 'run', the length of that run will determine
        # the height for which to count 1s in a given column:
        #
        # run = 3 := CSA; carry is placed to the left of source column
        # and one row down to avoid corrupting adjacent columns
        #
        #   [input-------] | [output------]
        #   ...00100010... | ...00100010...
        #   ...00101010... | ...01010100...
        #   ...00101010... | ...________...
        #
        # run = 2 := binary addition; carry generates through propagates
        #
        #   [input-------] | [output------]
        #   ...00110110... | ...01100000...
        #   ...00101010... | ...________...

        # -- partition ----------------------------------------------

        # all_chars = set(set(row) for all rows) ?
        # partition_table = {ch:[] for ch in all_chars}
        # for row in rows:
        #
        #   for char in chars:
        #       i = 0
        #       partition_row = []
        #       while char != row[i]:
        #           partition_row.append('_')
        #           i+=1
        #       while char == row[i]:
        #           partition_row.append('_')
        #           i+=1
        #       n = len(partition_row)
        #       partition_row += ['_' for _ in range(self.bits - n)]
        #


        # -- CSA ----------------------------------------------------



        # -- ADD ----------------------------------------------------



        ...


    def step(self, matrix: mp.Matrix) -> None:
        """
        Take template[internal_state], apply to matrix, advance internal_state
        """
        ...

    def exec(self,):
        """
        Run algorithm with a single set of intputs then reset internal state
        """
        ...

    def reset(self,):
        """
        Reset internal state and submit new initial matrix
        """
        ...


    def auto_resolve_stage(self, *, recursive=True,
    ) -> None:
        """
        Automatically resolve pattern using the previous stage and creates
        a new algoritm stage.

        Options:
            recursive: Recursively resolve until no partial products remain
        """

        # -- non recursive ------------------------------------------
        if not self.algorithm:
            pseudo = self.matrix
        else:
            pseudo = self.algorithm[self.len]['pseudo']
        pattern = mp.resolve_pattern(pseudo)
        self.push(mp.Template(pattern, matrix=pseudo))
        if not recursive:
            return

        # -- recursive setup ----------------------------------------
        pseudo    = self.algorithm[len(self.algorithm)-1]['pseudo']
        condition = self.bits-1 != mp.empty_rows(pseudo)
        if not condition:
            return

        # -- main loop ----------------------------------------------
        while condition:

            # Stage generation
            new_pattern = mp.resolve_pattern(pseudo)
            self.push(mp.Template(new_pattern, matrix=pseudo))

            # Condition based on generated stage
            pseudo    = self.algorithm[len(self.algorithm)-1]['pseudo']
            condition = self.bits-1 != mp.empty_rows(pseudo)
        return

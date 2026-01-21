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
        self._index    = 0

    def __str__(self) -> str:
        return mp.pretty(self.algorithm)

    def __repr__(self) -> str:
        return str(self.__str__())


    def __getitem__(self, index) -> dict:
        return self.algorithm[index]

    def __iter__(self):
        return iter(self.algorithm)

    def __next__(self):
        if self._index >= self.bits:
            raise StopIteration
        self._index += 1
        return self.algorithm[self._index - 1]


    # Mangled as execution order is sensitive and __reduce should only
    # be called by the algorithm itself via: self.step(), or self.exec()
    def __reduce(self):
        """
        use template or pattern to reduce a given matrix.
        """

        # -- pattern implementation ---------------------------------
        #
        # For a given 'run', the length of that run will determine
        # the height for which to count 1s in a given column:
        #
        # run = 3 := CSA; carry by placing bit left of source column
        # (bit will be placed one row below source row for visual sugar)
        #
        #   [input--------] | [output-------]
        #   ..-+-+-+-+-+-.. | ..-+-+-+-+-+-..
        #   .. |0|0|1|1| .. | .. |1|1|1|0| ..
        #   ..-+-+-+-+-+-.. | ..-+-+-+-+-+-..
        #   .. |1|1|1|0| .. | .. |0|1|1|?| ..
        #   ..-+-+-+-+-+-.. | ..-+-+-+-+-+-..
        #   .. |0|1|1|1| .. | .. |0|0|0|0| ..
        #   ..-+-+-+-+-+-.. | ..-+-+-+-+-+-..

        # --

        ...



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



    # def truth(self, matrix: mp.Matrix, template: mp.Template) -> None:
    #     ...

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


    # Used to automate splitting a matrix into Slice(n * row)
    @classmethod
    def split(cls, matrix: mp.Matrix, rows: int) -> list[mp.Slice]:
        """
        Returns list of slices via progressive allocation. Used to automate
        slicing a matrix into (Slice(n * row) * k), then splitting remainder.

        Append n contiguous slices of matrix to list, each containing x rows.
        If not enough rows, progress to rows-1 -> row-2 -> ...
        """

        # > find non zero rows
        # > formula can be found for progressive allocation
        empty_rows = mp.empty_rows(matrix)



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
        pseudo = self.algorithm[len(self.algorithm)-1]['pseudo']
        condition = self.bits-1 != mp.empty_rows(pseudo)
        if not condition:
            return


        # -- main loop ----------------------------------------------
        while condition:

            # Stage generation
            new_pattern = mp.resolve_pattern(pseudo)
            self.push(mp.Template(new_pattern, matrix=pseudo))

            # Condition based on generated stage
            pseudo      = self.algorithm[len(self.algorithm)-1]['pseudo']
            condition   = self.bits-1 != mp.empty_rows(pseudo)
        return

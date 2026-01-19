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

class Algorithm(mp.Matrix):
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
        pretty_ = ""
        for i, m in self.algorithm.items():
            pretty_ += f"\n[S{i}]\n\n"
            for j, k in m.items():
                if k:
                    pretty_ += f"{j}:\n{mp.pretty(k)}\n"
        return pretty_

    def __repr__(self) -> str:
        return str(self)

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



    def push(self, template: mp.Template, map: Any = None) -> None:
        """
        Populates stage of an algorithm based on template. Generates pseudo
        result to represent output matrix

        >>> self.algorithm[x] = {
        >>>     "template" : mp.Template,
        >>>     "pseudo"   : mp.Matrix,
        >>>     "map"      : mp.Map}
        """

        if not(isinstance(template, mp.Template)):
            raise TypeError("Invalid argument type. Expected mp.Template")
        if template.bits != self.bits:
            raise ValueError("Template bitwidth must match Algorithm bitwidth.")
        if map and not(isinstance(map, mp.Map)):
            raise TypeError("Invalid argument type. Expected mp.Map")

        # -- [TODO] ------------------------------------------------- #
        if not map.rmap:                                              #
            raise NotImplementedError("Complex map not implemnted")   #
        # ----------------------------------------------------------- #

        stage = {'template': template}
        stage_index = len(self.algorithm)
        if not map:
            self.algorithm[stage_index] = stage
            return







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
    def split(cls, matrix: mp.Matrix, rows: int) -> mp.Slice:
        """
        Returns list of slices via progressive allocation. Used to automate
        slicing a matrix into (Slice(n * row) * k), then splitting remainder.

        Append n contiguous slices of matrix to list, each containing x rows.
        If not enough rows, progress to rows-1 -> row-2 -> ...
        """
        x = 0
        if len(matrix) - (x * rows) < rows:
            ...
        ...

    def auto_resolve_pattern(self, pattern: mp.Pattern, matrix: mp.Matrix, *,
        populate=True,
        recursive=False,
    ) -> None | dict:
        """
        Automatically resolve pattern using matrix form the previous stage to
        produce a new stage of the algoritm.

        Options:
            populate: Add stage to algorithm or return stage as dict
            recursive: Recursively resolve until no partial products remail
        """

        # Recursively resolving patterns require applying a stage's map to
        # its template:
        #
        # > prior_map(prior_template) -> current pseudo_matrix
        # > pseudo_matrix -> create new_template
        # > resolve_map(new_template.resultant) -> new_map
        # > new stage = {map: new_map, matrix: None, template: new_template}
        #

        # -- apply prior map ----------------------------------------

        peek_stage = self.algorithm[len(self.algorithm) - 1]
        prior_map  = peek_stage['map']
        if prior_map:
            prior_template = peek_stage['template']
            prior_result = mp.Matrix(prior_template.result)
            ...

        # -- create pseudo_matrix -----------------------------------

        # -- create new_template ------------------------------------
        runs = pattern.get_runs()

        # -- resolve_map --------------------------------------------
        ...

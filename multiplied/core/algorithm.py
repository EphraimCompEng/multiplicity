###########################################
# Algorithm Defined By Templates and Maps #
###########################################

from typing import Any, Iterable
import multiplied as mp

class Algorithm():
    """
    Manages and sequences operations via a series of stages defined by templates and maps.
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
        if not isinstance(matrix, mp.Matrix):
            raise TypeError(f"Expected Matrix, got {type(matrix)}")
        self.bits      = len(matrix)
        self.state     = 0
        self.matrix    = matrix
        self.algorithm = {}
        self.len       = len(self.algorithm)

        # -- TODO: update this when anything is modified ------------
        # create update() function
        # add to each modifying class method
        self.stage = self.algorithm[self.state] if self.len > 0 else None
        return None


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
        return None


    # Mangled as execution order is sensitive and __reduce should only
    # be called by the algorithm itself via: self.step(), or self.exec()
    def __reduce(self) -> None:
        """
        use template or pattern to reduce a given matrix.
        """
        from copy import copy

        # -- implementation -----------------------------------------
        #
        # Arithmetic units are defined by how many rows they cover, or
        # their 'run', the length of which determines the type of unit:
        #
        # run = 3:
        #   CSA: carry is placed to the left of source column
        #   and one row down to avoid corrupting adjacent columns
        #
        #   [input-------] | [output------]
        #   ...00100010... | ...00100010...
        #   ...00101010... | ...01010100...
        #   ...00101010... | ...________...
        #
        # run = 2:
        #   binary adder: carry generates through propagates
        #
        #   [input-------] | [output------]
        #   ...00110110... | ...01100000...
        #   ...00101010... | ...________...

        # -- isolate units -----------------------------------------
        template = self.algorithm[self.state]['template']
        units    = isolate_arithmetic_units(template)
        n        = self.bits*2
        results  = []

        # -- reduce -------------------------------------------------
        for unit in units:
            base_index = unit.checksum.index(1)
            match sum(unit.checksum):
                case 1: # NOOP
                    output = [copy(self.matrix[base_index][0])]

                case 2: # ADD
                    operand_a = copy(self.matrix[base_index][0])
                    operand_b = copy(self.matrix[base_index+1][0])
                    checksum  = [False] * n

                    # -- skip empty rows ----------------------------
                    start = 0
                    while operand_a[start] == '_' and operand_b[start] == '_':
                        start += 1

                    for i in range(start, n):
                        # -- row checksum ---------------------------
                        if operand_a[i] != '_' or operand_b[i] != '_':
                            checksum[i] = True

                        # -- normalise binary -----------------------
                        if operand_a[i] == '_' and operand_b[i] != '_':
                            operand_a[i] = '0'

                        elif operand_b[i] == '_' and  operand_a[i] != '_':
                            operand_b[i] = '0'

                        elif operand_a[i] == '_' and operand_b[i] == '_':
                            operand_a[i] = '0'
                            operand_b[i] = '0'

                    # -- binary addition ----------------------------
                    bits_ = sum(checksum)
                    int_a = int("".join(operand_a[start:start+bits_]), 2)
                    int_b = int("".join(operand_b[start:start+bits_]), 2)

                    output     = [['_']*(start-1)]
                    output[0] += list(f"{int_a+int_b:0{bits_+1}b}")
                    output[0] += ['_']*(n-start-bits_)


                case 3: # CSA
                    operand_a = copy(self.matrix[base_index][0])
                    operand_b = copy(self.matrix[base_index+1][0])
                    operand_c = copy(self.matrix[base_index+2][0])
                    checksum  = [False]*n
                    output    = [['_']*n, ['_']*n]
                    start     = 0

                    # -- skip empty rows ----------------------------
                    while operand_a[start] == '_' and operand_b[start] == '_':
                        start += 1

                    # -- sum columns -------------------------------
                    for i in range(start, n):
                        csa_sum = 0
                        csa_sum += 1 if operand_a[i] == '1' else 0
                        csa_sum += 1 if operand_b[i] == '1' else 0
                        csa_sum += 1 if operand_c[i] == '1' else 0

                        output[0][i] = csa_sum
                        checksum[i]  = (
                            operand_c[i] != '_' or
                            operand_b[i] != '_' or
                            operand_a[i] != '_'
                        )

                        # -- check end of unit ----------------------
                        if not checksum[i]:
                            break

                        # -- brute force index 0 --------------------
                        # ! handle index zero outside of loop ! #
                        # ! unit may not even overlap index 0
                        try:
                            output[0][i] = '1' if csa_sum & 1 else '0'
                            j            = i-1 if 0 <= i-1 else i
                            output[1][j] = '1' if csa_sum & 2 else '0'
                        except IndexError:
                            continue
                case _:
                    raise ValueError(f"Unsupported unit type:\n{mp.pretty(unit)}")

            # -- build unit into matrix -----------------------------
            unit_result = [['_']*(self.bits*2) for _ in range(base_index)]
            for row in output:
                unit_result.append(row)
            for _ in range(base_index+len(output), self.bits):
                unit_result.append(['_']*(self.bits*2))
            results.append(mp.Matrix(unit_result))

        print(results)
        for i in results:
            print(f"\n{mp.pretty(i)}")









        # -- merge units to matrix ----------------------------------
        # Merge in any order, checking for overlaps between borders
        # resolve conflicts by summing present bit positions and shifting
        # a target unit's bit

        # ! difficult sanity checks --------------------------------- #
        # Complex scenarios, where NOOP, CSA and ADD units intersect
        # will require extensive checks:
        #
        #   [example--] || [isolated]
        #   ...BbaAa... || ....ba....
        #   ...CcaAa... || ....ca....
        #   ...CcaAa... || ....ca....
        #
        #
        # If repeated along the same y-axis, resolution can get very tricky.
        # One method could be skipping merges and opting for merges with non
        # conflicting units, repeat until few partially merged templates remain
        # and finally resolve conflicts, if possible.
        #
        # These conflicts can quickly be found by checking the sum of possible
        # bit positions in a given region of intersecting arithmetic units.
        # The example's sum for the first column is == 3.  This should raise a
        # flag indicating it should be merged later.
        #
        #
        # This functionality to be implemented at a later date.

        return None

    def auto_resolve_stage(self, *, recursive=True,
    ) -> None:
        """
        Automatically resolve pattern using the previous stage and creates
        a new algorithm stage.

        Options:
            recursive: Recursively resolve until no partial products remain
        """
        from copy import copy
        # -- non recursive ------------------------------------------
        if not self.algorithm:
            pseudo = copy(self.matrix)
        else:
            pseudo = copy(self.algorithm[self.len]['pseudo'])
        pattern = mp.resolve_pattern(pseudo)
        self.push(mp.Template(pattern, matrix=pseudo))
        if not recursive:
            return None


        # -- main loop ----------------------------------------------
        while self.bits-1 != mp.empty_rows(pseudo):

            # Stage generation
            new_pattern = mp.resolve_pattern(pseudo)
            self.push(mp.Template(new_pattern, matrix=pseudo))

            # Condition based on generated stage
            pseudo = copy(self.algorithm[len(self.algorithm)-1]['pseudo'])

        return None

    def step(self) -> None:
        """
        Take template[internal_state], apply to matrix, advance internal_state
        """
        self.__reduce()
        self.state += 1

        return None

    def exec(self) -> None:
        """
        Run algorithm with a single set of inputs then reset internal state
        """
        for stage in self.algorithm:
            self.__reduce()
        return None


    def reset(self, matrix: mp.Matrix) -> None:
        """
        Reset internal state and submit new initial matrix
        """
        if not isinstance(matrix, mp.Matrix):
            raise TypeError(f"Expected Matrix, got {type(matrix)}")
        self.matrix = matrix
        self.state = 0
        return None


    def __str__(self) -> str:
        return mp.pretty(self.algorithm)

    def __repr__(self) -> str:
        return f"<multiplied.{self.__class__.__name__} object at {hex(id(self))}>"

    def __len__(self) -> int:
        return len(self.algorithm)

    def __getitem__(self, index) -> dict:
        return self.algorithm[index]

    def __iter__(self) -> Iterable:
        return iter(self.algorithm.items())

    def __next__(self) -> dict:
        if self.index >= len(self.algorithm):
            raise StopIteration
        self.index += 1
        return dict(self.algorithm[self.index - 1])



# -- helper functions -----------------------------------------------


def isolate_arithmetic_units(matrix: mp.Template) -> list[mp.Template]:
    """
    Separate arithmetic units from source template into a list of templates.
    """

    if not isinstance(matrix, mp.Template):
        raise TypeError(f"Expected type Template got {type(matrix)}")

    allchars  = mp.allchars(matrix.template, hash=matrix.checksum)
    arithmetic_units = []*len(allchars)
    for char in allchars:
        row  = 0
        unit = [[]]*matrix.bits
        empty_row   = ['_']*(matrix.bits*2)
        # -- skip rows not containing char --------------------------
        # replace with checksum calculation
        while row < matrix.bits:
            if char not in matrix.template[row]:
                unit[row] = empty_row
                row += 1
                continue
            break

        # -- extract unit(s) ----------------------------------------
        charset = set([char.upper(),char.lower()])
        while(row < matrix.bits and
            (charset.intersection(matrix.template[row]))
        ):

            tmp  = ['_']*(matrix.bits*2)
            last = None
            intra_row_transition = []
            for i, b in enumerate(matrix.template[row]):
                if b in charset:
                    # -- vertical intra-row check ------------------------------------ #
                    if last not in charset:                                            #
                        intra_row_transition.append(i)                                 #
                    if len(set(intra_row_transition)) != 1:                            #
                        irt_err = intra_row_transition[1]-1                            #
                        raise SyntaxError(                                             #
                            f"Intra-row Error [column {irt_err}]. Invalid template."   #
                        )                                                              #
                    # ---------------------------------------------------------------- #
                    tmp[i] = char
                last = b

            unit[row] = tmp
            row += 1
        # -- fill remaining rows ------------------------------------
        # replace with checksum calculation

        while 0 < (matrix.bits-row):
            unit[row] = empty_row
            row += 1

        arithmetic_units.append(mp.Template(unit))

    # -- ! unit sanity checks ! -------------------------------------

    # These checks are not exhaustive and will need revisiting.
    #
    # Intra-row check(above):
    #   - test if unit exists within a single block
    #   - currently naive but *should* catch real world cases
    #   - ! rigorous checks require testing:
    #       - Vertical(row check) (|) [Done]
    #       - Backwards diagonal  (\)
    #       - Forward diagonal    (/)
    #
    # Simple row check(below):
    #   - count template's non empty rows
    #   - count total number of rows units encompass
    #
    # These should catch most cases of non compliance in:
    #   - CSAs
    #   - Adders
    #   - ! Decoders will require checks once implemented

    # -- row check --------------------------------------------------
    unit_rows = [sum(i.checksum) for i in arithmetic_units]
    if sum(unit_rows) != sum(matrix.checksum):
        raise SyntaxError("Invalid template. Each unit must use unique char")

    return arithmetic_units

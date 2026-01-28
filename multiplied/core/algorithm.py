###########################################
# Algorithm Defined By Templates and Maps #
###########################################

from typing import Any, Callable, Iterable
import multiplied as mp

class Algorithm():
    """
    Manages and sequences operations via a series of stages defined by templates and maps.
    """

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


    def push(self, source: mp.Template | mp.Pattern, map_: Any = None
    ) -> None:
        """
        Populates stage of an algorithm based on template. Generates pseudo
        result to represent output matrix

        >>> self.algorithm[x] = {
        >>>     "template" : mp.Template,
        >>>     "pseudo"   : mp.Matrix,
        >>>     "map"      : mp.Map}
        """

        if source.bits != self.bits:
            raise ValueError("Template bitwidth must match Algorithm bitwidth.")
        if map_ and not(isinstance(map_, (mp.Map))):
            raise TypeError("Invalid argument type. Expected mp.Map")

        # -- [TODO] ------------------------------------------------- #
        if map_ and not map_.rmap:                                    #
            raise NotImplementedError("Complex map not implemented")  #
        # ----------------------------------------------------------- #

        if isinstance(source, mp.Pattern):
            template = mp.Template(source)
        elif isinstance(source, mp.Template):
            template = source
        else:
            raise TypeError("Invalid argument type. Expected mp.Template")


        if not isinstance(template.result, list):
            raise ValueError("Template result is unset")


        result      = mp.Matrix(template.result)
        stage_index = len(self.algorithm)
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
                        # ! remove try catch:
                        # ! handle index zero outside of loop
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


        # -- merge units to matrix ----------------------------------
        # Merge in any order, checking for overlaps between borders
        # resolve conflicts by summing present bit positions and shifting
        # a target unit's bit

        # ! difficult sanity checks --------------------------------- ! #
        # Complex scenarios, where NOOP, CSA and ADD units intersect
        # will require extensive checks:
        #
        #   [example--] || [region--]
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
        # This functionality to be implemented at a later date.


        # testing
        for i in results:
            print(f"\n{mp.pretty(i)}")


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

    def step(self) -> mp.Matrix:
        """
        Execute the next stage of the algorithm and update internal matrix
        """
        self.__reduce()
        self.state += 1

        # getattr for matrix, template and map to peek algorithm
        return self.matrix

    def exec(self, *, a=0, b=0) -> list[mp.Matrix]:
        """
        Run entire algorithm with a single set of inputs then reset internal state.
        Returns list of results from all stages of the algorithm
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError(f"Expected int, got {type(a)} and {type(b)}")

        if a == 0 or b == 0:
            return [mp.Matrix(self.bits)]

        for stage in self.algorithm:
            self.__reduce()
        return []

    def reset(self, matrix: mp.Matrix) -> None:
        """
        Reset internal state and submit new initial matrix
        """
        if not isinstance(matrix, mp.Matrix):
            raise TypeError(f"Expected Matrix, got {type(matrix)}")
        self.matrix = matrix
        self.state = 0
        return None

    # ! getattr for matrix, template and map to peek algorithm

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

def horizontal_bounds(source: mp.Matrix | mp.Map | mp.Template
) -> list[tuple[int,int]]:
    if not isinstance(source, (mp.Matrix, mp.Map, mp.Template)):
        raise TypeError(
            f"Expected type Matrix or Template got {type(source)}"
        )
    mp.validate_bitwidth(bits := source.bits)

    from copy import copy
    from multiplied import ischar, ishex2, isint

    bounds = []
    match source:
        case mp.Matrix():
            matrix = copy(source.matrix)
            # border:
                # '_'
                # {'0', '1'}
            # err:
                # {'0', '1'} -> '_' -> {'0', '1'}

            border = ({'_'}, {'0', '1'})
            transit = isint

            for y, row in enumerate(matrix):
                x = 0
                while x < len(row) and not transit(row[x]):
                    x += 1

                boundary = (x, y)
                while x < len(row):
                    if not transit(row[x]):
                        raise ValueError(f"Binary value containing {row[x]} at position ({x}, {y})")
                    x += 1

                bounds.append(boundary)


        case mp.Map():
            raise NotImplementedError("Map not supported")
            # border:
                # '00'
                # if 0 < int(x, 16) < 255
            # err:
                # if 2 < len(x) or not 0 < int(x, 16) < 255:

            matrix = copy(source.map)
        case mp.Template():
            raise NotImplementedError("Map not supported")
            # border:
                # '_'
                # ischar(ch)
            # err:
                # ch -> '_' -> ch
            matrix = copy(source.template)
        case _:
            raise TypeError(
                f"Expected type Matrix, Map or Template got {type(source)}"
            )

    start = source.checksum.index(1)
    for row in range(start, bits):
        ...




    return




def isolate_arithmetic_units(matrix: mp.Template) -> list[mp.Template]:
    """
    Separate arithmetic units from source template into a list of templates.
    """

    if not isinstance(matrix, mp.Template):
        raise TypeError(f"Expected type Template got {type(matrix)}")

    allchars = mp.allchars(matrix.template, hash=matrix.checksum)
    arithmetic_units = []*len(allchars)
    for char in allchars:
        row  = 0
        unit = [[]]*matrix.bits
        empty_row   = ['_']*(matrix.bits*2)
        # -- skip rows not containing char --------------------------
        # ! to be replaced with bounding box logic once objects
        # ! generate their own bounding box

        while row < matrix.bits:
            if char not in matrix.template[row]:
                unit[row] = empty_row
                row += 1
                continue
            break

        # -- extract unit(s) ----------------------------------------
        # ! does not make use of newly added checksum

        charset = set([char.upper(),char.lower()])
        seen = {}
        present = True
        while(row < matrix.bits and present):
            tmp  = ['_']*(matrix.bits*2)
            last = None
            intra_row_transition = []

            # -- inter-row boundary check (|) ----------------------- #
            # exit outer loop when row not containing char found      #
            present = False                                           #
            for i, b in enumerate(matrix.template[row]):              #
                if b.upper() == char:                                 #
                    # -- intra-row boundary check ------------------------------------ #
                    # Detects reused chars within the same row: ch -> '_' -> ch        #
                    if last != char:                                                   #
                        intra_row_transition.append(i)                                 #
                    if len(set(intra_row_transition)) != 1:                            #
                        irt_err = intra_row_transition[1]-1                            #
                        raise SyntaxError(                                             #
                            f"Intra-row Error [column {irt_err}]. Invalid template."   #
                        )                                                              #
                    # ---------------------------------------------------------------- #
                    present = True                                    #
            # ------------------------------------------------------- #
                    tmp[i]  = char
                last = b.upper()

            unit[row] = tmp
            row += 1

        # -- fill remaining rows ------------------------------------
        while 0 < (matrix.bits-row):
            unit[row] = empty_row
            row += 1

        arithmetic_units.append(mp.Template(unit))

    # -- duplicate character check ----------------------------------
    # Detects duplicates by testing

    for i in arithmetic_units:
       print(i)

    unit_rows = [sum(i.checksum) for i in arithmetic_units]
    if sum(unit_rows) != sum(matrix.checksum):
        raise SyntaxError("Invalid template. Each unit must use unique char")

    return arithmetic_units


def horizontal_boundaries(matrix: list[list[Any]], *,
    transit: Callable[[Any], bool
    ]) -> list[tuple[int, int]]:
    """
    Returns a list of tuples representing the horizontal boundaries of the matrix.
    Each tuple contains the x and y coordinates of the boundary.

    Parameters:
    - matrix: The nested list to analyze.
    - transit: Boundary defined by a function:
        - isalpha
        - isint
        - ishex2
    """

    if not transit:
        raise ValueError("Transit function not provided")

    boundary = []
    width = len(matrix[0])
    for y, row in enumerate(matrix):
        x = 0

        while x < width and not transit(row[x]):
            print(transit(row[x]), row[x])
            x += 1
        boundary.append((x, y))
        while x < width and transit(row[x]):
            print(transit(row[x]), row[x])
            x += 1

        boundary.append((x-1, y))
        while x < width and not transit(row[x]):
            print(transit(row[x]), row[x])
            if transit(row[x]):
                raise ValueError(f"Binary value containing {row[x]} at position ({x}, {y})")
            x += 1
        print('end')

    return boundary

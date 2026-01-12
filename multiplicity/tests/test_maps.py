import multiplicity as mp




def main():

    m = mp.build_dadda_map(4)
    mp.mprint(m)
    sm = mp.Map(
        [
            '00',
            'FF',
            'FF',
            'FF',
        ]
    )
    mp.mprint(sm)
    m1 = mp.build_matrix(5, 5, 4)
    mp.mprint(m1)
    m1map = mp.resolve_rmap(m1)
    mp.mprint(m1map)




if __name__ == "__main__":
    main()

import multipy as mp




def main():

    m = mp.build_dadda_map(4)
    mp.mprint(m)
    sm = mp.Map(
        [
            '00',
            'FF',
            'FF',
            'FF',
        ], 4
    )
    mp.mprint(sm)




if __name__ == "__main__":
    main()

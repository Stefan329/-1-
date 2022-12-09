def gen(cor1, cor2, cor3):
    S1 = sum(cor1)
    A1 = sum(cor1) / len(cor1)
    S2 = sum(cor2)
    A2 = sum(cor2) / len(cor2)
    S3 = sum(cor3)
    A3 = sum(cor3) / len(cor3)
    return [(S1, S2, S3), (A1, A2, A3)]

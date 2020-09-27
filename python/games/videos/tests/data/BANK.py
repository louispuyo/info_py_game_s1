
# SPACE SHIP 1 DIM : (760, 706)
DIM = (760, 126)
# (from_x, from_y, to_x, to_y)

class SP_test:
    def __init__(self):
        self.SP_test_1 = (0, 0, 115, 120)
        self.SP_test_2 = (self.SP_test_1[2], self.SP_test_1[3], self.SP_test_1[2]+40, self.SP_test_1[3])
        self.SP_test_3 = (0, 115, self.SP_test_2[2]+100, self.SP_test_2[3])
        self.SP_test_4 = (self.SP_test_3[2], self.SP_test_3[3], self.SP_test_3[2]+40, self.SP_test_3[3])
        self.SP_test_5 = (self.SP_test_4[2], self.SP_test_4[3], self.SP_test_4[2]+40, self.SP_test_4[3])
        self.SP_test_6 = (self.SP_test_5[2], self.SP_test_5[3], self.SP_test_5[2]+40, self.SP_test_5[3])


# SP_test_4 = (SP_test_3[2], SP_test_3[3], SP_test_3[2], SP_test_3[3]+125)

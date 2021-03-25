import unittest
import problem as pb
import problem2 as pb2

class TestProblemMethods(unittest.TestCase):

    def test_simp_prt(self):
        input_lines = pb.decode("test_file.txt")
        result = pb.simp_prt(input_lines[0])
        result2 = pb.simp_prt(input_lines[1])

        self.assertEqual(result, 54)
        self.assertEqual(result2, 432)

    def test_simp_prt(self):
        input_lines = pb2.decode("test_file.txt")
        result = pb2.simp_prt(input_lines[0])
        result2 = pb2.simp_prt(input_lines[1])

        self.assertEqual(result, 54)
        self.assertEqual(result2, 1440) 

    def test_simp_add(self):
        input_lines = pb2.decode("test_file.txt")
        result = pb2.simp_add(input_lines[0])
        result2 = pb2.simp_add(input_lines[1])

        self.assertEqual(result, [6, '*', '9', ")"])
        self.assertEqual(result2, ['8', '*', 15, '*', "4", "*", "3", ")"])

import unittest
import problem as pb

class TestProblemMethods(unittest.TestCase):

    def test_rotation(self):
        photos = pb.decode("UT.txt")
        image1 = photos[0]
        dupl = copy.deepcopy(image1.edges)
        image1.rotate_clockwise()

        self.assertEqual(image1.edges[0], ['.', '#', '.', '.', '#', '#', '#', '#', '#', '.'])
        self.assertEqual(image1.edges[1], ['.', '.', '#', '#', '.', '#', '.', '.', '#', '.'])
        self.assertEqual(image1.edges[2], ['.', '.', '.', '#', '.', '#', '#', '.', '.', '#'])
        self.assertEqual(image1.edges[3], ['#', '#', '#', '.', '.', '#', '#', '#', '.', '.'])

        image1.rotate_clockwise()
        image1.rotate_clockwise()
        image1.rotate_clockwise()

        self.assertEqual(image1.edges[0], dupl[0])
        self.assertEqual(image1.edges[1], dupl[1])
        self.assertEqual(image1.edges[2], dupl[2])
        self.assertEqual(image1.edges[3], dupl[3])



    def test_flip(self):
        photos = pb.decode("UT.txt")
        image1 = photos[0]
        image1.flip()

        self.assertEqual(image1.edges[0], ['.', '.', '#', '#', '#', '.', '.', '#', '#', '#'])
        self.assertEqual(image1.edges[1], ['#', '.', '.', '#', '#', '.', '#', '.', '.', '.'])
        self.assertEqual(image1.edges[2], ['.', '#', '.', '.', '#', '.', '#', '#', '.', '.'])
        self.assertEqual(image1.edges[3], ['.', '#', '#', '#', '#', '#', '.', '.', '#', '.'])


#if __name__ == "__main__":
#    test_rotation()
#    test_flip()

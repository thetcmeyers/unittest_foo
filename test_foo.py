import unittest
import foo


class TestCase(unittest.TestCase):
    def test_cube1(self):
        self.assertEqual(foo.cube(4),64)
    #make sure te negative case fails since the volume cannot be negative
    def test_cube2(self):
        self.assertEqual(foo.cube(-4),None)
    #test floats, had to add round function
    def test_cube3(self):
        self.assertEqual(foo.cube(7.1),357.911)
    #make sure the string case fails (creates none)
    def test_cube4(self):
        self.assertEqual(foo.cube("Hi"),None)
    def test_average1(self):
        self.assertEqual(foo.average([1,2,3]),2)
    #make sure empty list fits
    def test_average2(self):
        self.assertEqual(foo.average([]),None)
    def test_average3(self):
        self.assertEqual(foo.average([1,4,10,7,8,9]),6.5)
    #try negative
    def test_average4(self):
        self.assertEqual(foo.average([-1,-2,-3,-7,-8,-9]),-5)
    #3 working sets
    def test_name1(self):
        self.assertEqual(foo.name("Tarren","Meyers"),"Tarren Meyers")
    def test_name2(self):
        self.assertEqual(foo.name("Rachel","McKinnon"),"Rachel McKinnon")
    def test_name3(self):
        self.assertEqual(foo.name("Mr.","Dude"),"Mr. Dude")
    ##fail condition, need strings
    def test_name4(self):
        self.assertEqual(foo.name(1,5),None)

if __name__ == "__main__":
    unittest.main(verbosity=2)

from django.test import TestCase
from .models import Courses, FlashCards

# Create your tests here.
class CoursesTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.tech = Courses.objects.create(course_name="Tech")

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.tech, Courses))

    # Testing Save Method
    def save_method_test(self):
        self.tech.save_Courses()
        coursess = Courses.objects.all()
        self.assertTrue(len(coursess) > 0)

class FlashCardTestClass(TestCase):
      # Set up method
    @classmethod
    def setUpTestData(cls):
        cls.flash1 = FlashCards.objects.create(flash_title="Flash1",flash_course='Tech', flash_body='Live in the moment.')

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.flash1, FlashCards))

    # Testing Save Method
    def save_method_test(self):
        self.flash1.save_FlashCards()
        FlashCardss = FlashCards.objects.all()
        self.assertTrue(len(FlashCardss) > 0)


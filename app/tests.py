from django.test import SimpleTestCase
from django.urls import reverse

# reverse takes in a string and turns it into a path

# Create your tests here.


class TestAddCanHandleSimpleAddition(SimpleTestCase):
    """
    0 + 0 = 0
    2 + 2 = 4
    2.3 + 1.2 = 3.5
    2 + -1 = 1
    -1 + 2 = 1
    -2 + -3 = -5
    """

    def test_two_plus_two(self):

        response = self.client.get(
            path=reverse('add'), data={
                'num1': '2',
                'num2': '2'
            })

        self.assertEqual(response.context['answer'], 4)

    def test_two_plus_negative_one(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '2',
                'num2': '-1'
            })

        self.assertEqual(response.context['answer'], 1)

    def test_zero_plus_zero(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '0',
                'num2': '0'
            })

        self.assertEqual(response.context['answer'], 0)

    def test_seven_plus_one(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '7',
                'num2': '1'
            })

        self.assertEqual(response.context['answer'], 8)

    def test_decimal(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '2.3',
                'num2': '1.2'
            })

        self.assertEqual(response.context['answer'], 3.5)

    def test_negative_one_plus_two(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '-1',
                'num2': '2'
            })

        self.assertEqual(response.context['answer'], 1)

    def test_negative_two_plus_negative_three(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '-2',
                'num2': '-3'
            })

        self.assertEqual(response.context['answer'], -5)


class TestAddWithoutNumbers(SimpleTestCase):
    """If add is not given two numbers it should present
    the user with the add.html template and not try to compute
    an answer."""

    def test_given_non_numeric_input(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': 'a',
                'num2': 'a'
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_one_numeric_input(self):
        response = self.client.get(path=reverse('add'), data={'num2': '3'})

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_no_input(self):
        response = self.client.get(path=reverse('add'), data={})

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_empty_input(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '',
                'num2': ''
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)


class TestDoubleCanDoubleRealNumber(SimpleTestCase):
    """If you GET double with an int or float, it should
    render double.html with double that number as 'answer'
    in the context."""

    def test_double_four(self):
        response = self.client.get(
            path=reverse('double'), data={'your_num': '4'})

        self.assertEqual(response.context['answer'], 8)

    def test_double_eight(self):
        response = self.client.get(
            path=reverse('double'), data={'your_num': '8'})

        self.assertEqual(response.context['answer'], 16)

    def test_double_zero(self):
        response = self.client.get(
            path=reverse('double'), data={'your_num': '0'})

        self.assertEqual(response.context['answer'], 0)

    def test_double_one(self):
        response = self.client.get(
            path=reverse('double'), data={'your_num': '1'})

        self.assertEqual(response.context['answer'], 2)

    def test_double_two_point_two(self):
        response = self.client.get(
            path=reverse('double'), data={'your_num': '2.2'})

        self.assertEqual(response.context['answer'], 4.4)

    def test_double_negative_four(self):
        response = self.client.get(
            path=reverse('double'), data={'your_num': '-4'})

        self.assertEqual(response.conext['answer'], -8)

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

        response = self.client.post(
            path=reverse('add'), data={
                'num1': '2',
                'num2': '2'
            })

        self.assertEqual(response.context['answer'], 4)

    def test_two_plus_negative_one(self):
        response = self.client.post(
            path=reverse('add'), data={
                'num1': '2',
                'num2': '-1'
            })

        self.assertEqual(response.context['answer'], 1)

    def test_zero_plus_zero(self):
        response = self.client.post(
            path=reverse('add'), data={
                'num1': '0',
                'num2': '0'
            })

        self.assertEqual(response.context['answer'], 0)

    def test_seven_plus_one(self):
        response = self.client.post(
            path=reverse('add'), data={
                'num1': '7',
                'num2': '1'
            })

        self.assertEqual(response.context['answer'], 8)

    def test_decimal(self):
        response = self.client.post(
            path=reverse('add'), data={
                'num1': '2.3',
                'num2': '1.2'
            })

        self.assertEqual(response.context['answer'], 3.5)

    def test_negative_one_plus_two(self):
        response = self.client.post(
            path=reverse('add'), data={
                'num1': '-1',
                'num2': '2'
            })

        self.assertEqual(response.context['answer'], 1)

    def test_negative_two_plus_negative_three(self):
        response = self.client.post(
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
        response = self.client.post(
            path=reverse('add'), data={
                'num1': 'a',
                'num2': 'a'
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_one_numeric_input(self):
        response = self.client.post(path=reverse('add'), data={'num2': '3'})

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_no_input(self):
        response = self.client.post(path=reverse('add'), data={})

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_empty_input(self):
        response = self.client.post(
            path=reverse('add'), data={
                'num1': '',
                'num2': ''
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)


class TestDoubleCanDoubleRealNumber(SimpleTestCase):
    """If you POST double with an int or float, it should
    render double.html with double that number as 'answer'
    in the context."""

    def test_double_four(self):
        response = self.client.post(
            path=reverse('double'), data={'your_num': '4'})

        self.assertEqual(response.context['answer'], 8)

    def test_double_eight(self):
        response = self.client.post(
            path=reverse('double'), data={'your_num': '8'})

        self.assertEqual(response.context['answer'], 16)

    def test_double_zero(self):
        response = self.client.post(
            path=reverse('double'), data={'your_num': '0'})

        self.assertEqual(response.context['answer'], 0)

    def test_double_one(self):
        response = self.client.post(
            path=reverse('double'), data={'your_num': '1'})

        self.assertEqual(response.context['answer'], 2)

    def test_double_two_point_two(self):
        response = self.client.post(
            path=reverse('double'), data={'your_num': '2.2'})

        self.assertEqual(response.context['answer'], 4.4)

    def test_double_negative_four(self):
        response = self.client.post(
            path=reverse('double'), data={'your_num': '-4'})

        self.assertEqual(response.context['answer'], -8)

    def test_number_none(self):
        response = self.client.post(path=reverse('double'), data={})

        self.assertTemplateUsed(response, 'app/double.html')
        self.assertNotIn('answer', response.context)

    def test_double_foo(self):
        response = self.client.post(
            path=reverse('double'), data={'your_num': 'foo'})

        self.assertTemplateUsed(response, 'app/double.html')
        self.assertNotIn('answer', response.context)


class TestMultipleCanMultiplyThreeNumbers(SimpleTestCase):
    """If you POST multiple with an int or float, it should 
    render multiple.html with the product of three numbers
    as 'answer' in the context."""

    def test_multiple_three(self):
        response = self.client.post(
            path=reverse('multiple'),
            data={
                'first_number': '3',
                'second_number': '3',
                'third_number': '3'
            })

        self.assertEqual(response.context['answer'], 27)

    def test_multiple_decimal(self):
        response = self.client.post(
            path=reverse('multiple'),
            data={
                'first_number': '27.8',
                'second_number': '33.4',
                'third_number': '62.0'
            })

        self.assertEqual(response.context['answer'], 57568.24)

    def test_multiple_negative(self):
        response = self.client.post(
            path=reverse('multiple'),
            data={
                'first_number': '-11',
                'second_number': '-2',
                'third_number': '-8'
            })

        self.assertEqual(response.context['answer'], -176.0)

    def test_multiply_foo(self):
        response = self.client.post(
            path=reverse('multiple'),
            data={
                'first_number': 'foo',
                'second_number': 'foo',
                'third_number': 'foo'
            })

        self.assertTemplateUsed(response, 'app/multiple.html')
        self.assertNotIn('answer', response.context)


class TestEarningsCanAdd(SimpleTestCase):
    """If you POST earnings with an int or float, it should
    render earnings.html with the three numbers of tickets 
    sold multiplied by the appropriate number and added 
    together.""" #1.15 2.12 3.9

    def test_low_earnings(self):
        response = self.client.post(
            path=reverse('earnings'),
            data={
                'first_number': '2',  #30
                'second_number': '1',  #12
                'third_number': '3'  #27
            })

        self.assertEqual(response.context['answer'], 69)

    def test_decimal_earnings(self):
        response = self.client.post(
            path=reverse('earnings'),
            data={
                'first_number': '2.2',  #33
                'second_number': '3.3',  #39.6
                'third_number': '4.4'  #39.6
            })

        self.assertEqual(response.context['answer'], 112.19999999999999)

    def test_string_earnings(self):
        response = self.client.post(
            path=reverse('earnings'),
            data={
                'first_number': 'me',
                'second_number': 'yes',
                'third_number': 'today'
            })

        self.assertTemplateUsed(response, 'app/earnings.html')
        self.assertNotIn('answer', response.context)


class TestTrueOrFalse(SimpleTestCase):
    """If you POST both with either True or False, it should
    render both.html with True or False. It should only return 
    True when both are True."""

    def test_true(self):
        response = self.client.post(
            path=reverse('both'),
            data={
                'first_answer': True,
                'second_answer': True
            })

        self.assertEqual(response.context['answer'], True)

    def test_false(self):
        response = self.client.post(
            path=reverse('both'),
            data={
                'first_answer': False,
                'second_answer': False
            })

        self.assertEqual(response.context['answer'], False)

    def test_second_false(self):
        response = self.client.post(
            path=reverse('both'),
            data={
                'first_answer': False,
                'second_answer': True
            })

        self.assertEqual(response.context['answer'], False)

    def test_false_true(self):
        response = self.client.post(
            path=reverse('both'),
            data={
                'first_answer': True,
                'second_answer': False
            })

        self.assertEqual(response.context['answer'], False)

    def test_both(self):
        response = self.client.post(
            path=reverse('both'),
            data={
                'first_answer': '-1',
                'second_answer': '-2'
            })

        self.assertNotEquals(response.context['answer'], False)


class TestWalkOrDrive(SimpleTestCase):
    """If you POST walkordrive with a number, it should
    render walkordrive.html with walk or drive depending
    on the distance."""

    def test_drive(self):
        response = self.client.post(
            path=reverse('walkordrive'), data={'miles': '2.2'})

        self.assertEqual(response.context['answer'], 'drive')

    def test_walk(self):
        response = self.client.post(
            path=reverse('walkordrive'), data={'miles': '0.22'})

        self.assertEqual(response.context['answer'], 'walk')

    def test_none(self):
        response = self.client.post(
            path=reverse('walkordrive'), data={'miles': '-2'})

        self.assertNotEquals(response.context['answer'], 'walk')


class TestHowPopulated(SimpleTestCase):
    """If you POST populated with a number, it should 
    render populated.html with densely populated or sparesly
    populated depending on the number."""

    def test_densely(self):
        response = self.client.post(
            path=reverse('populated'), data={'land_density': '200'})

        self.assertEqual(response.context['answer'], 'Densely Populated')

    def test_sparsely(self):
        response = self.client.post(
            path=reverse('populated'), data={'land_density': '50'})

        self.assertEqual(response.context['answer'], 'Sparsely Populated')


class TestScore(SimpleTestCase):
    """If you POST stars with a number, it should render stars.html with the 
    appropriate amount of stars needed shown."""

    def test_score_1000(self):
        response = self.client.post(
            path=reverse('stars'), data={'score': '50'})

        self.assertEqual(response.context['answer'], '*')

    def test_score_5000(self):
        response = self.client.post(
            path=reverse('stars'), data={'score': '4855'})

        self.assertEqual(response.context['answer'], '**')

    def test_score_8000(self):
        response = self.client.post(
            path=reverse('stars'), data={'score': '6777'})

        self.assertEqual(response.context['answer'], '***')

    def test_score_10000(self):
        response = self.client.post(
            path=reverse('stars'), data={'score': '9999'})

        self.assertEqual(response.context['answer'], '****')

    def test_score_over_10000(self):
        response = self.client.post(
            path=reverse('stars'), data={'score': '11000'})

        self.assertEqual(response.context['answer'], '*****')


class TestPoints(SimpleTestCase):
    """If you POST points with a type of score, it should render points.html
    with the appropriate amount of points needed."""

    def test_point_kick(self):
        response = self.client.post(
            path=reverse('points'), data={'what_score': 'extra point kick'})

        self.assertEqual(response.context['answer'], '1')

    def test_point_conversion(self):
        response = self.client.post(
            path=reverse('points'),
            data={'what_score': 'extra point conversion'})

        self.assertEqual(response.context['answer'], '2')

    def test_safety(self):
        response = self.client.post(
            path=reverse('points'), data={'what_score': 'safety'})

        self.assertEqual(response.context['answer'], '2')

    def test_field_goal(self):
        response = self.client.post(
            path=reverse('points'), data={'what_score': 'field goal'})

        self.assertEqual(response.context['answer'], '3')

    def test_touchdown(self):
        response = self.client.post(
            path=reverse('points'), data={'what_score': 'touchdown'})

        self.assertEqual(response.context['answer'], '7')

    def test_other(self):
        response = self.client.post(
            path=reverse('points'), data={'what_score': '7'})

        self.assertEqual(response.context['answer'], '0')

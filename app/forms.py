from django import forms


class AddForm(forms.Form):
    num1 = forms.FloatField(label='Number 1')
    num2 = forms.FloatField(label='Number 2')


class DoubleForm(forms.Form):
    your_num = forms.FloatField()


class MultipleForm(forms.Form):
    first_number = forms.FloatField()
    second_number = forms.FloatField()
    third_number = forms.FloatField()


class EarningsForm(forms.Form):
    first_number = forms.FloatField()
    second_number = forms.FloatField()
    third_number = forms.FloatField()


class BothForm(forms.Form):
    first_answer = forms.BooleanField(required=False)
    second_answer = forms.BooleanField(required=False)


class WalkOrDriveForm(forms.Form):
    miles = forms.FloatField()


class PopulatedForm(forms.Form):
    land_density = forms.FloatField()


class StarForm(forms.Form):
    score = forms.IntegerField()


class PointsForm(forms.Form):
    what_score = forms.CharField()

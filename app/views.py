from django.shortcuts import render
from django.views import View
from . import forms


class Add(View):
    def post(self, request):

        form = forms.AddForm(data=request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            answer = num1 + num2
            return render(request, 'app/add.html', {
                'answer': answer,
                'addForm': form
            })
        else:
            return render(request, 'app/add.html', {'addForm': form})

    def get(self, request):
        return render(request, 'app/add.html', {'addForm': forms.AddForm()})


class Double(View):
    def post(self, request):
        form = forms.DoubleForm(data=request.POST)
        if form.is_valid():
            your_num = form.cleaned_data['your_num']
            answer = your_num * 2
            return render(request, 'app/double.html', {
                'answer': answer,
                'doubleForm': form
            })
        else:
            return render(request, 'app/double.html', {'doubleForm': form})

    def get(self, request):
        return render(request, 'app/double.html',
                      {'doubleForm': forms.DoubleForm()})


class Multiple(View):
    def post(self, request):
        form = forms.MultipleForm(data=request.POST)
        if form.is_valid():
            first_number = form.cleaned_data['first_number']
            second_number = form.cleaned_data['second_number']
            third_number = form.cleaned_data['third_number']
            answer = first_number * second_number * third_number
            return render(request, 'app/multiple.html', {
                'answer': answer,
                'multipleForm': form
            })
        else:
            return render(request, 'app/multiple.html', {'multipleForm': form})

    def get(self, request):
        return render(request, 'app/multiple.html',
                      {'multipleForm': forms.MultipleForm()})


class Earnings(View):
    def post(self, request):

        form = forms.EarningsForm(data=request.POST)
        if form.is_valid():
            first_number = form.cleaned_data['first_number']
            second_number = form.cleaned_data['second_number']
            third_number = form.cleaned_data['third_number']
            first_earnings = first_number * 15
            second_earnings = second_number * 12
            third_earnings = third_number * 9
            answer = first_earnings + second_earnings + third_earnings
            return render(request, 'app/earnings.html', {
                'answer': answer,
                'earningsForm': form
            })
        else:
            return render(request, 'app/earnings.html', {'earningsForm': form})

    def get(self, request):
        return render(request, 'app/earnings.html',
                      {'earningsForm': forms.EarningsForm()})


class Both(View):
    def post(self, request):

        form = forms.BothForm(data=request.POST)
        if form.is_valid():
            first_answer = form.cleaned_data['first_answer']
            second_answer = form.cleaned_data['second_answer']
            return render(request, 'app/both.html', {
                'answer': first_answer and second_answer,
                'bothForm': form
            })
        else:
            return render(request, 'app/both.html', {'bothForm': form})

    def get(self, request):
        return render(request, 'app/both.html', {'bothForm': forms.BothForm()})


class walkOrDrive(View):
    def post(self, request):

        form = forms.WalkOrDriveForm(data=request.POST)
        if form.is_valid():
            miles = form.cleaned_data['miles']
            is_nice_weather = True
            if miles <= 0.25 and miles > 0 and is_nice_weather == True:
                return render(request, 'app/walkordrive.html', {
                    'answer': 'walk',
                    'walkordriveForm': form
                })
            else:
                return render(request, 'app/walkordrive.html', {
                    'answer': "drive",
                    'walkordrive': form
                })
        else:
            return render(request, 'app/walkordrive.html',
                          {'walkordriveForm': form})

    def get(self, request):
        return render(request, 'app/walkordrive.html',
                      {'walkordriveForm': forms.WalkOrDriveForm()})


class HowPopulated(View):
    def post(self, request):
        form = forms.PopulatedForm(data=request.POST)
        if form.is_valid():
            land_density = form.cleaned_data['land_density']
            if land_density > 100:
                return render(request, 'app/populated.html', {
                    'answer': 'Densely Populated',
                    'populatedForm': form
                })
            else:
                return render(request, 'app/populated.html', {
                    'answer': 'Sparsely Populated',
                    'populatedForm': form
                })
        else:
            return render(request, 'app/populated.html',
                          {'populatedForm': form})

    def get(self, request):
        return render(request, 'app/populated.html',
                      {'populatedForm': forms.PopulatedForm()})


class Stars(View):
    def post(self, request):
        form = forms.StarForm(data=request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            if score < 1000:
                return render(request, 'app/stars.html', {
                    'answer': '*',
                    'starForm': form
                })
            elif score < 5000:
                return render(request, 'app/stars.html', {
                    'answer': '**',
                    'starForm': form
                })
            elif score < 8000:
                return render(request, 'app/stars.html', {
                    'answer': '***',
                    'starForm': form
                })
            elif score < 10000:
                return render(request, 'app/stars.html', {
                    'answer': '****',
                    'starForm': form
                })
            elif score > 10000:
                return render(request, 'app/stars.html', {
                    'answer': '*****',
                    'starForm': form
                })
            # else:
            #     return render(request, 'app/stars.html', {'answer': '', 'starForm': form})
        else:
            return render(request, 'app/stars.html', {'starForm': form})

    def get(self, request):
        return render(request, 'app/stars.html',
                      {'starForm': forms.StarForm()})


class Points(View):
    def post(self, request):
        form = forms.PointsForm(data=request.POST)
        if form.is_valid():
            what_score = form.cleaned_data['what_score']
            if what_score.lower() == 'extra point kick':
                return render(request, 'app/points.html', {
                    'answer': '1',
                    'pointForm': form
                })
            elif what_score.lower(
            ) == 'extra point conversion' or what_score.lower() == 'safety':
                return render(request, 'app/points.html', {
                    'answer': '2',
                    'pointForm': form
                })
            elif what_score.lower() == 'field goal':
                return render(request, 'app/points.html', {
                    'answer': '3',
                    'pointForm': form
                })
            elif what_score.lower() == 'touchdown':
                return render(request, 'app/points.html', {
                    'answer': '7',
                    'pointForm': form
                })
            else:
                return render(request, 'app/points.html', {
                    'answer': '0',
                    'pointForm': form
                })
        else:
            return render(request, 'app/points.html', {'pointForm': form})

    def get(self, request):
        return render(request, 'app/points.html',
                      {'pointForm': forms.PointsForm()})

from django.shortcuts import render
from django.views import View


class Add(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1', default=""))
            num2 = float(request.GET.get('num2', default=""))
        except ValueError:
            return render(request, 'app/add.html')
        else:
            answer = num1 + num2
            return render(request, 'app/add.html', {'answer': answer})


class Double(View):
    def get(self, request):
        number = request.GET.get('your_num')

        if number is not None:
            try:
                your_num = float(number)
                answer = your_num * 2
                return render(request, 'app/double.html', {'answer': answer})
            except ValueError:
                return render(request, 'app/double.html')
        else:
            return render(request, 'app/double.html')


class Multiple(View):
    def get(self, request):
        # if first_number is not None and second_number is not None and third_number is not None:
        try:
            first = float(request.GET.get('first_number'))
            second = float(request.GET.get('second_number'))
            third = float(request.GET.get('third_number'))

        except:
            return render(request, 'app/multiple.html')

        else:
            answer = first * second * third
            return render(request, 'app/multiple.html', {'answer': answer})


class Earnings(View):
    def get(self, request):
        try:
            first_number = float(request.GET.get('first_number'))
            second_number = float(request.GET.get('second_number'))
            third_number = float(request.GET.get('third_number'))
        except:
            return render(request, 'app/earnings.html')

        else:
            first_earnings = first_number * 15
            second_earnings = second_number * 12
            third_earnings = third_number * 9
            total_earnings = first_earnings + second_earnings + third_earnings
            return render(request, 'app/earnings.html',
                          {'answer': total_earnings})


class Both(View):
    def get(self, request):
        first_answer = request.GET.get('first_answer')
        second_answer = request.GET.get('second_answer')
        if first_answer.lower() == 'true' and second_answer.lower() == "true":
            return render(request, 'app/both.html', {'answer': 'True'})
        elif first_answer.lower() == "false" and second_answer.lower(
        ) == "false":
            return render(request, 'app/both.html', {'answer': 'False'})
        elif first_answer.lower() == "false" and second_answer.lower(
        ) == "true":
            return render(request, 'app/both.html', {'answer': 'False'})
        elif first_answer.lower() == "true" and second_answer.lower(
        ) == "false":
            return render(request, 'app/both.html', {'answer': 'False'})
        else:
            return render(request, 'app/both.html')

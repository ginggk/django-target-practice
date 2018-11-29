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
        first_number = request.GET.get('one_number')
        second_number = request.GET.get('two_number')
        third_number = request.GET.get('three_number')

        if first_number is not None and second_number is not None and third_number is not None:
            first = float(first_number)
            second = float(second_number)
            third = float(third_number)
            answer = first * second * third
            return render(request, 'app/multiple.html', {'answer': answer})
        else:
            return render(request, 'app/multiple.html')

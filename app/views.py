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
        number = request.GET.get('your_number')

        if number is not None:
            your_num = float(number)
            answer = your_num * 2
            return render(request, 'app/double.html', {'answer': answer})
        else:
            return render(request, 'app/double.html')

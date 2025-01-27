from django.shortcuts import render
import requests


def index(request):
    converted_amount = None
    amount = None
    from_currency = None
    to_currency = None
    if request.method == 'POST':
        amount = request.POST.get('amount')
        from_currency = request.POST.get('from')
        to_currency = request.POST.get('to')
        if from_currency == to_currency:
            converted_amount = amount
        else:
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
            data = requests.get(url).json()
            converted_amount = data['rates'][to_currency]

    return render(request, 'index.html', {'to_amount': converted_amount, 'from_amount': amount, "to_currency": to_currency, "from_currency": from_currency})

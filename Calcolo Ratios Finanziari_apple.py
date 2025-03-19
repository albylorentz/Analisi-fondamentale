apple = {
    "name":"APPLE",
    "tk": "AAPL",
    "prezzo": 150.50,
    "eps": 6.15,
    "book_value": 25.80
}

apple["pe"] = apple["prezzo"] / apple["eps"]
apple["pb"] = apple["prezzo"] / apple["book_value"]

print(apple)  # Mostra tutti i dati!
'aggiungo un commento per verificare git'
''
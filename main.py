def add_surname(lst):
    return [x + " Kardashian" for x in lst if x[0].lower() == 'k']


# Testing
lst = ["Kiki", "Krystal", "Pavel", "Annie", "Koala"]
print(add_surname(lst))

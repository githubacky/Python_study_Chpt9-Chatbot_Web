from bottle import template

name = input("What's your name? ")
response = template('こんにちは{{name}} さん')
print(response)

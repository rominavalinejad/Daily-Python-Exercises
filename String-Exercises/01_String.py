# Srting Exercise 01
user_text = "my name is Romina"
user_text_expandtab = "Nmae\tFamily\tAge\tCity"
user_text_format = "Ma name is {}"
user_text_format_map = "my name is {name}; I'm from {country} and I love {lang}"
user_text_dic = {"name" : "Romina", "lang": "Python" , "country" : "Iran"}
user_text_isal = "mynameisRomina"
user_text_isal_secound = "@mynameisRomina"
user_text_isascii = "my name is Romina😊"
user_text_isdecimal = 23
user_text_isdecimal_secound = 6**2
print(user_text.capitalize())
print(user_text.casefold())
print(user_text.casefold().casefold())
print(user_text.center(20))
print(user_text.center(30, "*"))
print(user_text.count("m")) 
print(user_text.count("a"))
print(user_text.count("m",0,10))
print(user_text.encode())
print(user_text.encode().decode())
print(user_text.endswith("Romina"))
print(user_text.endswith("ROMINA"))
print(user_text.endswith("my"))
print(user_text.startswith("my"))
print(user_text.startswith("Romina"))
print("my" in user_text)
print("Romina" in user_text)
print("is" in user_text)
print("Valinejad" in user_text)
print(user_text_expandtab.expandtabs())
print(user_text_expandtab.expandtabs(40))
print(user_text.find("m"))
print(user_text.find("R"))
print(user_text.find("e"))
print(user_text.find("z"))
print(user_text.index("m"))
print(user_text.index("R"))
print(user_text.index("e"))
print(user_text.find("a",0,6))
print(user_text.index("R",0,12))
print(user_text_format.format("Romina Valinejad"))
print(user_text_format_map.format_map(user_text_dic))
print(user_text.isalnum())
print(user_text_isal.isalnum())
print(user_text_isal_secound.isalnum())
print(user_text.isalpha())
print(user_text_isal.isalpha())
print(user_text.isascii())
print(user_text_isascii.isascii())

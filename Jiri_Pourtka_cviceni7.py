# Vytvoř následující funkce:
#
# is_adult: Funkce ověří zda je uživatel dospělý
# is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
# create_user:
#   Funkce vytvoří slovník reprezentujícího uživatele.
#  Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
# Pokud je vše v pořádku, create_user vrátí následující slovník:
# {
# "success": True,
# "user": {"username": "...", "age": ..., "email": "..."}
# }
#  Pokud validace selže, create_user vrátí:
# {
# "success": False,
# "error": "Chybová zpráva..."
# }
#
#
# print_user_info: Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření
#
# Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.
#
# Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.

import pprint

def is_adult(age: int) -> bool:
    if age > 17:
        return True
    else: return False

def is_name_valid(name: str) -> bool:
    if len(name) > 3:
        return True
    else: return False

def print_user_info(list_of_users: list) -> None:
    pprint.pprint(list_of_users)

list_of_users = []

def create_user(age: int, name: str, email: str) -> dict or list:
    if is_adult(age) and is_name_valid(name):
        new_user = {
            "name": name,
            "age": age,
            "email": email
        }
        create_user_succsess = {
            "success": True,
            "new_user": new_user
        }
        list_of_users.append(new_user)
        return create_user_succsess
    else:
        create_user_failure = [{
            "success": False,
            "error": "Uživatelský věk nebo jméno nevyhovuje kritériím."
        }]
        print_user_info(create_user_failure)
        return create_user_failure

create_user(18,"Honza", "strejdahonza@seznamka.cz" )
create_user(17, "Tonda", "tondachstrechanacelyzivot@ttt.cz")
create_user(20, "DJ", "DJ@jedeeeem.cz")
create_user(100, "Děda", "jestenejsmestary@ne.cz")
create_user(19, "Maruska", "splnimtikazdeprani@maruska.hot")

print_user_info(list_of_users)
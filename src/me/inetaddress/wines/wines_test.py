'''
Created on 29 oct 2021

@author: alberto
'''
from me.inetaddress.wines import wines

def main():
    test_parse_file("../../../../data/wine_ratings.csv")
    
def print_test_header(test_name):
    print("\n\n--------------------------------------")
    print(test_name, "test")
    print("--------------------------------------")

# --------------------------------------
# ENTREGA 1
# --------------------------------------

def test_parse_file(path:str) -> None:
    print_test_header("parse_file")
    wine_list = wines.parse_file(path)
    print("Leídos", len(wine_list), "vinos")
    
    print("3 primeros vinos leídos:")
    for wine in wine_list[:3]:
        print(" -", wine)
        
    print("3 últimos vinos leídos:")
    for wine in wine_list[-3:]:
        print(" -", wine)



if __name__ == '__main__':
    main()
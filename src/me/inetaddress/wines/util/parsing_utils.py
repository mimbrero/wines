'''
Created on 29 oct 2021

@author: alberto
'''
from datetime import datetime, date

def parse_date(to_parse:str) -> date:
    '''
    Parsea una fecha dada en tipo str con formato dd/mm/aaaa.
    
    @param to_parse: fecha a parsear
    @return fecha parseada
    '''
    return datetime.strptime(to_parse, "%d/%m/%Y").date
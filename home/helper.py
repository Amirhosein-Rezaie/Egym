import random
import string
from datetime import datetime


class Helper:
    def genrate_trackcode(perfix: str = 'PREFIX', number_random_char: int = 8,char:str='-'):
        date_str = datetime.now().strftime('%Y%m%d%S')
        random_part = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=number_random_char))
        
        if (perfix != ''):
            perfix += char
        return f"{perfix}{random_part}{char}{date_str}"

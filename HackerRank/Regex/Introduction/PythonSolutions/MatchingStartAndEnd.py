Regex_Pattern = r"^\d{1}\w{4}.{1}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
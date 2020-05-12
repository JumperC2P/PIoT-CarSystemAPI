import hashlib
from datetime import datetime

# h = hashlib.new("sha256","12345678")
# print("Test")
# print(h.hexdigest())


datetime_str = '19/09/2018'

datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y')

print(type(datetime_object))
print(datetime_object)  # printed in default format
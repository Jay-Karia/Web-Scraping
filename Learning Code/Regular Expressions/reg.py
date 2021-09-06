import re

str = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiiin'''

# findall, search, split, sub, finditer

# pattern = re.compile(r'fass')
# pattern = re.compile(r'.adm')
# pattern = re.compile(r'^Tata')
# pattern = re.compile(r'iin$')
pattern = re.compile(r'ai*')

matches = pattern.finditer(str)

for match in matches:
    print(match)
    # print(str[485:489])
 lst = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
max(lst, key=lambda d:d['age'])
oldest = max(lst, key=lambda d:d['age'])
old_age = oldest['age']
print(old_age)
list(filter(lambda d:d['age'] == old_age, lst))
# best solution：
def find_senior(lst): 
    mage = max(a['age'] for a in lst)
    return [a for a in lst if a['age']==mage]
# boş dictionary
my_dict = {'x': 2}
# dictionary int anahtarlı
my_dict = {1: 'elma', 2: 'armut'}
# dictionary karışık
my_dict = {'ad': 'Ali', 1: [2, 4, 3]}
# dict() kullanarak
my_dict = dict({1:'elma', 2:'armut'})
# her bir öğeye çift olarak sahip olan diziden
my_dict = dict([(1,'elma'), (2,'armut')])
my_dict = {'ad':'Ali', 'yas': 261}

print(my_dict['ad'])
 
print(my_dict.get('soyad'))
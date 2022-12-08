from DadyaFood.models import *

wr = Worker(user=User.objects.create(
    email='altywa1998@gmail.com',
    password='nono34'),
    name='������� ������',
    position='�������� �����')

cl = Client(user=User.objects.create(
    email='nikname21@gmail.com',
    password='defender42'),
    name='��������� �������',
    card_number=4147565798789009)

cl.save()
wr.save()

F = Food.objects.create(name='������', start_price=200, type_of_cuisine='�������', calories=500)
F2 = Food.objects.create(name='���������', start_price=180, type_of_cuisine='�������', calories=350)
F3 = Food.objects.create(name='�����', start_price=450, type_of_cuisine='�������', calories=400)
F4 = Food.objects.create(name='����', start_price=600, type_of_cuisine='�����������', calories=500)
F5 = Food.objects.create(name='����', start_price=400, type_of_cuisine='��������', calories=450)



F.save()
F2.save()
F3.save()
F4.save()
F5.save()

D1 = Ingredient(name='���', extra_price=80, calories=150)
D2 = Ingredient(name='������', extra_price=100, calories=250)
D3 = Ingredient(name='��������', extra_price=80, calories=300)
D4 = Ingredient(name='�����', extra_price=50, calories=50)
D5 = Ingredient(name='���', extra_price=50, calories=70)
D6 = Ingredient(name='����', extra_price=120, calories=270)
D7 = Ingredient(name='���', extra_price=70, calories=100)
D8 = Ingredient(name='������', extra_price=100, calories=170)
D9 = Ingredient(name='������� ����', extra_price=50, calories=120)
#
# for fp in Ord.objects.all():
#     fp.save()

D1.save()
D2.save()
D3.save()
D4.save()
D5.save()
D6.save()
D7.save()
D8.save()
D9.save()

F.ingredient.set([D1, D4, D3, D5], through_defaults={'client': cl, 'worker': wr})
F2.ingredient.set([D2, D4], through_defaults={'client': cl, 'worker': wr})
F3.ingredient.set([D9, D4, D1, D8], through_defaults={'client': cl, 'worker': wr})
F4.ingredient.set([D7, D5, D1, D4, D8], through_defaults={'client': cl, 'worker': wr})
F5.ingredient.set([D7, D6, D9], through_defaults={'client': cl, 'worker': wr})


F.ingredient.all()
F2.ingredient.all()
F3.ingredient.all()
F4.ingredient.all()
F5.ingredient.all()


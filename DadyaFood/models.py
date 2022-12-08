from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='имя')
    card_number = models.IntegerField(verbose_name='номер карточки')

    class Meta:
        db_table = 'Client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='имя')
    position = models.CharField(max_length=30, verbose_name='должность')

    class Meta:
        db_table = 'Worker'
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=60, verbose_name='ингридиент')
    extra_price = models.IntegerField(verbose_name='надбавка')
    calories = models.IntegerField(verbose_name='кол-во каллорий')

    class Meta:
        db_table = 'Ingredient'
        verbose_name = 'ингридиент'
        verbose_name_plural = 'ингриденты'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20, verbose_name='наименование бдюда')
    start_price = models.IntegerField(verbose_name='цена')
    ingredient = models.ManyToManyField(Ingredient, related_name='mill', through='Order')
    type_of_cuisine = models.CharField(max_length=30, verbose_name='кухня')
    calories = models.IntegerField(verbose_name='кол-во каллорий')

    class Meta:
        db_table = 'Food'
        verbose_name = 'хавчик'
        verbose_name_plural = 'хавчикс'

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True, verbose_name='время заказа')
    vegetarian = models.BooleanField(default=False, verbose_name='Вегетарианская')
    food_status = models.CharField(max_length=20, verbose_name='тип блюда', null=True)
    final_price = models.IntegerField(verbose_name='цена', null=True)

    class Meta:
        db_table = 'Order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return self.food.name


class Ord(Order):
    class Meta:
        proxy = True

    def vegetarian(self):
        ingredients = []
        for ing in self.food.all():
            ingredients.append(ing.name)
        for i in ['курица', 'говядина', 'рыба', 'куриные яйца']:
            if i in ingredients:
                return False
            else:
                return True

    def food_status(self):
        ingredient_calories = 0
        for cal in self.ingredient.all():
            ingredient_calories += cal.calories

        cl = self.calories + ingredient_calories
        if cl >= 700:
            self.food_status = 'перекус'
        if cl <= 1200:
            self.food_status = 'обед'
        if cl > 1200:
            self.food_status = 'обжираловка'


    # def final_price(self):
    #    return Food.start_price + Ingredient.extra_price
    #
    # def order_date_time(self):
    #
    #     self.order_date_time.strftime('%Y-%m-%Y %H:%M:%S:%f')


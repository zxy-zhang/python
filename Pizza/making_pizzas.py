import pizza
pizza.make_pizza(12,'pepperoni')
pizza.make_pizza(16,'mushrooms','green peppers','extra cheese')


#导入特定的函数
from pizza import make_pizza
make_pizza(12,'pepperoni')
make_pizza(16,'mushrooms','green peppers','extra cheese')


#使用as给模块指定别名
import pizza as p
p.make_pizza(12,'pepperoni')
p.make_pizza(16,'mushrooms','green peppers','extra cheese')

#导入模块中的所有函数
from pizza import*
make_pizza(12,'pepperoni')
make_pizza(16,'mushrooms','green peppers','extra cheese')

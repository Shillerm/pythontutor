# В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же
# время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть не
# больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт
# чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом
# из трех классов.

learnerOne = int(input())
learnerTwo = int(input())
learnerThee = int(input())

desk = ((learnerOne) // 2) + ((learnerOne) % 2) + ((learnerTwo) // 2) + ((learnerTwo) % 2) + ((learnerThee) // 2) + (
            (learnerThee) % 2)
print(desk)

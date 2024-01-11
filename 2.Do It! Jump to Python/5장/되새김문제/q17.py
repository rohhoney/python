import random
import itertools
people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
tasks = ['청소', '빨래', '설거지']

random_order_people = random.sample(people, 5)
print(list(itertools.zip_longest(random_order_people, tasks, fillvalue='휴식')))
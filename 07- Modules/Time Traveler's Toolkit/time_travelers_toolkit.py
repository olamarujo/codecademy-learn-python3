# importing
import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

# date setting
current_day = dt.date.today()
current_time = dt.datetime.now().time()

#randomizing date
random_year = randint(1,2024)
random_month = randint(1,12)
if random_month == 2:
  random_day = randint(1,28)
elif random_year % 4 == 0 and random_month == 2:
  random_day = randint(1,29)
elif random_month in [1, 3, 5, 7, 8, 10,12]:
  random_day = randint(1,31)
else:
  random_day = randint(1,30)
date = dt.date(random_year, random_month, random_day)

#base cost and cost multiplier
base_cost = Decimal("1000.00")
cost_multiplier = abs(current_day.year - random_year) * Decimal('0.01')

#calculation
diff_days = abs((current_day - date).days)
cost = base_cost * cost_multiplier * diff_days
cost = cost.quantize(Decimal('0.01'))

#destinations
possible_destinations = ["Great Wall of China", "Colosseum", "Stonehenge", "Angkor Wat", "Machu Picchu", "Chinchén Itzá", "Taj Mahal", "Giza Necropolis", "Petra"]
destination = choice(possible_destinations)

print(current_day)
print(date)
print(diff_days)
print(generate_time_travel_message(date, destination, cost))
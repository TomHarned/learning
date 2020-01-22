import pygal
from die import Die

# Create three D6's
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and store results in a lit.
results = []
for roll_num in range(10**5):
    result = die_1.roll() * die_2.roll() * die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result  = die_1.num_sides * die_2.num_sides * die_3.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 100,000 times."
hist.x_labels = [x for x in range(1, max_result + 1)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6 * D6', frequencies)
hist.render_to_file('die_visual.svg')

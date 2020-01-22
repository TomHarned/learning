import json
import pygal
from pygal.style import RotateStyle

from country_codes import get_country_code

# Load the data into a list.
filename = 'population_data.json'
with open(filename, 'r') as f:
    pop_data = json.load(f)
# Build a dictionary of population data
cc_pop = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_pop[code] = population

# Group the countries into 3 population levels
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_pop.items():
    if pop < 10**7:
        cc_pops1[cc] = pop
    elif pop < 10**9:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

# See how many countries are in each level
print(len(cc_pops1), len(cc_pops2), len(cc_pops3))

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)

wm.render_to_file('world_pop.svg')

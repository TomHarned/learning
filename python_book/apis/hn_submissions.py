import requests
import pygal
from operator import itemgetter


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: ", r.status_code)

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
plot_dicts = []
names = []
for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +\
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
            'title' : response_dict['title'],
            'link' : 'http://news.ycombinator.com/item?id=' +\
                      str(submission_id),
            'comments' :  response_dict.get('descendants', 0)
            }
    submission_dicts.append(submission_dict)

    plot_dict = {
            'value': submission_dict['comments'],
            'label': submission_dict['title'],
            'xlink': submission_dict['link']
            }
    plot_dicts.append(plot_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),\
                          reverse=True)

plot_dicts = sorted(plot_dicts, key=itemgetter('value'),\
                          reverse=True)

names = [x['label'] for x in plot_dicts]

chart = pygal.Bar()
chart.title = 'Most-Commented Submissions on Hacker News'
chart.x_labels = names
chart.x_label_rotation =45

chart.add('', plot_dicts)
chart.render_to_file('hn_plot.svg')

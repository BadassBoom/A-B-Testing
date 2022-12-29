import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
utm_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
    columns = 'is_click',
    index = 'utm_source', 
    values = 'user_id'
)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
salam = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
haram = ad_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index()
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
aclicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
aclicks_pivoted = aclicks.pivot(
    columns = 'is_click',
    index = 'day',
    values = 'user_id'
)
aclicks_pivoted['percent_clicked'] = aclicks_pivoted[True] / (aclicks_pivoted[False] + aclicks_pivoted[True])
bclicks = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
bclicks_pivoted = bclicks.pivot(
    columns = 'is_click',
    index = 'day',
    values = 'user_id'
)
bclicks_pivoted['percent_clicked'] = bclicks_pivoted[True] / (bclicks_pivoted[False] + bclicks_pivoted[True])
print(aclicks_pivoted)
print(bclicks_pivoted)

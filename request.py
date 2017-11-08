import requests
import random
import json
import html

URL = 'http://ads.appia.com/getAdsDebug?id=3855&password=OCD8KOQI8F4MPUPXDXDE0V4EZF&key=r3c@che4t0mc@t&userAgentHeader=Android&siteId=9814'

rand_num = random.randint(1,10000000000000000000)

PARAMS = {'sessionId':rand_num}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

# print(rand_num)

filtered_data = data['filteredCampaigns']

for x in filtered_data:
    if x['failedFilters'][0]['filterName'] == 'CampaignCreativeFilter':
        print(x['failedFilters'][0])


t = HTML.Table(header_row=['CampaignId', 'CampaignName', 'Reason/message'])

for x in filtered_data:
    t.rows.append([x['campaignId'], x['campaignname'], x['failedFilters'][0]['message']])

htmlcode = str(t)

print(htmlcode)

# SELECT sites.site_id, products.product_id
# FROM sites, products
# WHERE (sites.site_id = 10 OR sites.site_id = 12) AND (products.product_id != 31 OR  products.product_id != 33);
#
# SELECT sites.site_id, products.product_id
# FROM sites, products
# WHERE (sites.site_id != 10 OR sites.site_id != 12) AND (products.product_id = 31 OR  products.product_id = 33);

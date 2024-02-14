# kawalpemilu-api

Minimal Python script to scrape data from KawalPemilu.org and serve the api using Flask (Initially will be used to feed data to my [visualisation](https://github.com/hariesramdhani/kawalpemilu-visualized))

Sample (`data/provinces_data.json`)
```json
{"data": {"ACEH": {"paslon_1_ratio": 80.23, "paslon_1_count": 4962, "paslon_2_ratio": 18.17, "paslon_2_count": 1124, "paslon_3_ratio": 1.6, "paslon_3_count": 99, "cakupan_ratio": 0.22, "cakupan_count": "36/16,046", "cakupan_jaga_ratio": 13.86, "cakupan_jaga_count": "2,224/16,046"}, "BALI": {"paslon_1_ratio": 6.65, "paslon_1_count": 5086, "paslon_2_ratio": 55.44, "paslon_2_count": 42372, "paslon_3_ratio": 37.91, "paslon_3_count": 28975, "cakupan_ratio": 2.8, "cakupan_count": "359/12,809", "cakupan_jaga_ratio": 6.59, "cakupan_jaga_count": "844/12,809"}, "BANTEN": {"paslon_1_ratio": 37.88, "paslon_1_count": 35676, "paslon_2_ratio": 47.17, "paslon_2_count": 44424, "paslon_3_ratio": 14.94, "paslon_3_count": 14074, "cakupan_ratio": 1.25...
```

Access it from `http://157.230.44.40/kawalpemilu` Data updates every 10 minutes

### Todos
- [ ] Make the API public
- [ ] Scrape city/regency level data
- [ ] Save and load data directly to/from Postgre instead of saving it to JSON

All credit for the data belongs to the KawalPemilu team!
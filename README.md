# ShoeStore Ad Campaign Analysis

This code analyzes the effectiveness of an ad campaign for ShoeStore using data from **'ad_clicks.csv'**. The analysis includes information about the source of clicks, the percentage of clicks, and the number of clicks for each experimental group (A and B) by day of the week.

## Data

* **'user_id'**: unique identifier for each user
* **'utm_source'**: advertising source (google, facebook, twitter, etc.)
* **'day'**: day of the week the ad was clicked (Monday, Tuesday, etc.)
* **'ad_click_timestamp'**: timestamp of the ad click
* **'experimental_group'**: indicates whether the user was shown ad A or ad B

## Code

The code reads in the **'ad_clicks.csv'** file and groups the data by **'utm_source'**, **'is_click'** (whether or not the ad was clicked), and **'experimental_group'**. It then calculates the number and percentage of clicks for each **'utm_source'** and **'experimental_group'**, and the number and percentage of clicks by day of the week for each experimental group.

The resulting output shows the number of clicks and the percentage of clicks for each day of the week, separated by experimental group. The output can help to determine which ad campaign was more effective (A or B) and which day of the week had the highest click-through rate.

## Example Output

```
   is_click      day  user_id  percent_clicked
0     False   Friday      271         0.422924
1      True   Friday      367         0.577076
2     False   Monday      267         0.428571
3      True   Monday      357         0.571429
4     False   Sunday      307         0.473846
5      True   Sunday      339         0.526154
6     False  Thursday      252         0.402857
7      True  Thursday      373         0.597143
8     False  Tuesday      269         0.438491
9      True  Tuesday      344         0.561509
10    False   Monday      148         0.429658
11     True   Monday      198         0.570342
12    False  Tuesday      158         0.423313
13     True  Tuesday      214         0.576687
14    False   Friday      141         0.408759
15     True   Friday      200         0.591241
16    False  Thursday      155         0.432584
17     True  Thursday      203         0.567416
18    False   Sunday      143         0.416088
19     True   Sunday      201         0.583912

```

# A-B-Testing-for-ShoeStore

## Description
ShoeStore is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. I'll help them analyze the data using aggregate measures.

 ## Analyzing Ad Sources
- I wanted to know the percent of people who clicked on ads from each utm_source.

-  I've started by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups and I saved my answer to the variable clicks_by_source.

-  A new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

-  Was there a difference in click rates for each source?
## Analyzing an A/B Test
-  The column experimental_group tells us whether the user was shown Ad A or Ad B.

- Were approximately the same number of people shown both ads?

-  Using the column is_click that I defined earlier, I checked if a greater percentage of users clicked on Ad A or Ad B.

- The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

- a_clicks and b_clicksccontain only the results for A group and B group, respectively.

- For each group (a_clicks and b_clicks) I calculated the percent of users who clicked on the ad by day.


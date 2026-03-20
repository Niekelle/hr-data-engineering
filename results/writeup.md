1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

Phase 2 appears to represent the most active period, with the rolling average sustaining peaks of around 95 bpm, pushing into the target 50 - 85% heartrate zone of 95 to 162 bpm. Phase 2 also has the largest range of all the files with 63 bpm which usually points to an active workout where the particiapnt pushes hard and then recovers.

2) Which file had the **poorest** data quality? How do you know?

Phase 0 had the poorest data quality, having the highest number of invalid entries (3).

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
T
he range of this dataset is 180 - 68 = 112.


b) Explain how the extreme value affects the range.

The extreme value causes the range to skyrocket, from what may have been a range closer to 7 (given the similarity of all the outher measurements) all the way to 112. This extreme shift, due to the fact that the range only uses the absolute highest and lowest values, largely misrespresents the person's true physical state.

c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

The interquartile range would better represent the typical variability for the dataset. Since the IQR measures the spread of the middle 50% of data and ignores the highest and lowest 25% of numbers, it filters out large outliers and gives a truer picture.
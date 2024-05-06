''' Toulouse Business School MSc AIBA

Course: Python for Data Science -- PROJECT
Author: Evan Brahma Hughie Azhabur
Version: v1.0
'''

"""
PROJECT INSTRUCTIONS
---
Your project shoud :
- import at least one of the following packages:
    - matplotlib
    - pandas
- load the dataset into a pandas DataFrame
- have at least one variable defined and printed
- print a filtered dataframe with a comparison operator
- print a filtered dataframe with a boolean operator
- have a for-loop to create a new column to the DataFrame
- display a plot:
    - either a line-plot, a scatter-plot, or a histogram-plot
    - with x-axis and y-axis labels
    - with a title
- have some comments
"""
# Import the packages
import pandas as pd 
import matplotlib.pyplot as plt 

def main():
    print("Starting the project...")

    # Load the Trending YT dataset into Pandas DataFrame
    trendingyt = pd.read_csv('D:/Local Disk D/TBS/Semester 1/Module 3 Programming/3.2. Python for Data Science - Samia Drappeau/Project/Micro-dosing study_first harvest1.csv')
      
    # Variable defined is The number of videos in the dataset : video_count, and print video count
    video_count = len(trendingyt) #len for length which is the quantity of data
    print(f"Total number of videos in the dataset: {video_count}")
    
    # Column defines for comparison operator is durationSec, for value over 600  (10 minutes) it's considered long time
    Long_duration = trendingyt[trendingyt['durationSec']> 600]
    print(Long_duration)
    
    # Column defines for boolean operator is durationSec, for view count over 1000 second it's considered High
    high_view_count_videos = trendingyt['viewCount'] > 1000
    print("Videos with a view count higher than 1000:")
    print(high_view_count_videos)
    
    # For-Loop New Column, calculating the like-to-dislike ratio for each video       
    # There is some zero value in like Count and dislike Count, so it is needed to be define it first
    for ind, row in trendingyt.iterrows():
        like_count = row['likeCount']
        dislike_count = row['dislikeCount']
        
    # Use the calculation only if the value is not 0
        if like_count != 0 and dislike_count != 0:
            trendingyt.loc[ind, "Like-to-Dislike Ratio"] = like_count / dislike_count
        else:
            trendingyt.loc[ind, "Like-to-Dislike Ratio"] = 0  # Set ratio to 0 to handle the division by zero case
    print(trendingyt.head) #this print is for checking 
    
    #Displaying a Scatter plot of Like Count vs Dislike Count
    plt.figure(figsize=(10, 6))
    plt.scatter(trendingyt['likeCount'], trendingyt['dislikeCount'])
    plt.xlabel('Like Count')
    plt.ylabel('Dislike Count')
    plt.title('Scatter Plot of Like Count vs Dislike Count')
    plt.grid(True)
    plt.show()
    #The Result of the scatter plot is stacked in one part and a lot of outliers, 
    #this happens because there is some data (3 data in the plot) that has significantly large value    
    
    print("... project ended.")

if __name__ == '__main__':
    main()
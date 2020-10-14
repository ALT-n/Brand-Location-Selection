Successful location selection helps business:
1.	To understand which area is appropriate for future business development 
2.	To run a new business/new branch in an area in needs of your type of products/services
3.	To avoid financial losses and waste time in unfriendly environment 

My goal was to pick the best location if a client considers 3 options and ask me to determine which one is the best and why. 

Firstly, I had to scrape data from a database including all brands throughout Canada.

Secondly, in order to understand what location is appropriate for a brand, I wanted to have a model showing information about a potential location. For instance, if I put a postal code of a potential location, I want to see population in that area and number of competitors in radius 2, 5, or 10 kilometers. 

I have done this project via several steps:

• Created a web scraper using BeautifulSoup and Requests Libraries to grab data over 1,000 brands throughout North America. 
• Received geolocation for each store from scraped data using GeoPy and cleaned dataset. 
• Built a generic tool, which allows calculating the distance between the potential location and any competitor in 10 kilometers radius and shows the best potential location. 
• Mapping the result to visualize options for better making decisions. 







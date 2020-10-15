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

For instance, IKEA wants to open up a new store in Canada and considers 3 cities:  Sudbury (P3C5G3), North Bay (P1B4Y8), and Barrie(L4M3C1). Where is the best location?

I used my code to map competitors in 10 kilometers radius in blue color and potential location of IKEA in red color in each three potential locations. I also printed the number of competitors and population in the area. And the result is the output with a map that anyone can review and understand.

![pic1](https://user-images.githubusercontent.com/69282278/96058146-8bc84180-0e58-11eb-9373-83552a87fb06.jpg)
![pic2](https://user-images.githubusercontent.com/69282278/96058179-997dc700-0e58-11eb-8d7f-f255e5af0671.jpg)

Now I am able to make a decision. If we look at those 3 potential locations, more likely we pick up the location in Sudbury, where the population is the largest and number of competitors is smaller than in Barry. We would not consider North Bay at all, because there are plenty of furniture stores in the are for such a small number of people. 

I believe it the powerful tool and it definitely gives insights to decision makers. 





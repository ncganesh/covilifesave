# CoviLifeSave - AI for Social Good  Search Offer Help  Save Lives.


**PROBLEM**

India is currently in the midst of an unprecedented public health emergency with sudden spike in new COVID-19 cases and 
people are dying due to the acute shortage of **hospital beds,oxygen cylinders,Remedesvier Injection** throughout the country.
So there are million of tweets posted related to Requests,Medical help,Medical products on twitter.


![image](https://user-images.githubusercontent.com/24853196/120939523-75703e00-c6e6-11eb-92d7-9abb8968dae5.png)



**SOLUTION**
The main goal of this project is to build a system that will help the Emergency Management System/People Offering  to get related specific tweets that will save lives.
CoviLifeSaver helps the Emergency management system /  to identify specific tweets(request,offer etc) and take actions that will save lives.
Tweets are categorized into : 
Request - people requesting for Help on Twitter 
Offer - people Offering  Help on Twitter 
Medical Help - Tweets related to medical help

If a user is interested to offer help,They can filter by  requests and further filter by location and help.

Also,There are different kind of new medical help changing over time . As pandemic progressed, there was new requirements like Injections,blood plasma etc. So, we developed a Semantic Search so that users can get related tweets based on User's Query.

The proposed system has 3 platforms:
> Twitter Intents/Insights : network graphs 
 > (2) Provide/Offer Help (Automated Tweet Classification): Automated classification component classifies each tweet to 35 crisis related categories. The categories include but not limited to request, offer, medical help, medical products, and transport. This categorization is made possible by learning a model using machine learning algorithms on the text of the tweet. 
    
  > (3) Semantic Search - Semantic search provides the user the control to search for relevant tweets by querying the Twitter stream through textual input. In addition to these two components, we also provide the user the ability to see and filter by the origin location of tweets. Through this semantic search we will also be able to narrow down scams and spam tweets.


Steps to execute :

CVD Analytics
Install python requirements using pip :
pip install -r requirements.txt

python main.py

API  will be available at - http://127.0.0.1:5000/

CVD UI:
Run ng serve for a dev server. Navigate to http://localhost:4200/. The app will automatically reload if you change any of the source files.

Future Work:

Work on scaling the application  using Apache Kafka and Apache Spark to 

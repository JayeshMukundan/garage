This is a work in progress. Nothing concrete yet, just a trail of thoughts...

How graph databases could help online groceries help with better search responses?

Today, many online shopping systems by either solr or elasticsearch, the two stalwarts in the field of text search. Both
technologies, based on Lucene, offer solutions that help to quickly find the items based on the user's search query.
For example, when you search for “fruits”, there is not much time to figure out which among the millions of items are “fruits”.
So they support indexing (much like the one you see in books) such that the application knows exactly which items to return. 

Now, what else do we need here? User asks for something and we quickly find it. The challenge here is how do we keep with what
users can ask for. Today, they ask for “fruits”. What if they change the search to “vitamin a rich fruits”? I tried this search
query in one of the popular grocery giants and it listed all the vitamin supplements and no fruits. In machine learning 
parlance, we have built a high variance system. We have built a model that is too much tied to the training set such that we 
get excellent results when the test set (user query) matches very very closely with the training set. The moment a user starts 
to search for a new input that isn’t indexed properly by the application, we start seeing behaviors that are not inline with 
the user's expectations. 

How can we modify the search system to satisfy the user's request without moving to a new system? 
We could attach vitamin information to the index, translate the response that maps the “rich” in the user's query to an 
appropriate filter on the vitamin information and render relevant results. Pretty straightforward… 

Now, lets say if we want to query “vitamin balanced fruits”? What should it search for? Vitamin A or come up with a list of 
combinations of fruits such that they form a proper balanced diet that folks can put in a subscription for recurring delivery? 
How is the text search system going to help? It is very likely that we can come up with a solution, but the problem is that 
the solutions are very reactive. They don’t capture the relationships between items upfront. We need a model that captures the 
relationships and connections. Unlike clothes, toys, office items etc, groceries have connections with each other that are more
personal. We could provide more personal feedback to users on their shopping. For example, we could say that “Hey John, based 
on your shopping history, you tend to focus more on Vitamin-A fruits. Do you know that Oranges are great for your immunity?
Here are some recommendations….”.  Unless we capture the relationships and their connections proactively, it is very hard to 
address growing demands from the users and the more reactive the grocery systems are, more likely they go out of business. 
So how do we capture the relationships proactively? Graph databases...

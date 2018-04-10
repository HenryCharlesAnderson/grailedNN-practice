# grailedNN-practice

This is a personal project.

Using neural networks to determine if an item is worth purchasing. 

TODO:  
•Create a script that scrapes data off of the site. Starting with the base details (designer, category, price, size, number of likes, number of comments). One thing to keep in mind is that the scraping will be a lot faster if I limit myself to data that can be seen on the home page.  
--  Eventually it might be interesting to attempt to glean potential input data from the item descriptions. The obvious way to do that would be to look for a limited set of known indicators (x/10, "warning!", etc). But if I ever want to get some practice with NLP, this would be a good place to start.   
--  The other obvious future extension is to take the images as input. It would be very data heavy though. I'd either need to get more local HD space, scrape the input in a stream as the NN is trained (slooooow I imagine), only get to this step if/when I'm running this project on a server, or only take a small sample of each image. That last option would provide an interesting compression challenge.


•Write the NN! I can start with using the NN's in the book, but the whole point of this is to learn, and there's no better way for me to learn how it really works, than to struggle through the process of making it myself. I'd like to upload the book code here, but don't want anyone thinking it's mine. Hmm  
--  what type of NN is best suited to this particular problem  
--  how can I set up the network to maximize it's effectiveness. Should I just have one output node for buy/don't buy? should I try to output an estimated value and compare that value to the value the item actually sold for (limiting my testing+training batch to the sold items). Each of the input dimensions have some effect on the sellPrice, if the designer and category are very coveted that drives up the price, but if the size is rare that drives it down. It might be useful to combine those two results only after they have been calculated, mimicking the human decision process. Worth thinking about anyway, even if it turns out that that is violating the entire point of a NN or something. In general, useful to remember that it's humans who are deciding the market price of these items.

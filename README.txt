Hi,

This is jsut a little fun project I decided to do because my mom wanted a way to download a 32 page study guide from StuDocu but didn't know how, and I realized that was because you had to pay for the premium membership in order to download the pdf file.
However, I didn't want my mom paying for that and I also realized that the way the site was hostin the document was easily susceptible to web scraper when I looked at its html code.
That's when I deceide to create my own web scrapping bot the scrape the entire 32 page pdf on the website and store all that information into a word document.

I later did some data cleaning and formating of the word document for readability, which I then converted the word doc to a pdf

I have attached the source for my work along with the jupyter notebook incase anyone would like to test my code.

Note: I ran into so trouble trying to access the vaules in <div id="pf15"...> and onwards
so I have two separate loops that scrapes the pdf document from different number of pages:

    one loop scrapes the first 20 pages and another loop that scrapes the last 12 pages
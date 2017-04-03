"""Create a BlogPost class that has an authorName, a title, a text and a publicationDate
Create a few blog post objects:
"Lorem Ipsum" titled by John Doe posted at "2000.05.04."
Lorem ipsum dolor sit amet.
"Wait but why" titled by Tim Urban posted at "2010.10.10."
A popular long-form, stick-figure-illustrated blog about almost everything.
"One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention.
When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t
really into the whole organizer profile thing."""

class BlogPost():
    authorName = ""
    title = ""
    text = ""
    publicationDate = ""

post1 = BlogPost()
post2 = BlogPost()
post3 = BlogPost()

post1.authorName = "John Doe"
post2.authorName = "Tim Urban"
post3.authorName = "William Turton"
post1.title = "'Lorem Ipsum'"
post2.title = "'Wait but why'"
post3.title = "'One Engineer Is Trying to Get IBM to Reckon With Trump'"
post1.publicationDate = "'2000.05.04.'"
post2.publicationDate = "'2010.10.10.'"
post3.publicationDate = "'2017.03.28.'"
post1.text = "Lorem ipsum dolor sit amet."
post2.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
post3.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn't want to be the center of attention. When I asked to take his picture outside one of IBM's New York City offices, he told me that he wasnt really into the whole organizer profile thing."

print(post1.title + " titled by " + post1.authorName + " posted at " + post1.publicationDate + "\n" + post1.text)
print(post2.title + " titled by " + post2.authorName + " posted at " + post2.publicationDate + "\n" + post2.text)
print(post3.title + " titled by " + post3.authorName + " posted at " + post3.publicationDate + "\n" + post3.text)

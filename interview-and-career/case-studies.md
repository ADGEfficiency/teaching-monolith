## Airbnb's first data scientist

https://venturebeat.com/2015/06/30/how-we-scaled-data-science-to-all-sides-of-airbnb-over-5-years-of-hypergrowth/

The foundation on which a data science team rests is the culture and perception of data elsewhere in the organization. So defining how we think about data has been a prerequisite to ingraining data science in business functions.

While answering questions and measuring things is certainly part of the job, at Airbnb we characterize data in a more human light: it’s the voice of our customers. A datum is a record of an action or event, which in most cases reflects a decision made by a person. If you can recreate the sequence of events leading up to that decision, you can learn from it; it’s an indirect way of the person telling you what they like and don’t like — this property is more attractive than that one, I find these features useful but those — not so much.

This sort of feedback can be a goldmine for decisions about community growth, product development, and resource prioritization. But only if you can decipher it. Thus, data science is an act of interpretation — we translate the customer’s “voice” into a language more suitable for decision-making.

We use statistics to understand individual experiences and aggregate those experiences to identify trends across the community; those trends inform decisions about where to drive the business.

A lot has been written about the pros and cons of centralized and embedded data science teams, so I won’t focus on that. But suffice to say we’ve landed on a hybrid of the two.

Five years ago, I joined Airbnb as its first data scientist.At that


 time, the few people who’d even heard of the company were still figuring out how to pronounce its name, and the roughly seven-person team (depending on whether you counted that guy on the couch, the intern, and the barista at our favorite coffee shop) was still operating out of the founders’ apartment in SoMA. Put simply, it was pretty early-stage.Recommended videosPowered by AnyClipChina's U.


S. Oil Tariffs Spark Fear of a Global Demand SlowdownPlay VideoNOW PL

AYINGChina's U.S. Oil Tariffs Spark Fear of a Global Demand SlowdownRe
searchers Discover Human-Like Brain Waves In Lab-Grown Mini-BrainsStud
y Finds Market Conditions Perfect for Disney+ RolloutScientists Want T
o Build A Space Elevator From Earth To MoonNew Safari App Lets You Tra
ck Cicadas Life CycleCanadian Man Wins $60M Lottery After Playing Same
 Numbers For 30 Years80-Year-Old Woman Sleeping In Car Wakes Up To Fin
 d It MissingBringing me on was a forward-looking move on the part of 

 our founders. This was just prior to the big data craze and the conventional wisdom that data can be a defining competitive advantage. Back then, it was a lot more common to build a data team later in a company’s lifecycle. But they were eager to learn and evolve as fast as possible, and I was attracted to the company’s culture and mission. So even though we were a very small-data shop at the time, I decided to get involved.T

 here’s a romanticism in Silicon Valley about the early days of a startup: you move fast, make foundational decisions, and any good idea could become the next big thing. From my perspective, that was all true.B

 ack then we knew so little about the business that any insight was groundbreaking; data infrastructure was fast, stable, and real-time (I was querying our production MySQL database); the company was so small that everyone was in the loop about every decision; and the data team (me) was aligned around a singular set of metrics and methodologies.But fi


ve years and 43,000 percent growth later, things have gotten a bit more complicated. I’m happy to say that we’re also more sophisticated in the way we leverage data, and there’s now a lot more of it. The trick has been to manage scale in a way that brings together the magic of those early days with the growing needs of the present — a challenge that I know we aren’t alone in facing.At the 2015 Airbnb OpenAir developer confere

nce in San Francisco on June 4.Above: At the 2015 Airbnb OpenAir devel
oper conference in San Francisco on June 4.Image Credit: Jordan Novet

/VentureBeatSo I thought it might be worth pairing our posts on specif
ic problems we’re solving with an overview of the higher-level issues data teams encounter as companies grow, and how we at Airbnb have responded.This will 

mostly center around how to connect data science with other business functions, but I’ll break it into three concepts — how we characterize data science, how it’s involved in decision-making, and how we’ve scaled it to reach all sides of Airbnb.I won’t say that our solutions are per

fect, but we do work every day to retain the excitement, culture, and impact of the early days.Data isn’t numbers, it’s peopleThe foundation on which


 a data science team rests is the culture and perception of data elsewhere in the organization. So defining how we think about data has been a prerequisite to ingraining data science in business functions.In the past, data was often referenced in cold, numeric terms.

  It was construed purely as a measurement tool, which paints data scientists as Spock-like characters expected to have statistics memorized and available upon request. Interactions with us would therefore tend to come in the form of a request for a fact: how many listings do we have in Paris? What are the top 10 destinations in Italy?While answering questions a

	nd measuring things is certainly part of the job, at Airbnb we characterize data in a more human light: it’s the voice of our customers. A datum is a record of an action or event, which in most cases reflects a decision made by a person. If you can recreate the sequence of events leading up to that decision, you can learn from it; it’s an indirect way of the person telling you what they like and don’t like — this property is more attractive than that one, I find these features useful but those — not so much.This sort of fe

	edback can be a goldmine for decisions about community growth, product development, and resource prioritization. But only if you can deciph





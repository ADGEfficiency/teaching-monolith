## https://localghost.dev/2019/08/what-questions-should-you-ask-at-an-engineering-interview/

“Do you have any questions for us?”

It might be tempting to just skip over this with a “no, thank you” - maybe the job description gave you enough information for now - but you should always ask at least one question.

How closely do the dev team work with business stakeholders/customers?

How does work come in to the team?

How involved are engineers with deciding what to build?
- Am I going to be involved in the decision making and the shaping of what we’re building or am I going to be blindly picking up JIRA tickets? Is it an iterative development process, or is it a case of “requirements come in, code comes out 6 months later”?

Who makes technical decisions? How much independence do product teams have to make technical decisions?A
- Is it going to be a case of “here is the work, go and do it” or “how shall we build this? What do you think?”

Who looks after the live applications?
- Is it “you build it, you run it” or is it “you build it, and throw it over the wall”? Do engineers have ownership of the apps they build, and are they trusted to look after them?

What’s your deployment process like?

What does an average path to production look like for a service or application?

Do you practice continuous integration?

How often do you release to production?

Can I deploy stuff myself on an ad-hoc basis, or is it once a week/every three months? Is it going to be six months before you let me put it into the wild?

This is about finding out how much friction there is in the path to production. The more obstacles and Process With A Capital P, the more obstacles to innovation and experimentation. That said, there is a happy medium, and I don’t believe you should be firing off software into prod without due diligence, some process and quality control, especially when you’re working with people’s data. It’s worth finding out how the company handles that delicate balance.

Bonus points for continuous deployment.

Say I wanted to spin up a new service. How would I do that?

Would I need to get permission from the Change Advisory Board in a distant ivory tower? Would I need to write numerous documents and have handover meetings for deployment and maintenance?

The answer I got in my Monzo interview was “there’s a command line script to generate a new service” and I nearly wept with joy.

How do you do version control?

If they say “Subversion”, it’s time to question why. Is there a big beast of a monolith that was written in Java 6 and nobody has quite had the guts to move it off SVN because they aren’t quite sure where all the code lives, and do you really want to work with that every day?

How are architectural decisions made?

Do you have an architecture team? What do they do?

Do you have people whose job title is literally “Architect”? If so, are they hands-on and technical, or do they come in and tell you how to build stuff and then leave again? Am I going to be allowed to make my own decisions about the structure of the software I’m building?

I’ve definitely met some good architects, but really things like solution architecture should be done by the team building the actual thing.

What’s your testing strategy?

Do your developers do any testing? (Conversely, are you obsessed with as high test coverage as possible?) And if there’s pretty poor test coverage, are they open to improving it or do they see it as a waste of time?





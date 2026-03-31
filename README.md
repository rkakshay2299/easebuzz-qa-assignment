## Task 5: Strategy & Leadership

1. Flaky Automation Tests Dropping Sprint Velocity
Honestly, the first thing I'd do is just look at the data. Which tests are failing? Is it the same 5 tests every time or random ones? Because that tells you completely different things.
If it's the same tests repeatedly, those are your priority. Pull them out of the pipeline immediately — I'm not letting 3 broken tests block the whole team's sprint. Tag them, park them, move on for now.
Then I'd sit with my team and say "okay, what's actually going on here?" Nine times out of ten it's one of three things — bad locators, someone put a hard sleep in there, or the test data is inconsistent between runs. We've all seen it.
I'd split the fixes across the team based on who knows which module best. No point in me assigning the login flow tests to someone who's never touched auth. Give people ownership of what they know.
And I'd be honest with the team — retries are a band-aid. We can add them temporarily to reduce noise, but if we ship a flaky suite and call it done, we've just pushed the problem forward. The goal is tests people actually trust.

2. Critical Bugs Caught by Client in Production
First thing — don't panic, don't point fingers. Get the bug reproduced, loop in the developer, and get a fix moving. Client is waiting, that's the priority.
But once that's done, I'd sit with the team and just ask honestly — how did this get through? Not in an accusatory way, genuinely trying to understand. Was the scenario never written as a test case? Did we test it but miss something? Was it only reproducible in production because of data or config differences?
That conversation usually gives you the real answer. And based on that, you fix the specific gap — write the missing test, update the checklist, whatever it is.
What I'd also do is look at whether this is a one-off or a pattern. If two critical bugs slipped through, I want to know if our coverage of critical flows is actually solid or if we just assumed it was.
The mindset I try to keep, and push my team to have, is that a production bug isn't a failure — it's a gap that we didn't know existed. Now we know. Fix it and make sure it never slips through the same way again.
## Task 5: Strategy & Leadership

### 1. Handling Flaky Automation Tests

If sprint velocity is dropping because of flaky tests, I wouldn’t try to fix everything at once. First, I would identify which tests are flaky by looking at test reports or failure patterns.

Then I would separate those flaky tests from the main pipeline so they don’t block the team. After that, I’d start fixing them one by one by checking common issues like unstable locators, unnecessary waits (like sleep), or test data problems.

In many cases, replacing hard waits with proper waits and improving element locators solves most of the instability. I would also run those tests multiple times to confirm they are stable after fixes.

If needed, I might temporarily add retries to reduce impact, but the focus would always be on fixing the root cause, not hiding the problem.

The main goal is to make the automation suite reliable again so that the team can trust the test results.


---

### 2. Handling Critical Bugs Missed in Production

If critical bugs are reported in production, my first priority is to quickly understand and reproduce the issue. I would work closely with the developer to help identify the root cause and validate the fix as soon as possible.

Once the issue is fixed, I would make sure we add proper test coverage for that scenario so it doesn’t happen again.

After that, I would analyze why it was missed in the first place. It could be due to missing edge cases, incomplete requirements, or gaps in test coverage.

Based on that, I would improve the testing process, like adding more negative scenarios, improving test case reviews, or making sure we test with more realistic data.

The idea is not just to fix the bug, but to learn from it and strengthen the overall testing process so similar issues don’t reach production again.
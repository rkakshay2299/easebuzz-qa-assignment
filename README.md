## Task 5: Strategy & Leadership

#1. Flaky Tests

To handle flaky tests impacting sprint velocity, I first identify patterns by analyzing test failures. If specific tests are repeatedly failing, I temporarily remove them from the main pipeline to avoid blocking the team.

Next, I focus on identifying root causes. Common issues include unstable locators, improper waits, and inconsistent test data. These are addressed by improving locator strategies, replacing hard waits with dynamic waits, and stabilizing test data.

Retries may be used temporarily to reduce noise, but the primary goal is to fix the underlying issues and ensure the test suite remains reliable and trustworthy.


#2. Critical Bugs Caught by Client in Production

FWhen critical bugs are reported in production, the immediate priority is to reproduce the issue and collaborate with developers to validate and release a fix quickly.

After resolution, I analyze the root cause to understand why the issue was missed. This could be due to gaps in test coverage, missing edge cases, or differences in test and production environments.

Based on these findings, I improve the testing process by adding relevant test cases, enhancing coverage (including negative scenarios), and refining review practices to prevent similar issues in the future.
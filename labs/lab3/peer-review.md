Peer-Review Guidelines
======================

## General description

For Lab 3, each group of students (hereinafter the submitting group) is expected to submit their solution to another group (hereinafter the reviewing group), which will have to assess whether the submission passes or fails.
Each submitting group will submit to a reviewing group **selected by the teaching team** in order to reduce conflicts of interest (matching groups who tackled the same Bonus parts as much as possible).
However, the review process is not blinded.

The groups are paired and will review each other, as such, *submitting* or *reviewing* should be seen as a role that each group will have to endorse.
Each submitted solution must be clear whether any bonus part has been tackled or not.

## Assessment
Each reviewing group have to assess whether the submitted solution is acceptable or not according to the following criteria:

- the web application runs
- it displays the complete map of tram lines
- it is possible to query the shortest path between any two points

Optionally, the reviewing group may have to assess the bonus assignments:
- whether the web application account for changes (Bonus 1)
- whether it is possible to select departures by clicking on any stops (Bonus 2)

These points 3 (+ 2) points will be assessed during a live presentation (physical or online) conducted by the submitting group on their own machines (we do not expect you to run someone else's code).

## Report

The reviewing group must write a short report motivating their decision according the criteria mentioned above.
The report must been submitted as an issue opened on the other group's repository.
In order to open such an issue, you must first invite the other team as collaborators, as explained [here](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository).

You must mention in this issue the name of which must include the names of the reviewing group (person 1 and person 2 if the group is a pair) and of the submitting group (person 3 and person 4 if the group is a pair) as `name1-surname1_name2-surname2_reporting_name3-surname3_name4-surname4`.

This is the template for the report/issue:

Section 1: Core assignment
- Q1: Does the application run? --> yes/no
- Q2: Does the application display the complete map of tram lines? --> yes/no
- Q3: Is it possible to query shortest path between any two points? --> yes/no

Section 2: Optional tasks
- B1: Is the submission successfully accounting for Bonus Part 1? --> yes/no
- B2: Is the submission successfully accounting for Bonus Part 2? --> yes/no

Section 3: Code quality

It must at least include whether:
- code from lab 2 has been properly reused (i.e., in an efficient way without [boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code))
- dijkstra has been implemented and used as intended: there is just
  one definition of the function itself, and different distances are
  obtained by just changing the cost function

Section 4: Screenshots
Insert two screenshots: 
- screenshot 1 must present the web application displaying a shortest path between two stops (similar to the one presented in the assignement [here](https://htmlpreview.github.io/?https://github.com/aarneranta/chalmers-advanced-python/blob/main/labs/lab3/examples/show_route.html) but with **different tram stops** than in the example)
- screenshot 2 must present the code of the function `show_shortest()` (the main function required in the core part of the assignment, see [here](https://github.com/aarneranta/chalmers-advanced-python/blob/main/labs/lab3/lab3.md#your-todo-continue-from-here)).

Note that all Sections are **mandatory** in the report, although Section 2 can be left blank if no bonus part has been tackled.
Section 3 is more open than the other sections, you can write general comments on the optimization of the code and good practices of Object Oriented Programming.

## Deadlines
### Registration
The deadline for the registration to _at least two_ peer-review sessions is **Dec 11** firm.
That is, each group has to suggest at least two sessions during which they can be available in order to facilitate pairing with other groups (see below).

Each group will have to perform only one demonstration during one session with one group. 

### Code 
The deadline for the submission of your code is **Dec 13** firm, but you can submit beforehand.

### Report, demonstration, and self-registration

**External link for scheduling**: 

https://docs.google.com/spreadsheets/d/1Jy4RNaheW5Dzd0aQ6tJ7JkCVXdjbSTVOjTTdR3155TY/edit?usp=sharing

The demonstration are conducted during peer-review sessions which will be organized on:
- **Dec 14**, 13-15 and 15-17
- **Dec 15**, 10-12, 13-15, and 15-17

We provide a spreadsheet to facilitate the pairing (**self-registration**) required for the demonstration, which includes an example on how to use it.
The spreadsheet contains all relevant information for the pairing, such as whether you addressed _bonus_ parts, _when_ you are available and _how_ (physically or only on zoom), means of _contact_ and name of your _repository_.
Please indicate when you have found a pair, a column is dedicated to that (_Registered_).

Note that **you are ultimately responsible** for selecting a pair, conducting the demonstration and ensuring a seamless functioning of the process.

The rooms are the same as booked in TimeEdit for "studentledd undervisning" and "laboration" at these times.
You also have the possibility to conduct such session online via Zoom (using the screen sharing feature).

The report must be written **within 1 day (24 hours)** after the peer-review session.

## Other considerations - resubmission

A TA is ultimately responsible for the validation of the submission, and also has the responsibility to support the reviewing group in their endeavor (typically for edge cases).
Note that a solution will have to be resubmitted if it doesn't pass the peer-review process (as prescribed in Section 1 of the report), a submitting group can apply for resubmission **once**.
The same reviewing group is assigned for the resubmission, as for the TA.
A group reviewing a resubmission can simply add an addendum to their initial report.
The resubmission report must be written **within 1 day (24 hours)** after resubmission (as the structure should already be familiar to the reviewers).

We invite you to self-manage your resubmission on your private time, which includes a new demonstration.

**The deadline for resubmitting the report/issue of lab 3 is Jan 5.**

The bonus parts must be included already in the first
submission. But if any of them fails, they can be completed in a
resubmission. No new bonus parts can be added in the resubmission (in
other words, the first deadline **Dec 13** also applies to the bonus
parts).


---
layout: post
title: Cool Tools for Git
description: Handy extensions that enhanced and integrated various <code>Git</code> related services at a previous company.
when: 2018
image_url: /images/cool_tools.jpg
tags: [Git, JS, Python]
---

## Key Points
- Browser extensions that enhanced and integrated Jira, Bitbucket, and Team City websites to  display better information, add inter-site links, and improve overall workflow.
- A desktop program which improved the setting up of local environments, usually during code reviews. It reduced a frequent 5+ min workflow to under 20s.
- They were built for internal use at a previous company had 100s of installs across various teams.

---

## Background

[Read about _why_ these extensions were built]({% post_url 2018-01-02-cool-tools-background %}){:.big-link}

---

## Features

Extensions were modularised and added functionality for specific use cases. Some were more applicable for architects, whilst others were tailored for code reviewers etc. Devs simply chose what they wanted.

Here were some popular ones:

---

### Bildebeest

{:.img-with-text}
![Image of Bildebeest logo](/images/cool_tools_bildebeest.jpg){:.image-small}<br>
Like a Wildebeest, this tool was all about speed and power. We also liked naming tools after animals.

Bildebeest (builder beast) was a desktop app used to build apps quickly when testing code locally. It was written in `Python` and integrated with Jira and Bitbucket

Often you needed to download and build code from multiple repos. It took many dozens of clicks to find a branch, download it, and build it - _and that was just for one app!_ With Bildebeest you simply entered in a Jira number, then Bildebeest would fetch all of necessary code and build the apps asynchronously. This reduced a 5+ minute workflow to under 20s.

<blockquote>
BILDEBEEST IS AWESOME!!<br>
- An actual quote from a colleague
</blockquote>

The idea sounds simple but this app had to utilise many technologies in order to work. Once it was working though it was just magic!

---

### Web Tools

{:.img-with-text}
![Image of Dead Branch Finder](/images/cool_tools_dead_branch_finder.png)<br>
A dead branch finder in Bitbucket which identified deletable branches based on dozens of criteria. It integrated with Jira and found branches that were old, merged, completed etc.

---

{:.img-with-text}
![Image of Jira Popup Improvements](/images/cool_tools_jira_popup.gif)<br>
Added critical info to Jira to help architects track and merge branches during release.

---

{:.img-with-text}
![Image of Bitbucket Improvements](/images/cool_tools_pr_build_status.png)<br>
Integrated Bitbucket and Team City to display whether tests had passed for a given branch. Team City's own implementation of this did not work with our setup.

---

{:.img-with-text}
![Image of Jira Improvements](/images/cool_tools_pr_jira_status.png)<br>
Improved Jira integration in Bitbucket. This example shows a new Jira status and link when viewing branches.

---

{:.img-with-text}
![Image of Team City links](/images/cool_tools_pr_link.png)<br>
Added dozens of links in Team City to go to Bitbucket and Jira pages.

---

{:.img-with-text}
![Image of Team City timeout UI](/images/cool_tools_timeouts.png)<br>
Improved the look of tests that timed out in Team City.

---

## Tech Specs

### ![Chrome](/icons/chrome.png) Web Tools
- Written in `JS` and deployed through [Tampermonkey](https://www.tampermonkey.net/).
- Scripts were linked to internal Bitbucket urls which meant code changes were automatically deployed to users.
- Future work was planned to integrate all scripts into a standalone browser extension.
- Jira and Bitbucket extensions made use of the [Atlassian User Interface](https://docs.atlassian.com/aui/) to ensure UI changes were visually consistent.

### ![Bildebeest](/icons/bildebeest.png) Bildebeest
- Written in `Python` and directly integrated with `Git`, Jira, and Bitbucket services.
- Secured auth details via the operating system credential manager.
- Distributed to users via an internal tooling platform.
- Functioned as a system tray app which users simply clicked on to activate.
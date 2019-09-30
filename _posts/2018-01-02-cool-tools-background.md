---
layout: post
title: Cool Tools for GIT - Background
hidden: 1
---

[Back to original article here]({% post_url 2018-01-02-cool-tools %}){:.big-link}

---

`GIT` was the version control system of choice at a previous company who made use of the following online services:
- [Jira](https://www.atlassian.com/software/jira) for issue tracking.
- [Bitbucket](https://bitbucket.org) as the online repository and code review platform.
- [Team City](https://www.jetbrains.com/teamcity/) for automated tests and code deployment.

<blockquote>
Hol' up, aren't these services integrated already? What are these extensions for?<br>
Good question!
</blockquote>

Firstly, you must understand that the codebase was setup as follows:
- Hundreds of independent 'apps' were contained in separated `GIT` repos.
- Features often required changes in multiple apps as apps were highly integrated.
- Deploying a single feature could therefore require one to review, track, and deploy code over multiple repos.

<blockquote>
They already handle multiple repos don't they?<br>
Yes, but...
</blockquote>

They were often lacking given our specific setup:
- Jira linked to pull requests but with limited information. 'Which apps have this feature?', 'Has this code been deployed?'. We couldn't easily tell.
- Services required manual integration. For example if a Team City build failed, we had to manually find the Jira issue or Bitbucket pull request.
- Finding code, fetching it locally, then building it all took time. More apps meant more work.

The `GIT` tools fixed these types of issues and simplified the lives of developers in this multi-repo world.

---

[Back to original article here]({% post_url 2018-01-02-cool-tools %}){:.big-link}
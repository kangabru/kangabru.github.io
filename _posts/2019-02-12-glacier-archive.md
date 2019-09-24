---
layout: post
title: Glacier Archiver
description: An app using an unorthodox Python and Electron combo which helps me track, summarise, and archive terrabytes of media files on two continents.
when: Feb 2019
image_url: images/glacier.jpg
tags: [Python, React, AWS S3, Electron, Typescript, Redux]
---

## Features

`Glacier Archiver` is the perfect assistant for me to back up endless apply of photos and videos. It's also quite performant despite the name.

I generate a lot of data through my travel and photography habbits. In fear of losing this data on the road, I craved a backup solution that was easy to use and secured in multiple locations. Consumer solutions didn't seem to cut it, and thus, a new project was born.

It features:

{:.img-with-text}
![Glarier Archiver Summary Image](/images/glacier_summary.jpg)
A cozy `React` built UI which includes a file explorer, upload tracker, and ability to run various actions.

{:.img-with-text}
![Glacier Archive Example Contact Sheet](/images/glacier_contact_sheet.jpg)
Ability to summarise media content into a [contact sheet](https://en.wikipedia.org/wiki/Contact_print) which helps me to locate files visually.

---

## Tech Specs

Originally all functionality was performed through a collection of `Python` scripts. These scripts enabled me to summarise and perform my initial backup before embarking on an extended trip. The `Electron` part came after-the-fact and wraps the original logic in a nice and friendly UI.

### ![Python](/icons/python.png) Python
- Generates the data to render the file explorer. This includes the file 'is archived' and 'is summarised' tags.
- Summarises a folder into [contact sheets](https://en.wikipedia.org/wiki/Contact_print) which contains thumbnails of media files with their respective file names. These sheets are lightweight and provide a allow me to locate files visually.
- Handles AWS functionality such as restoring and download files.

### ![Electron](/icons/electron.png) Electron
- Allowed me to apply my love of web apps whilst utilising an existing python and file system backend.
- Electron apps are large and memory hungry, but as the only user this was acceptable because of its ease of development.

### ![React & Redux](/icons/react.png) React/Redux
- I love react. Why not try it out on the desktop?
- React and Redux were probably overkill, but let me easily create a solid, extensible, component based application.

### ![AWS S3](/icons/s3.png) AWS S3
- Stores all uploaded data. S3 was chosen for its affordability, security, and backup options.
- All files are backed up on 2 continents for redundancy. Syncing is provided by AWS.
- Use of this service included auth setup through SSH keys.
- [Rclone](https://rclone.org/) is used to perform bulk data uploads and track upload progress. This saved me some time doing it myself!
- The [AWS CLI](https://aws.amazon.com/cli/) is used to track uploaded files, [trigger file restores](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/restore-archived-objects.html), and download restored files.

# Usage


To extract all domains and subdomains from the list out URLs.

``python getalldomains.py urls.txt``

To extract all file extensions used in the list URLs.

``getallextensions.py urls.txt``

To extract path used in the list of URLs. Here I would suggest to use ``uro`` initially. Example: ``cat urls.txt | uro`` after decluttering url lists run the below file to get the paths. 

``getallpaths.py urls.txt``

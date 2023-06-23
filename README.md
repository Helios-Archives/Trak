# Trak
## Project not in development if you wish to take over the development message me on telegram @nyxqxx

## Contribution
If you wish to become a contributer on this project you can by adding a new site to the sites.cfg file. The format is as follows:
```
[site_url] | [texttofind],[texttofind],...
```

### how to find the text to find

1. obtain a url of an existing account and a url of a non existing account
2. use the get.py script at ./src/tools/get.py to get the html of both pages
3. find a difference in the two html pages (higher in the html the better)
4. add the new entry to the sites.cfg file
5. test the new entry with at least 3 active and 3 inactive accounts
6. submit a pull request with the new entry + the accounts used for testing for verification

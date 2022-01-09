# HOW TO RUN USING DOCKER

 - build the image

>docker build -t langpars .

 - run a new docker container named langpars

>docker run --name langpars \
    -d -p 5000:5000 \
    langpars

# RUNNING LOCALLY
- use pipenv install for dependencies

>pipenv install
- run index.py


# Fetch contents using curl
curl http://localhost:5000/repos/{user}

curl http://localhost:5000/lang/{user}

Github API has limit of 60 requests per hour for unauthorized users, 
one LangPars requests consumes multiple of those, 
depending on amount of repos that user has.

You can rise this limit to 5000 by authorizing.
for example using Github OAuth token in header of request:
in GithubAPI/auth.py inject token as token

# Ideas

Authorization:
- create configuration service for injecting token
- github to get oauth token (session wide, otherwise account/recognition system needed) https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps 

API:
- think about adding async for fetching data from github if functionality expands
- Show actual request limit, in response or in header
- Cache for repeating responses, endpoints for same user are repeating request, caching those would alleviate requests limiting
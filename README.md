# GithubLangPars
HOW TO RUN USING DOCKER
# build the image
docker build -t langpars .

# run a new docker container named langpars
docker run --name langpars \
    -d -p 5000:5000 \
    langpars

RUNNING LOCALLY
#use pipenv install for dependencies
pipenv install

#run index.py

# in both cases you can fetch contents using curl
curl http://localhost:5000/repos/{user}
curl http://localhost:5000/lang/{user}

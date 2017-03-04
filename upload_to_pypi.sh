#docker pull python:2.7
#docker pull python:3.4
#docker pull python:3.5
#docker pull python:3.6


#python2.7 setup.py bdist_egg upload
#python3.4 setup.py bdist_egg upload
#python2.7 setup.py sdist upload 

docker build -f ./Dockerfile_2.7 -t pypi2.7 .

docker run -it -v `pwd`:/prettysettings pypi2.7 python2.7 setup.py sdist upload -r pypi
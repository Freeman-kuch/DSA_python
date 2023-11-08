"""A hash function is a function where you put in a string1 and you get back a number. basically maps strings to numbers
the major use case of mapping is deinitely in the use of dictionaries"""
import requests


def voters_verification(name):
    voted = {}
    if voted.get(name):
        return f"{name} has already voted"

    voted.__setitem__(name, True)
    return f"{name}'s vote has been successfully cast"


print(voters_verification("newman"))

""" in its application in webapplication and severs 
1. it could be used for LFu to tailor an algorithm for feed users interest over a certain period of time
2. to speed up request to response time

so it is bold to assume the request checks the hash table(cache) if the information being requestes is present before 
making the request to the server or database in this case"""


def url_caching(url):
    cache = {}
    if cache.get(url):
        return cache.get(url)
    # make the request to the server
    content_requested = requests.get(url)
    cache.__setitem__("url", content_requested)
    return content_requested

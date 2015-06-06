#!/usr/bin/python

import re
import sys
import urllib2
import fresh_tomatoes
import move_store


input_movie_list = sys.argv[1:]
return_movie_list = []
for movie in input_movie_list:
    try:
        # get web content of information of a movie from Rotten tomatoes.
        rt_search_url = "http://www.rottentomatoes.com/m/{}/".\
            format(movie.strip().replace(' ', '_').lower())
        req = urllib2.Request(rt_search_url)
        res = urllib2.urlopen(req)
        content = res.read()

        # search paragraph tag, which contains movie synopsis from the content string.
        synopsis = re.search(r'(<p id="movieSynopsis".+?>)(.+?)(<)', content).group(2)
        synopsis = "From Rotten Tomatoes: " + synopsis + "..."

        # search image tag, which contains a movie poster image url from the content string.
        post_image_tag = re.search(r'<img class=" posterImage".+?>', content).group(0)
        image_url = re.search(r'(src=")(.+?)(")', post_image_tag).group(2)

        # get web content of search results of a movie from Youtube.
        yt_search_url = "https://www.youtube.com/results?search_query={}".\
            format(movie.strip().replace(' ', '+').lower() + "+trailer")
        req = urllib2.Request(yt_search_url)
        res = urllib2.urlopen(req)
        content = res.read()

        # search the first hyperlink tag, which contains a movie trailer url.
        trailer_url = re.search(r'(href=")(/watch\?v=.+?)(")', content).group(2)
        abs_trailer_url = "https://www.youtube.com" + trailer_url

    except:
        # If there is no result show an empty image so user can try run application with another movie.
        movie += "(No movie)"
        synopsis = "Movie not found"
        image_url = "#"
        abs_trailer_url = "#"

    finally:
        # store an instance of the movie with the proper information.
        return_movie_list.append(move_store.Movie(movie, synopsis, image_url, abs_trailer_url))

# generate an html file and show it on the browser.
fresh_tomatoes.open_movies_page(return_movie_list)

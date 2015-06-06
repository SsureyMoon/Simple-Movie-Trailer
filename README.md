# Movie Trailer Website

This python application simply generate .html file of movie trailers from your command line inputs.

## Check Environment

```bash
which python
```

should show a proper python path

## How it works

1. It get a space-seperated list of movies which user wants to generate their trailer website of.
2. It scrapes and parse Rotten tomatoes' website to get poster image and sysnopsis.
3. It scrapes youtube website with search query, and get the first trailer url from the list of results searched.

## Example

```bash
cd /where/your/project/root/is
python generate_movie_page.py 'school of rock' 'Avatar'
```

## Reference

Poster image, Synopsis: [Rotten Tomatoes](http://www.rottentomatoes.com/)
Trailer: [Youtube](https://www.youtube.com/)


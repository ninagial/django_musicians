# django_musicians
Web app to help like-minded musicians find each other

In actual reality, this app is an exercise to better understand Models and Views in Django, and provide a quick boilerplate for Django app development.

# Jim and Ronald

So, Jim is the leader of a death metal band. They are called Psychonecrosis and have published the Necrotic Psychosis demo. They are a power trio, but recently their drummer quit. They are currently looking for a drummer.
Their main influences are Obituary and Carcass.

Ronald is a drummer whose main influence is Death. Although not listed in Psychonecrosis's influences, the software should match them on the musical tastes distance criterion.
(And for now this is the only criterion.)

OK, let's assume that geographical distance and age are not prohibitive for the time being.
The app's novelty lies exactly in a sophisticated influence matching for non-mainstream musicians.

So when Jim logs in and goes to the 'Check out these musicians" section, he must be able to see only those musicians that are interested in this genre, play the instruments he needs, and live nearby.

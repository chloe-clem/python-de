# Lesson 1.4: Dictionaries and sets

1. When would I use a dictionary instead of a list? A dictionry is when you have a set of unique keys to look up other values right. They are the form jsons come in when calling apis. they are good ofr nested data. 
use a list when order or position matters (a ranking, a sequence of stops), and a dict when you look things up by a name or code (station code → details).
2. What's the difference between `d["key"]` and `d.get("key")`? When would I use each? The first one is when you know for sure tht key value exists, the second is when you are checking if it exists. both will return the vlaue accosiated with the key. Also the first one crashes with a KeyError. That’s actually useful when the data must exist: you want the pipeline to fail loudly rather than carry on with bad data. The seocond will retunr None if it  doesn't exist or you can specify a default value.
3. Why can a tuple be a dictionary key but a list can't? a list it muttable so it cannot be a key.
4. How do I tell a dict `{"a": 1}` from a set `{1, 2}`? colon = dict, no colon = set.
5. SQL equivalent I want to remember: sum(dict.values())
import requests

def get_rhymes(word):
    """ (string) -> (List of 3 Strings)
    
    Takes a word and returns 3 rhyming words in a list. Can edit
    para_dict["max"] = "3" to another number to produce more results
    
    -> get_rhymes("funny")
    -> ['money', 'honey', 'sunny']
    """
    baseurl = "https://api.datamuse.com/words"
    para_dict = {}
    para_dict['rel_rhy'] = word
    para_dict["max"] = '3'#Get a max of 3 results, change for more
    resp = requests.get(baseurl, params=para_dict)
    word_ds = resp.json()
    return [d['word']for d in word_ds]
    return resp.json() 
    
    # Return a Python object(a list of dictionaries)

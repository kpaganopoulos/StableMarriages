# StableMarriages
A python script that implements the Gale-Shapley Algorithm in order to find a stable matching for any given input.

##Stable Marriages 
A python script that implements the Gale-Shapley Algorithm in order to find a stable matching for any given input. According to the given arguments while running the script, it finds the matching for "men" or "women". Input files should be given in JSON type with the following format:

{
  "men_rankings": {
    "abe": ["cat", "bea", "ada"],
    "bob": ["ada", "cat", "bea"],
    "cal": ["ada", "bea", "cat"]
  },

  "women_rankings": {
    "ada": ["abe", "cal", "bob"],
    "bea": ["bob", "abe", "cal"],
    "cat": ["cal", "abe", "bob"]
  }
}

Output is given in JSON type files with the following format:

{"abe": "cat", "bob": "bea", "cal": "ada"}

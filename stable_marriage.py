import copy
import sys
import json

json_data =  json.loads(open(sys.argv[2]).read())

men_ranks = json_data['men_rankings']
women_ranks = json_data['women_rankings']

men = list(men_ranks.keys())
women = list(women_ranks.keys())

married = {}

# ---------------------  ΆΝΤΡΕΣ  (1η Περίπτωση) ------------------- #


if ( sys.argv[1] == '-m' and len(sys.argv) == 3 ):

    def marriage():

        menfree = list(men)
        men_ranks2 = copy.deepcopy(men_ranks)
        women_ranks2 = copy.deepcopy(women_ranks)
        
        i = 0
        while ( len(menfree) > 0 ):
            man = menfree.pop(i)
            menlist = men_ranks2[man]
            woman = menlist.pop(i)
            zeugos = married.get(woman)
            
            if ( zeugos is None ):
                # Είναι ελεύθερη
                married.update({woman:man})   
    
            else:
                # Είναι δευσμευμένη
                womenlist = women_ranks2[woman]
                
                if ( womenlist.index(zeugos) > womenlist.index(man) ):
                    # Προτιμά τον νέο άντρα
                    married.update({woman:man})
                    
                    if ( men_ranks2[zeugos] is not None ):
                        # Ο πρώην στρέφεται σε άλλες επιλογές
                        menfree[len(menfree):]=[zeugos]
                        
                else:
                    # Μένει πιστή
                    
                    if ( len(menlist) > 0 ):
                        # Ο άντρας στρέφεται σε άλλες επιλογές
                        menfree[len(menfree):]=[man]
                
        return dict(map(reversed, married.items()))
 
    married = marriage()
    
    JSON_data = json.dumps(married, sort_keys = True, indent = 4)
    print(JSON_data)



# -------------------- ΓΥΝΑΙΚΕΣ (1η Περίπτωση) --------------------- #

if ( sys.argv[1] == '-w' and len(sys.argv) ==3 ):
    
    def marriage():

        womenfree = list(women)
        men_ranks2 = copy.deepcopy(men_ranks)
        women_ranks2 = copy.deepcopy(women_ranks)

        i = 0
        while ( len(womenfree) > 0 ):
            woman = womenfree.pop(i)
            womenlist = women_ranks2[woman]
            man = womenlist.pop(i)
            zeugos = married.get(man)
            
            if ( zeugos is None ):
                # Είναι ελεύθερος
                married.update({man:woman})
              
            else:
                # Είναι δεσμευμένος
                menlist = men_ranks2[man
                                     ]
                if ( menlist.index(woman) < menlist.index(zeugos) ):
                    # Προτιμά τη νέα γυναίκα
                    married.update({man:woman})
                    
                    if ( women_ranks2[zeugos] is not None):
                        # Η πρώην στρέφεται σε άλλες επιλογές
                        womenfree[len(womenfree):]=[zeugos]
                        
                else:
                    # Μένει πιστός
                    
                    if ( len(menlist) > 0 ):
                        # Η γυναίκα στρέφεται σε άλλες επιλογές
                        womenfree[len(womenfree):]=[man]
                
        return dict(map(reversed, married.items()))
 
    married = marriage()
    
    JSON_data = json.dumps(married, sort_keys = True, indent = 4)
    print(JSON_data)



# --------------------- ΆΝΤΡΕΣ (2η Περίπτωση) ---------------------- #

if ( sys.argv[1] == '-m' and len(sys.argv) == 5 ):
    
    
    def marriage():

        menfree = list(men)
        men_ranks2 = copy.deepcopy(men_ranks)
        women_ranks2 = copy.deepcopy(women_ranks)
        
        i = 0
        while ( len(menfree) > 0 ):
            man = menfree.pop(i)
            menlist = men_ranks2[man]
            woman = menlist.pop(i)
            zeugos = married.get(woman)
            
            if ( zeugos is None ):
                # Είναι ελεύθερη
                married.update({woman:man})

            else:
                # Είναι δευσμευμένη
                womenlist = women_ranks2[woman]
                
                if ( womenlist.index(zeugos) > womenlist.index(man) ):
                    # Προτιμά τον νέο άντρα
                    married.update({woman:man})
                    
                    if ( men_ranks2[zeugos] is not None ):
                        # Ο πρώην στρέφεται σε άλλες επιλογές
                        menfree[len(menfree):]=[zeugos]
                        
                else:
                    # Μένει πιστή
                    
                    if ( len(menlist) > 0 ):
                        # Ο άντρας στρέφεται σε άλλες επιλογές
                        menfree[len(menfree):]=[man]
                
        return dict(map(reversed, married.items()))
 
    married = marriage()

    
    with open(sys.argv[4], 'w') as v: 
        json.dump(married, v, sort_keys = True, indent = 4)
        


# -------------------- ΓΥΝΑΙΚΕΣ (2η Περίπτωση) ---------------------- #

if ( sys.argv[1] == '-w' and len(sys.argv) == 5 ):

    def marriage():
        
        womenfree = list(women)
        men_ranks2 = copy.deepcopy(men_ranks)
        women_ranks2 = copy.deepcopy(women_ranks)

        i = 0 
        while ( len(womenfree) > 0 ):
            woman = womenfree.pop(i)
            womenlist = women_ranks2[woman]
            man = womenlist.pop(i)
            zeugos = married.get(man)
            
            if zeugos is None:
                # Είναι ελεύθερος
                married.update({man:woman})
                
            else:
                # Είναι δεσμευμένος
                menlist = men_ranks2[man]
                
                if ( menlist.index(woman) < menlist.index(zeugos) ):
                    # Προτιμά τη νέα γυναίκα
                    married.update({man:woman})
                    
                    if ( women_ranks2[zeugos] is not None ):
                        # Η πρώην στρέφεται σε άλλες επιλογές
                        womenfree[len(womenfree):]=[zeugos]
                        
                else:
                    # Μένει πιστός
                    
                    if ( len(menlist) > 0 ):
                        # Η γυναίκα στρέφεται σε άλλες επιλογές
                        womenfree[len(womenfree):]=[woman]
                
        return dict(map(reversed, married.items()))
 
    married = marriage()

    with open(sys.argv[4], 'w') as v: 
        json.dump(married, v, sort_keys = True, indent = 4)


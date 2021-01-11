
# number of combinations of len l of set len n = n ! / l! * (n-l)!

def get_combinations(characters , comb_len):

    combinations = []

    def combinations_generator(start , curr_length , curr_txt  , characters):
        
        if curr_length == 0:
            combinations.append(curr_txt)
            return None
        
        for i in range(start , len(characters)-curr_length+1):
            combinations_generator(i+1 , curr_length-1 , curr_txt+characters[i] , characters)

    combinations_generator(0, comb_len , "" , characters)
    return combinations
        
    
def main():
    characters = "abc"
    comb_len = 2
    print(get_combinations(characters , comb_len))
     
main()
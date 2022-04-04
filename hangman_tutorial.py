'''Írj egy programot, amely egy ötbetűs főneveket tartalamzó listából véletelenszerűen választ egyet, 
amit a játékosnak egy-egy betű megadásával kell kitalálnia! 
A főprogramot a main() függvény tartalmazza, és ezen kívűl legyen még minimum 2 - részfeladatokat megvalósító - függvény! 
'''
import random

def select_from_list():
    '''Randomly select a word from a list of words.
       Return word in string format.'''
    words = ['labda', 'cukor', 'tükör', 'kakas', 'bolha', 'pince']
    return random.choice(words)
     
def create_hidden(word):
    ''' "_" kerül a listába minden egyes betű után, ami a szóban van. 
       Returnöli a listát. tartalma = ["-","-","-",..."_"]'''
    return ["_" for letter in word]
    
    # ez ugyanazt csinálja, csak hosszabb:
    # rejtett_lista = []
    # for letter in word:
        # rejtett_lista.append("_")
    # return rejtett_lista
     
def look_for(guess, word):
    location_of_guess = [] # legyen lista, mert lehet több találat is
    for index, letter in enumerate(word):
        if letter == guess:
            location_of_guess.append(index)
    return location_of_guess
    
def mark_found_guess(guess, indicies, hidden_word):
    for index in indicies: # ha többször is be kell illeszteni egy betűt (pl labdában 2 A betűt találtunk)
        hidden_word[index] = guess # kicseréli a rejtett szóban az adott indexen lévő betűt a tippelt betűre (pl "_" -> "A")
 
    return hidden_word # a végén visszaadja az új (kiegészített) listát
    
def main():
    '''1. Select a word in string format from a predefined list of strings
       2. Split string into list of characters "_" this will be used as the main 'playing field'
       3. Make guesses until all the "_" are gone from the hiddden word
        a) make a guess
        b) look for letter/s in the word, mark their spots 
        c) insert found letter/s into the marked spots in the hidden word
        d) break when no more "_" are in the hidden word
       '''
    word = select_from_list()
    hidden_word = create_hidden(word)
    
    while "_" in hidden_word:
        guess = input("Make a guess!\n")
        location_of_guess = look_for(guess, word) # tippet look_for meg a szoban
        hidden_word = mark_found_guess(guess, location_of_guess, hidden_word)
        print("".join(hidden_word))
        
    print("No more hidden words, game over! GG!")
    
main()
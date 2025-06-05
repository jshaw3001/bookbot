from stats import word_count, char_count, dict_sort
import sys
   
def main(filepath):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}\n----------- Word Count ----------")
    print("Found " + word_count(filepath) + " total words")
    print("--------- Character Count -------")
    for x in dict_sort(filepath):
        print(x)
    print("============= END ===============")
    
if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
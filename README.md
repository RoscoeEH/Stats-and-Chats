# Stats-and-Chats

This program has two main portions to it:

Stats: This one takes a .txt file as an argument and counts the number of times each word appears. It holds the counts in a sorted list that maintains order using the fixOrder function; this function takes the list and an index and moves that index to the appropruate spot. Sorting as the program runs is significantly faster because you each element is incremenented one by one so at most one value needs to be moved.

Chats: This also takes a .txt file but instead it returns a statement that is similar to the originial file. It does this by building groups of words of a maximum length and selecting a next word at random based on the patterns of the original file. 


from sys import argv
# open and read file
# save file as text
# split text by "\n"
# create dict with key value pairs
# alphabetically print restaurant (key) + " is rated at " + rating (value) + " stars."



def string_to_dict(text):
    restaurants = {}
    list_of_text = text.split("\n")

    for i in list_of_text:
        restaurant_to_rating = i.split(":")
        restaurants[restaurant_to_rating[0]] = restaurant_to_rating[1]
    return restaurants


def print_dict_alphabetically_by_key(dictionary):

    for key in sorted(dictionary.keys()):
        print "Restaurant '%s' is rated at %s stars." % (key, dictionary[key])


def main():
    script, filename = argv

    f = open(filename)
    filetext = f.read()
    print_dict_alphabetically_by_key(string_to_dict(filetext))




main()
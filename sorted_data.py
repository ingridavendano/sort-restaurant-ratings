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
        is_there_any_quotes(key,dictionary[key])


def print_with_a_new_list(dictionary):
    stars = []
    for key, value in dictionary.iteritems():
        if value not in stars:
            # stars.append(value)
            stars.append((value, key))

    stars = sorted(stars)[::-1]

    for rating in stars:
        is_there_any_quotes(rating[1],rating[0])


def is_there_any_quotes(key, value):
    if key.find("\'") != -1:
        print 'Restaurant "%s" is rated at' % key, '*' * int(value)
    else:
        print "Restaurant '%s' is rated at" % key, '*' * int(value)
 


def main():
    script, filename = argv

    f = open(filename)
    filetext = f.read()
    # print_dict_alphabetically_by_key(string_to_dict(filetext))
    print_with_a_new_list(string_to_dict(filetext))



main()
# Hey CodeWarrior,

# we've got a lot to code today!

# I hope you know the basic string manipulation methods, because this kata will be all about them.

# Here we go...
# Background

# We've got a very long string, containing a bunch of User IDs. This string is a listing, which seperates each user ID with a comma and a whitespace ("' "). Sometimes there are more than only one whitespace. Keep this in mind! Futhermore, some user Ids are written only in lowercase, others are mixed lowercase and uppercase characters. Each user ID starts with the same 3 letter "uid", e.g. "uid345edj". But that's not all! Some stupid student edited the string and added some hashtags (#). User IDs containing hashtags are invalid, so these hashtags should be removed!
# Task

#     Remove all hashtags
#     Remove the leading "uid" from each user ID
#     Return an array of strings --> split the string
#     Each user ID should be written in only lowercase characters
#     Remove leading and trailing whitespaces


def get_users_ids(st):
    # uid = st.replace("#","")
    # uid = uid.strip()
    # uid = uid.strip('uid')
    # uid = uid.lower()
    # uid = uid.split(",")
    # return uid
    final = []
    st = st.split(",")
    for uid in st:
        uid = uid.replace("#","")
        uid = uid.strip()
        uid = uid.strip('uid')
        uid = uid.lower()
        uid = uid.split(",")     
        final = final+uid

    return final  


st = '#uidawawerAAAA3453, #uidsdfsdfc34'

print(get_users_ids(st))

# skeleton_story ="""
# Today I went to a {adjective1} zoo. 
# In an exhibit, I saw a {noun1}. The {noun1} was {adjective2} 
# and suddenly {verb1} {adverb1}. I was so {adjective3} that I {verb2}, and everyone started laughing!"""


# skeleton_story ="""
# Today I went to a {adjective1} zoo.
#  In an exhibit, I saw a {noun1}. 
# The {noun1} was {adjective2} and suddenly {verb1} {adverb1}. I was so {adjective3} 
# that I {verb2}, and everyone started laughing!
# """

noun1 = str(input("Enter any Noun: "))
verb1 = str(input("Enter any Verb 'Ing': " ))
verb2 = str(input("Enter any Noun: "))
adb1 = str(input("Enter any Adverb:"))
adj1 = str(input("Enter any Adjective: "))
adj2 = str(input("Enter any Adjective: "))
adj3 = str(input("Enter any Adjective: "))

skeleton_story =f"""
Today I went to a {adj1} zoo.
 In an exhibit, I saw a {noun1}. 
The {noun1} was {adj2} and suddenly {verb1} {adb1}. I was so {adj3} 
that I {verb2}, and everyone started laughing!
"""
print(skeleton_story)

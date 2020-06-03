# check if the given string is palindrome or not #a="swetha" then a[0] equals 's'

def reverse(word):
    length = len(word)
    final = ""
    for a in word:
        final = final + word[length - 1]
        length = length - 1
    return final


def palindrome(word):
    return word == reverse(word)


print(palindrome("bob"))
print(palindrome("malayalam"))
print(palindrome("noon"))
print(palindrome("goat"))
print(palindrome("engineer"))

# find the reverse of a string 'swetha' to 'ahtews'

print(reverse("swetha"))
print(reverse("malayalam"))

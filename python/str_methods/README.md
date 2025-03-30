# STRING METHODS
# str.upper() Method 
The str.upper() method in Python is used to convert all characters in a string to uppercase. It does not take any parameters and returns a new string where all the letters are converted to uppercase. The original string remains unchanged, as strings are immutable in Python. 
# str.lower() Method
The str.lower() method is used to convert all characters in the string to lowercase. Like str.upper(), it does not take any parameters and returns a new string with all the letters in lowercase, leaving the original string unchanged. 
# str.title() Method
The str.title() method converts the first character of each word in the string to uppercase and the rest to lowercase. It also does not take any parameters and returns a new string with each word capitalized. 
# str.capitalize() Method
The str.capitalize() method converts the first character of a string to uppercase and all other characters to lowercase, ensuring proper capitalization without modifying the original string.
# str.swapcase() Method 
The str.swapcase() Method is used to reverse the case of each alphabetic character in the string, changing uppercase letters to lowercase and vice versa, while leaving non-alphabetic characters untouched. Both of these methods are immutable, creating new strings rather than altering the original ones.
# str.find() Method 
The  str.find() method searches for the first occurrence of a specified substring within the string, returning its starting index, or -1 if the substring is not found. This method is case-sensitive, and it allows optional parameters, start and end, to narrow the search range. 
# str.index() Method
the str.index() method returns the index of the first occurrence of a specified substring and raises a ValueError if not found, making it case-sensitive and allowing optional start and end parameters for a limited search. 
# str.startswith() Method 
the str.starstwith() method checks whether a string starts with a specified prefix, returning True or False , and supports optional start and end arguments to refine the check range. 
# str.endswith() Method
the str.endswith method functions similarly, checking if a string ends with a specified suffix, with support for start and ends parameters.
# str.count() Method
The str.count() method counts occurrences of a substring in a string, is case-sensitive, and allows optional start and end parameters to specify the range.
# str.replace() Method
the str.replace() method replaces occurrences of a substring with another, allowing an optional count to limit replacements, and returns a new string without modifying the original. immutable, case sensitive and optional count parameter. 
# str.strip() Method 
the str.strip method removes leading and trailing characters (default is whitespace) or a specified set of characters, returning a new string while leaving the original unchanged.
# str.lstrip() Method 
The str.lstrip() method in python removes any leading characters (such as spaces or specified characters) from the beginning of a string. This property is particularly useful for cleaning up text data where unwanted spaces or characters appear at the start. The property it showcases is the ability to handle and manipulate strings effectively by focusing on their starting portion.
# str.rstrip() Method 
The str.rstrip() method works similarly but targets the trailing characters at the end of a string. By default, it trims whitespace, but you can specify other characters to remove.
# str.split() Method 
The str.split() method is used to divide a string into a list of substrings based on a specified delimiter. The default behavior is to split by whitespace, making it highly useful for processing and analyzing text data.
# str.join() Method
The str.join() method in Python is used to concatenate elements of an iterable, such as a list or tuple, into a single string. The string it is called on acts as the delimiter between the elements.
# str.isalpha() Method 
The str.isalpha() method checks whether all characters in a string are alphabetic (i.e., letters only, with no numbers or special characters). If the condition is met, it returns True; otherwise, it returns False.
# str.isdigit() Method
The str.isdigit() method verifies if all characters in a string are numeric digits. Similarly to , it returns True if the string is made up entirely of digits and False otherwise.
# str.isalnum() Method
The str.isalnum() method checks whether all characters in a string are alphanumeric, meaning they consist only of letters and numbers, without any spaces or special symbols. For instance, if the string consists both number and alphabet would return True because it only contains letters and numbers, while False would return  if there is space. 
# str.issapce() Method
The str.isspace() method evaluates whether a string is made up entirely of whitespace characters such as spaces, tabs, or newline characters. For example, the string " " would return True because it only contains spaces, while  "hi hi" would return False as it includes non-whitespace characters.
# str.format() Method 
The str.format() method allows you to create formatted strings by embedding dynamic values into placeholders defined using curly braces {} . 
# F-string 
Provide a concise way to format strings by embedding variables directly into the text. To use them, you prefix the string with f and include the variables inside curly braces.

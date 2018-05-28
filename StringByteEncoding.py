# importing sys module
import sys 

#unpacking arguments 
script, encoding , errors = sys.argv

# definign a main function
def main(language_file,encoding,errors):
    line = language_file.readline()
    # some if condition 

    if line:
        print_line(line,	encoding,	errors)
        return main(language_file,	encoding,	errors)


# function to print line and encode and decode a string 
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors = errors)
    cooked_string	=	raw_bytes.decode(encoding,	errors=errors)

    # printing the line 
    print(raw_bytes,"<==>",cooked_string)

if __name__ == '__main__':
    languages = open("languages.txt",encoding="utf-8")
    main(languages,encoding,errors)
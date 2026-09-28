# computers store characters as numbers
# some are whitespaces and others are control characters (as they control input/output devices)
# Whitespaces
    # an example will be that is invisible to the naked eye, is a special code, or a pair of codes,
    # (different OS treat the issue differently)
    # which are used to mark the ends of the lines inside text files
    # people are able to observe the effect of these signs where the lines are broken

# The ASCII (American Standard Code for Information Interchange) is the widely used and universally accepted code
    # that all devices use.
    # it provides 256 different chars
    # only encodes latin alphabets and some of its derivates

# I18N (short for internationalization)
    # the software is a standard in present times
    # each program has to be written in a way that enables it to be used all around the world

# Unicode
    # code pages helped the industry solve I18N issues for some time only.
    # Unicode assigns unique auambiguous characters(letter, hyphens, ideograms, etc.) to more than a million code points
    # the first 128 code points are identical to ASCII and the first 256 Unicode code points are identical to 
    # ISO/IEC 8859-1 code page(a code page for western european languages)
    # able to encode virtually all alphabets being used by humans

# UCS-4 (Universal Character Set)
    # the unicode only names all available characters and assigns them to planes(a group of characters
    # of similar origin, application, or nature.)
    # UCS-4 is one of the most general of standards describing the techniques used to implement
    # Unicode in computer and storage systems
    # uses 32-bits (4 bytes) to store each character and the code is the unique Unicode code points
    # file encoded with ucs-4 may start with a BOM(byte order mark)
    # UCS-4 is a rather wasteful standard. it increases the text's size by four time compared to ASCII

# BOM
    # byte order mark is a special combination of bits announcing the encoding used by a files content(e.g. USC-4 or UTF-8)

# UTF-8 (Unicode Transformation Format)
    # it is smarter. uses as many bits for each of the code points as it really needs to represent them
    # all latin chars and all standard ASCII chars occupy 8 bits
    # non latin 16 bits
    # CJK (China-Japan-Korea) ideographs occupy 24 bits
    # it doesnt need BOM(byte order mark)

# Python 3 fully supports unicode and UTF-8
    # during all input and output
    # to name variables and other entities
    # Python 3 is I18Ned
        # supports natively global char sets, multi-language data processing, international software development
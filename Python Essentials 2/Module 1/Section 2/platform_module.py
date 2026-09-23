# Platform module lets us access the underlying platform's data
# i.e. hardware, OS, interpreter

from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

# platfrom(aliased = False, terse = False)
# aliased when True or non-zero, presents the alternative underlying layer names instead of common one
# terse when True or non-zero, may convince the func to present a briefer form of the result(if possible)

# print(platform())
# print(platform(1))
# print(platform(0, 1))

# machine() to get the generic name of the processor which runs the OS
print(machine())

# processor() returns the real processor name (if possible)
print(processor())

# system() return generic OS name
print(system())

# version() returns OS version
print(version())

# python_implementation() returns python implementation (expect CPython)
print(python_implementation())

# python_version_tuple() returns 3-element tuple with pythons major, minor version and patch level number
print(python_version_tuple())

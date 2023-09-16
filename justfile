default: black isort

# Format with black formatter
black:
    black mysite/

# Sort imports using isort
isort:
    isort mysite/

# Remove unused imports using unimport
unimport:
    unimport mysite/

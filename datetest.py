from dateutil.parser import parse

last_edited = parse('June 11, 2021')

update_after = parse('June 10, 2021')

print(update_after < last_edited)
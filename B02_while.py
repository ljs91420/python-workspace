# B02_while.py

i = 0;

while i < 10:
    print("Hello~ %d" % i);
    i = i + 1;

i = 0;
while True:
    print("Infinite Loop~!! %d" % i);
    i = i + 1;
    if i == 1000:
        break;
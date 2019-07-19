g=input()
if((g>='a' and g<='z') or (g>='A' and g<='Z')):
  if(g=='a' or g=='A' or g=='e' or g=='E' or g=='i' or g=='I' or g=='o' or g=='O' or g=='u' or g=='U'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")

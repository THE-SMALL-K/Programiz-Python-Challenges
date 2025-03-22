def convert_to_titlecase(s):
   list = s.split()
   y = " "
   for i in list:
      z = i[0].upper()
      z+= i[1:len(i)]
      y+=z + " "
   return y

print(convert_to_titlecase("hello world"))


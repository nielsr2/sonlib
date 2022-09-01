
def stripFM(content):
      # REMOVE POTENTIAL FRONT-MATTER ( e.g. :--- Type: Journal, Date: asfasdf ----) AT TOP OF FILE
   content = re.split('^---[\s\S]+?---',content)
   # only if it has it...
   if (len(content) == 2):
     c = content[1]
   elif (len(content) == 1):
     c = content[0]
   else:
     print("ERROR WITH FRONT-MATTER")
   return c

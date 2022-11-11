class StringUtility:   
  def __init__(self,s):     
    self.s = s    
    
  def __str__(self):     
    return self.s    
    
  def bothEnds(self):     
    if(len(self.s) <= 2):       
      return ''     
      return self.s[:2]+self.s[-2:]     
      
  def fixStart(self):     
    a = self.s[1:]     
    a.replace(self.s[0],'*')     
    return self.s[0]+a     
    
  def asciiSum(self):     
    total = 0      
    for i in self.s:       
      total += ord(i)      
      return total      
      
  def cipher(self):     
    key = len(self.s)     
    encrypt = ''      
    for i in self.s:    
      if (i.isupper()):         
        encrypt += chr((ord(i) + key - 65) % 26 + 65)
      else:         
        encrypt += chr((ord(i) + key - 97) % 26 + 97)          
        return encrypt
  
  def vowels(self):
    count = 0         
    escape = ['a', 'e', 'i', 'o', 'u']         
    for i in self.s:             
      if i.lower() in escape:                 
       count+=1         
      if count >= 5:             
        return "many"         
      return count         
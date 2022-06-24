def replace_string(filepath):
  text_file=open(filepath,'r')
  data=text_file.read()
  text_file.close()
  text_file=open(filepath,'w')
  return text_file.write(data.replace('placement','screening'))
replace_string('example.txt') 

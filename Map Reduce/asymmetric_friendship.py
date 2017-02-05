import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    value2 = "#"+key
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value,value2)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #found = False
    for v in list_of_values:
        if v[0] == '#':
            temp = v[1:]
            found = False
            for j in list_of_values:
                if j == temp:
                    found = True
            if found == False:
                mr.emit((temp,key))
                mr.emit((key,temp))
          
                

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

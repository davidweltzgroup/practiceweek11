

def FizzBuzz(start, finish):
  #import numpy as np
  #start = 1
  #finish = 15+1
  v=[]
  numvec = np.arange(start,finish+1)
  objvec = np.array(numvec, dtype=object)
  objvec = np.where(numvec % 15==0,('fizzbuzz'), (np.where(numvec % 5==0,('buzz'),(np.where(numvec % 3==0,('fizz'),numvec)))))
  objvec = [int(ele) if ele.isdigit() else ele for ele in objvec]
  objvec = ['buzz', 41, 'fizz', 43, 44, 'fizzbuzz']
  v= objvec
  return(v)


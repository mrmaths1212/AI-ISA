

from functions import write_file as write_file
import os


write_file.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
write_file.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
write_file.write_file("calculator", "/tmp/temp.txt", "this should not be allowed")





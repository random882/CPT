import os
import time

frames = [
r"""
  O 
 /|\ 
 / \ 
""",
r"""
  \O/
  |  
 / \ 
""",
r"""
  |O__
  |   
 / \  
""",
r"""
  \O
  |\
 / \
""",
r"""
__O 
 /| 
 / \
""",
r"""
  O/
  | 
 /|\
 """,
r"""
  O/
 /| 
 / \
""",
r"""
__O|
  | 
 / \
""",
]

# frames per second
FPS = 15 / 60  

for frame in frames:
    
    print(frame)
    time.sleep(FPS)
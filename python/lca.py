"""
# found nothing
  keep going down
# found a num
  Keep checking
  if finds the second, return true
  if it only finds one, return which one it found

"""

# def lca(head,a,b):
#   if head == None:
#     return None:
#   if head.val == a:
#     return a
#   if head.val == b:
#     return b
Class Node:
  def __init__(self, val, left, right):
    self.val = val
    self.right = right
    self.left = left

def path(head, a):
  if head == None:
    return[0]
  r = path(head.right, a)
  l = path(head.left, a)
  if head.val == a:
    return [a]
  if r[0] == a:
    return r.append(head.val)
  if l[0] == a:
    return l.append(head.val)

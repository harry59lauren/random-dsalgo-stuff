
import collections

def can_form_palindrome(s):
    cnt = collections.Counter([c.upper() for c in s])
    return len([k for k in cnt if cnt[k] % 2]) < 2




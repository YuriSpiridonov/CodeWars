# https://www.codewars.com/kata/the-hashtag-generator/train/python

def generate_hashtag(s):
    s = '#'+s.title()
    s = ''.join(s.split())
    if len(s) in range(2,140):
        return s
    else:    
        return False
        
print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')    
print(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')

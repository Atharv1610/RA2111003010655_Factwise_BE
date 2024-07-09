# If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?



def num_to_words(n):
    ones = ['','one','two','three','four','five','six','seven','eight','nine',
            'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    
    tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    if n == 1000:
        return 'one thousand'
    
    if n >= 100:
        if n % 100 == 0:
            return ones[n // 100] + ' hundred'
        else:
            return ones[n // 100] + ' hundred and ' + num_to_words(n % 100)
    
    if n >= 20:
        return tens[n // 10] + ('-' + ones[n % 10] if n % 10 != 0 else '')
    
    return ones[n]

def count_letters(n):
    return sum(len(word) for word in num_to_words(n).replace(' ','').replace('-',''))


start = int(input('Enter starting element: '))
end =  int(input('Enter the ending element: '))
total_letters = sum(count_letters(i) for i in range(start, end+1))
print(f"Total number of letters used: {total_letters}")

import textwrap

def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(width=max_width+1)
    word_list = wrapper.wrap(text=string)
    for i in word_list:
        print(i)

    return ""



    
    
        
    


        
 
    
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
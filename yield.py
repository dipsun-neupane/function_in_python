def even_generator(num):
    for i in range(1,num+1 , 2):
        yield i


for num in even_generator(10):
    print(num)


''' so , here in my opinion ( i alaso checked it ! )  - here basicaal,
the num goes inside that function even_genrator and picks up the value available there.
since there is even num up to a specified limit is being yield .
so now every time num is going upon that function,
it catches out that i being yeild and finally print it.'''


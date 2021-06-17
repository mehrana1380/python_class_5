my_class= "paniz zeinab mahnaz mehrana mohammad amin farokh reza meysam".split('')
for index, name in enumerate(my_class):
    print (f'nafare shomare {index} {name} ast')
    if index% 3== 0:
        continue

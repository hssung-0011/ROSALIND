""" Computing GC Content """

# -------------------------------------------------

def recog(dic):
    """ 줄바꿈 기준으로 나뉘진 텍스트 리스트를, '>' 기준으로 묶는다."""
    seq_list = []
    indx = 0
    for num in range(len(dic)):
        """첫 줄 예외처리, 첫줄 제외 나머지는 '>' 인식"""
        if (num !=0) and ('>' in dic[num]):
            seq_list.append(dic[indx:num])
            indx = num
        
        """마지막 줄 예외처리"""
        if num == len(dic)-1:
            seq_list.append(dic[indx:])
    return seq_list



def test_recog():
    assert recog(['>sample','ATAAAGG']) == [['>sample','ATAAAGG']]
    assert recog(['>sample','ATG','TTG']) == [['>sample','ATG','TTG']]
    assert recog(['>sp1','ATG','TGG','>sp2','T','G']) == [['>sp1','ATG','TGG'],['>sp2','T','G']]
    
    
    
def gc_percent(dict):
    percent_list = []
    for values in dict.values():
        gc_ratio = (values.count('G') + values.count('C')) * 100 / len(values)
        percent_list.append(gc_ratio)
    return percent_list

def test_gc_percent():
    assert gc_percent({'>s1':'ATTG'}) == [1/4]
    assert gc_percent({'>s2':'GGGG', '>s3':'AGGAT'}) == [100/1, 200/5]
    
# --------------------------------------------

filepath = ('/mnt/c/Users/jsml6/Downloads/rosalind_gc.txt')
f = open(filepath, 'r')
lines = f.readlines()

total_text = [line.rstrip() for line in lines]
f.close()

total_text = recog(total_text)

id_seq = {item[0][1:]:''.join(item[1:]) for item in total_text}
gc_ratio = gc_percent(id_seq)
gc_biggest = sorted(gc_ratio)[-1]
print(list(id_seq.keys())[gc_ratio.index(gc_biggest)])
print(gc_biggest)

from typing import Counter


tweet_names=["sachin tweet_id_1",
             "sehwag tweet_id_2",
             "sachin tweet_id_3",
             "sachin tweet_id_4",]

uniq_names=[pref_names.split()[0] for 
            pref_names in tweet_names]


times=Counter(uniq_names)
repeat=times.values()


for element in set(repeat):
    dep1=([(key,value) for 
    key,value in sorted (times.items()) if 
    value==element])



    if len (dep1)>1:
        for (key,value) in dep1:
            print(key,"", value)

    max_value=max(times.values()) 
    temp_max_result=[(key,value) for key,value in sorted(times.items()) if value ==max_value]


    if temp_max_result!=dep1:
        for (key,value) in temp_max_result:
            print(key,"",value)       


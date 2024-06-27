a=["f","n",'e','n','f','n','e']
print(round(a.count('f')/len(a)*100),round(a.count('n')/len(a)*100),round(a.count('e')/len(a)*100))
for i in range(36):
    print(f'wmatch{i} varchar(32),')


CREATE TABLE predictions(
    username varchar(32),
    prediction_id int identity(1,1) PRIMARY KEY,
    matchnum int, 
    eq1 varchar(32),
    eq2 varchar(32),
    score_eq1 varchar(32),
    score_eq2 varchar(32),
    )
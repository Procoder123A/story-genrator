import random
when=['last night','last year','yesterday','few months ago','few years ago','on 19/1/2012']
who=['an elephant','an ant','a lion','a tiger','a hippo','a hyena','a giraffe']
name=['sam','abdullah','koby','ifra','esa','singh','hamna','haider']
residence=['GERMANY','UAE','AMERICA','CANADA','AUSTRALIA','BRAZIL','PORTUGAL','IRAN','PAKISTAN']
went=['school','mall','airport','colage','friends house']
happend=['ATE A BURGER','FOUND A MYSTRY KEY']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' +
 random.choice(residence) + ' name '+ random.choice(name )+
 ', went to the ' + random.choice(went) + ' and ' + random.choice(happend))
# Support ---> lts 
-------------
null -----> database [column - null]
blank ----> form [column = null]


coment 
    text : null =True , blank=True

-------------
User :
    - username
    - email 
    - first_name
    - last_name
    - password 
    - Auth 


- extend User : 
    - BaseUser
    - AbstractBaseUser
    - one-to-one model

-----------------------------
        pre : before    delete   init   save
        post: after     delete   init   save 
        m2m


        action1     -----> send ------> function : call

        signup:save                   --> create profile
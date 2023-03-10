CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);



INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');


SELECT * FROM Posts


--Users initially generated 
INSERT INTO 'Users' VALUES (NULL,"Jason","Howes","jasonmatthewhowes@gmail.com","Is awesome very cool dude","jhowes","oyster","https://www.google.com/imgres?imgurl=https%3A%2F%2Fd1hbpr09pwz0sk.cloudfront.net%2Fprofile_pic%2Fjason-howes-91015d34.jpg&imgrefurl=https%3A%2F%2Frocketreach.co%2Fjason-howes-email_4752027&tbnid=cZ5ROgfimUu_DM&vet=12ahUKEwiV0JrTlej8AhU2G94AHZVaDj8QMygHegUIARC5AQ..i&docid=oAwVgvIKKSlvrM&w=200&h=200&itg=1&q=jason%20howes&ved=2ahUKEwiV0JrTlej8AhU2G94AHZVaDj8QMygHegUIARC5AQ","01/27/2023",1);	
INSERT INTO 'Users' VALUES (NULL,"Charles","Seals","charlesseals11@gmail.com","Is the best","cseals","oyster","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRVBmTkhlsg8WA9ctT4MMA3ZItV4m6xfVYBgFXeYfyQRH-w5WUQCT-r229fEsOSmU8kMU&usqp=CAU","01/27/2023",1);		
INSERT INTO 'Users' VALUES (NULL,"Emily","Nelson","evnelson2021@gmail.com","Is second best","evnelson","oyster","https://i.ytimg.com/vi/q6Ye-4vaSE8/maxresdefault.jpg","01/27/2023",1);		
INSERT INTO 'Users' VALUES (NULL,"Nathan","Pyles","nathanpyles.91@gmail.com","Is third best","npyles","oyster","https://cloudfront-us-east-1.images.arcpublishing.com/coxohio/BUH7WJB75XUROLJKH2S66JWF4U.jpg","01/27/2023",1);
--Posts Initially created			
INSERT INTO 'Posts' VALUES (NULL,1,1,"Bologna Up 30%","02-01-2022","https://upload.wikimedia.org/wikipedia/commons/c/c3/Bologna_lunch_meat_style_sausage.JPG","Bologna is up 30% according to Newsweek. That sucks says Jason Howes who really loves the shit",1)		
INSERT INTO 'Posts' VALUES (NULL,4,1,"The weather today","01-27-2023","https://s7d2.scene7.com/is/image/TWCNews/sun_dogs_cold","Today is 44 degrees and sunny in Music City. Why does it insist on being this cold?",1)		
INSERT INTO 'Posts' VALUES (NULL,2,2,"Big Potato Down 93%","10-31-1874","https://www.google.com/search?q=potato+farm+black+and+white&tbm=isch&ved=2ahUKEwji3PjCnuj8AhVOyFMKHZrkC94Q2-cCegQIABAA&oq=potato+farm+black+and+white&gs_lcp=CgNpbWcQAzoECCMQJzoFCAAQgAQ6BggAEAcQHlDECFjbDmDqD2gAcAB4AIABd4gBnwWSAQMwLjaYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=8ATUY-KkHM6QzwKaya_wDQ&bih=857&biw=1745&rlz=1C5CHFA_enUS698US699#imgrc=a40wlRjLC7RJZM","Potato Farm 1874",1)		
INSERT INTO 'Posts' VALUES (NULL,3,4,"Zappa Philosophy","01-01-1969","https://www.azquotes.com/picture-quotes/quote-a-wise-man-once-said-never-discuss-philosophy-or-politics-in-a-disco-environment-frank-zappa-37-54-57.jpg","Zappa wrote a beautiful book about life and music",1)		
		

--Categories Initially Created
INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Comedy');
INSERT INTO Categories ('label') VALUES ('Murder Mystery');
INSERT INTO Categories ('label') VALUES ('Music')

--Tag Initially
INSERT INTO Tags ('label') VALUES ('JavaScript');

--Reactions intially created
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');


--Table not listed in ERD
-- CREATE TABLE "DemotionQueue" (
--   "action" varchar,
--   "admin_id" INTEGER,
--   "approver_one_id" INTEGER,
--   FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
--   FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
--   PRIMARY KEY (action, admin_id, approver_one_id)
-- );


SELECT 
  a.id,
  a.user_id,
  a.category_id,
  a.title,
  a.publication_date,
  a.image_url,
  a.content,
  a.approved,
  b.id user_id,
  b.first_name user_first_name,
  b.last_name user_last_name,
  b.email user_email,
  c.id category_id,
  c.label
FROM Posts a
JOIN Users b 
  ON b.id = a.user_id
JOIN Categories c 
  ON c.id = a.category_id



        SELECT 
            a.id,
            a.user_id,
            a.category_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content,
            a.approved,
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
            FROM Posts a
            JOIN `Users` u
                on u.id = a.user_id
            WHERE a.user_id = 2
            ORDER BY u.id

            
SELECT 
  a.id,
  a.user_id,
  a.category_id,
  a.title,
  a.publication_date,
  a.image_url,
  a.content,
  a.approved,
  b.first_name user_first_name,
  b.last_name user_last_name,
  c.label category_label
  FROM Posts a
  JOIN Users b 
  ON b.id = a.user_id
  JOIN Categories c 
  ON c.id = a.category_id
  ORDER BY a.publication_date DESC


UPDATE Posts
SET publication_date = "2022-01-02"
WHERE id = 1

UPDATE Posts
SET publication_date = "2023-01-27"
WHERE id = 2

UPDATE Posts
SET publication_date = "1874-10-31"
WHERE id = 3

UPDATE Posts
SET publication_date = "1969-01-01"
WHERE id = 4

UPDATE Posts
SET image_url = "https://www.redrivervalleypotatoes.com/wp-content/uploads/2016/11/OLD-2003-P-10-0048c_Picking_potatoes_near_Park_River_ND.jpg"
WHERE id = 3

UPDATE Posts
  SET
    user_id = 3,
    category_id = 2,
    title = "Testing Edit",
    publication_date = "1675284696969",
    image_url = "google.com",
    content = "please work",
    approved = 1
  WHERE id = 13


UPDATE Posts
SET user_id = "2"
WHERE id = 5
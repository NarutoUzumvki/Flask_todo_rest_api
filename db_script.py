from connection import connection
cursor = connection.cursor()

create_query = """
CREATE TABLE `Todo`(
    `S.NO` INT AUTO_INCREMENT PRIMARY KEY,
    `TITLE` VARCHAR(50) DEFAULT NULL,
    `DESCRIPTION` VARCHAR(500) NOT NULL,
    `TIME` DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""

# cursor.execute(create_query)

insert_query = """
INSERT INTO `Todo`(`TITLE`, `DESCRIPTION`)
values
    ("Work", "Have a Meeting Tommorow at 2:30"),
    ("Gym", "Have to increase 2 Sets of each Workout"),
    ("Laundary", "Have to Wash all the Winter clothes that are kept inside the Trolly"),
    ("Medicine", "Need to Buy an Eno and an Anti-Fungal Ointment for Your neck.")
"""

# cursor.execute(insert_query)
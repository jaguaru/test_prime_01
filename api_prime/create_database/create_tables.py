####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

# CREATE TABLE ApiPrime.rooms (
#   id INT auto_increment primary key NOT NULL,
#   code varchar(8) NULL UNIQUE,
#   name varchar(32) NULL UNIQUE,
#   capacity varchar(7) NULL,
#   status  tinyint(1) DEFAULT 0,
#   created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#   updated DATETIME
# )
# ENGINE=InnoDB
# DEFAULT CHARSET=utf8mb4
# COLLATE=utf8mb4_0900_ai_ci;

# ####--------------------------------------------------------------------------------------------------------------
# ####--------------------------------------------------------------------------------------------------------------

# CREATE TABLE ApiPrime.events (
#   id INT auto_increment primary key NOT NULL,
#   code varchar(8) NULL UNIQUE,
#   name varchar(32) NULL UNIQUE,
#   type varchar(8) NULL,
#   status tinyint(1) DEFAULT 0,
#   fk_room_code varchar(8) NULL,
#   fk_event_code varchar(8) NULL,
#   fk_customer_code varchar(8) NULL,
#   created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#   updated DATETIME
# )
# ENGINE=InnoDB
# DEFAULT CHARSET=utf8mb4
# COLLATE=utf8mb4_0900_ai_ci;

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

# CREATE TABLE ApiPrime.customers (
#   id INT auto_increment primary key NOT NULL,
#   code varchar(8) NULL UNIQUE,
#   phone varchar(32) NULL UNIQUE,
#   name varchar(32) NULL UNIQUE,
#   lastname varchar(32) NULL UNIQUE,
#   status  tinyint(1) DEFAULT 0,
#   created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#   updated DATETIME
# )
# ENGINE=InnoDB
# DEFAULT CHARSET=utf8mb4
# COLLATE=utf8mb4_0900_ai_ci;

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------


DELIMITER $$

CREATE PROCEDURE get_user_by_credentials(user_email varchar(70), user_password varchar(100))
BEGIN
    SELECT * FROM users WHERE users.password = user_password AND users.email = user_email;
END $$

DELIMITER ;
import os
def get_env():
    host = os.getenv("DB_HOST")
    if not host:
        raise ValueError("DB_HOST is required")
    if host.strip()=="":
        raise ValueError("DB_HOST not be emtmty")
    port = os.getenv("DB_PORT")
    if port is None:
        raise ValueError("DB_PORT is required ")
    try:
        port_int = int(port)
    except ValueError:
        raise ValueError("DB_PORT must be an integer")
    if port_int < 1 or port_int > 65535:
                    raise ValueError("DB_PORT must be equal 1-65535")
    dbname = os.getenv("DB_NAME")
    if dbname is None:
        raise ValueError("DB_NAME must be a string")
    if dbname.strip()=="":
        raise ValueError("DB_NAME not be empty")
    user = os.getenv("DB_USER")
    if user is None:
        raise ValueError("USER must be a string")
    if user.strip()=="":
        raise ValueError("DB_USER not be empty")
    password = os.getenv("DB_PASSWORD")
    if password is None or not isinstance(password, str):
        raise ValueError("PASSWORD must be a string")
    if password.strip()=="":
        raise ValueError("DB_PASSWORD not be empty") 
    return {"DB_HOST":host,
            "DB_PORT":port_int,
            "DB_NAME":dbname,
            "DB_USER":user,
            "DB_PASSWORD":password}
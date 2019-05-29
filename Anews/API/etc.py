# encoding :utf-8
def to_dict(dict):
    if "_sa_instance_state" in dict:
        del dict["_sa_instance_state"]
    return dict

def fail_msg(msg):
    message ={
        "status": 0,
        "message":msg
    }
def success_msg(msg):
    success_msg= {
        "status": 0,
        "message":"成功"
    }
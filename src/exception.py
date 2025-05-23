import sys
'''
1. Here we have make a custom exception 
2. using sys we feteched file_name,line_nbr  and error info 
3. overriden and call custom message from the functions
4. display using str func

'''
from src.logger import logging
def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_detail)

    def __str__(self) -> str:
        return self.error_message
    
if __name__=='__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('divide by zero')
        raise CustomException(e,sys)



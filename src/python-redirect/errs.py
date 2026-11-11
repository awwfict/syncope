import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁


#The first param's errors
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
#1)
msf3 = 'Routing failed. The first parameter is missing or has an unsupported type.' # param is none, zero / not exists or has an unsupported type

#2)
msf16 = 'Routing failed. Line number must be 1 or greater.' # param less than 1


# The Second param's errors and logs
# ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
#1)
mss6 = 'Routed successfully. Second parameter was not provided. Keep going.' #param is zero / none or not exists

#2) 
mss22 = 'Only one line was routed. The second param should be given as a valid type too. Please check your input later.' #param has unsupported type or less than 1

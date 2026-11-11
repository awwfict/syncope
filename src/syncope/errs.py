#The first param's errors
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
msf3 = '✕ Routing failed. The first parameter is missing or has an unsupported type.' # param is none, zero / not exists or has an unsupported type
msf16 = '✕ Routing failed. Line number must be 1 or greater.' # param less than 1


# The Second param's errors and logs
# ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
mss6 = '✓ Routed successfully. Second parameter was not provided. Keep going.' #param is zero / none or not exists
mss22 = '𝒊 Only one line was routed. The second param should be given as a valid type too. Please check your input later.' #param has unsupported type or less than 1


#General and other
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
msg23 = '𝒊 Line is currently busy. Waiting or reassigning params...' # line is locked in sync mode
msg4 = '✕ Routing failed. Line number does not exist in the current file.' # line number exceeds total file lines

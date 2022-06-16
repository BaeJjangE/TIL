import sys
import sendbot as sb

id = sys.argv[1]
pw = sys.argv[2]
tag = sys.argv[3]
contents = sys.argv[4]
num = int(sys.argv[5].strip())

BOT = sb.SendBot()

BOT.login(id, pw)
BOT.mix(tag, contents, num)
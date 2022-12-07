import json
import resources.helper as helper



### ASSUMES: Camera / Microphone / Contacts access for meet app = allowed



driver = helper.launch_app('pixel4xl_1')
helper.start_meet_session(driver)
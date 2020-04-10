from db.orm import dbInterface
from db.tables import Profile
p1 = Profile(first_name="Thomas", last_name="Edison", work_email="edison@example.com", personal_email="user_personal1@example.com", work_phone_number=111, personal_phone_number=222)
p2 = Profile(first_name="Issac", last_name="Newton", work_email="issac_newton@example.com", personal_email="user_personal1@example.com", work_phone_number=111, personal_phone_number=222)
p3 = Profile(first_name="Albert", last_name="Einstein", work_email="albert_einstein@example.com", personal_email="user_personal2@example.com", work_phone_number=111, personal_phone_number=222)
dbInterface.create_profile(p1)
dbInterface.create_profile(p2)
dbInterface.create_profile(p3)

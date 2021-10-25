
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import time


bhopkey = 32
master_break_key = 1
faceit_mode = 0
friendlyfire = 0
glow_esp_key = 112
radar = 0
noflash_amount = 0
panic_key = 122
sound_esp_enabled = 0
sound_esp_pitch = 300
sound_esp_max_range = 400


deserteagle = [{'weapon_id': 1, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8,
                'smooth': 15.00, 'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
dualberettas = [{'weapon_id': 2, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8,
                 'smooth': 15.00, 'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
fiveseven = [{'weapon_id': 3, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
              'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
glock = [{'weapon_id': 4, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
tec9 = [{'weapon_id': 5, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
         'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
p2000 = [{'weapon_id': 6, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
p250 = [{'weapon_id': 7, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
         'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
usp = [{'weapon_id': 8, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
        'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
cz = [{'weapon_id': 9, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
       'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
revolver = [{'weapon_id': 10, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
             'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
ak47 = [{'weapon_id': 11, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
         'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
aug = [{'weapon_id': 12, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
        'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
famas = [{'weapon_id': 13, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
galil = [{'weapon_id': 14, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
m4a1silencer = [{'weapon_id': 15, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8,
                 'smooth': 15.00, 'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
m4a4 = [{'weapon_id': 16, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
         'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
sg553 = [{'weapon_id': 17, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
awp = [{'weapon_id': 18, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
        'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
g3sg1 = [{'weapon_id': 19, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
scar20 = [{'weapon_id': 20, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
           'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
ssg08 = [{'weapon_id': 21, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
mag7 = [{'weapon_id': 22, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
         'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
nova = [{'weapon_id': 23, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
         'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
sawedoff = [{'weapon_id': 24, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
             'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
xm1014 = [{'weapon_id': 25, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
           'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
ppbizon = [{'weapon_id': 26, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
            'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
mac10 = [{'weapon_id': 27, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
mp5sd = [{'weapon_id': 28, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
mp7 = [{'weapon_id': 29, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
        'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
mp9 = [{'weapon_id': 30, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
        'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
p90 = [{'weapon_id': 31, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
        'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
ump45 = [{'weapon_id': 32, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
m249 = [{'weapon_id': 33, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
         'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
negev = [{'weapon_id': 34, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]
knife = [{'weapon_id': 35, 'aim_key': 1, 'aim_rotation': 1, 'aim_stick': 0, 'unknown': 0, 'aim_fov': 120.00, 'bone_selection': 1, 'bone_3': 5, 'bone_2': 6, 'bone_1': 7, 'bone_0': 8, 'smooth': 15.00,
          'aim_delay': 0, 'aim_time': 0, 'aim_thru_walls': 0, 'trigger_key': 86, 'trigger_delay': 1, 'trigger_pause': 5, 'trigger_after_shot': 175, 'horizontal_rcs': 5.00, 'vertical_rcs': 5.00}]


print("Config loaded")
print("Welcome to Sakura - Brain Damage Edition (because no one wanted to help me make a nice sexy UI)\n")


#print("Weapons:\n1) Desert Eagle\n2) Dual Berettas\n3) Five-Seven\n4) Glock-18\n5) Tec-9\n6) P2000\n7) P250\n8) USP-S\n9) CZ75-Auto\n10) R8 Revolver\n11) AK-47\n12) AUG\n13) FAMAS\n14) Galil-AR\n15) M4A1-S\n16) M4A4\n17) SG-553\n18) AWP\n19) G3SG1\n20) SCAR-20\n21) SSG-08\n22) MAG-7\n23) Nova\n24) Sawed Off\n25) XM1014\n26) PP-Bizon\n27) MAC-10\n28) MP5-SD\n29) MP7\n30) MP9\n31) P90\n32) UMP-45\n33) M249\n34) Negev\n35) Knife\n0) DUMP CONFIG")

while True:
    print("Weapons:\n1) Desert Eagle\n2) Dual Berettas\n3) Five-Seven\n4) Glock-18\n5) Tec-9\n6) P2000\n7) P250\n8) USP-S\n9) CZ75-Auto\n10) R8 Revolver\n11) AK-47\n12) AUG\n13) FAMAS\n14) Galil-AR\n15) M4A1-S\n16) M4A4\n17) SG-553\n18) AWP\n19) G3SG1\n20) SCAR-20\n21) SSG-08\n22) MAG-7\n23) Nova\n24) Sawed Off\n25) XM1014\n26) PP-Bizon\n27) MAC-10\n28) MP5-SD\n29) MP7\n30) MP9\n31) P90\n32) UMP-45\n33) M249\n34) Negev\n35) Knife\n0) DUMP CONFIG")
    Options = ("Options:\n1) Aim Key\n2) Aim Rotation\n3) Sticky Aim\n4) ???\n5) Aimbot FOV\n6) Bone Selection\n7) Bone 3\n8) Bone 2\n9) Bone 1\n10) Bone 0\n11) Smooth\n12) Aim Delay\n13) Aim Time\n14) Aim Through Walls\n15) Trigger Key\n16) Trigger Delay\n17) Trigger Pause\n18) Trigger After Shot\n19) Horizontal RCS\n20) Vertical RCS\n0) Go Back")
    weapon_id = int(input("Select Option: "))
    if weapon_id == 1:
        while True:
            cls()
            print("Weapon: Desert Eagle")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[DEAGLE] Aim Key: "))
                deserteagle[0]['aim_key'] = aim_key
                print("[DEAGLE] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[DEAGLE] Aim Rotation: "))
                deserteagle[0]['aim_rotation'] = aim_rotation
                print("[DEAGLE] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[DEAGLE] Sticky Aim: "))
                deserteagle[0]['aim_stick'] = aim_stick
                print("[DEAGLE] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")
            elif option_select == 5:
                aim_fov = float(input("[DEAGLE] Aim FOV: "))
                deserteagle[0]['aim_fov'] = aim_fov
                print("[DEAGLE] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)

            elif option_select == 6:
                bone_selection = int(input("[DEAGLE] Bone Selection: "))
                deserteagle[0]['bone_selection'] = bone_selection
                print("[DEAGLE] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)

            elif option_select == 7:
                bone_3 = int(input("[DEAGLE] Bone 3: "))
                deserteagle[0]['bone_3'] = bone_3
                print("[DEAGLE] Bone 3 set to: " + str(bone_3))
                time.sleep(2)

            elif option_select == 8:
                bone_2 = int(input("[DEAGLE] Bone 2: "))
                deserteagle[0]['bone_2'] = bone_2
                print("[DEAGLE] Bone 2 set to: " + str(bone_2))
                time.sleep(2)

            elif option_select == 9:
                bone_1 = int(input("[DEAGLE] Bone 1: "))
                deserteagle[0]['bone_1'] = bone_1
                print("[DEAGLE] Bone 1 set to: " + str(bone_1))
                time.sleep(2)

            elif option_select == 10:
                bone_0 = int(input("[DEAGLE] Bone 0: "))
                deserteagle[0]['bone_0'] = bone_0
                print("[DEAGLE] Bone 0 set to: " + str(bone_0))
                time.sleep(2)

            elif option_select == 11:
                smooth = float(input("[DEAGLE] Smooth: "))
                deserteagle[0]['smooth'] = smooth
                print("[DEAGLE] Smooth set to: " + str(smooth))
                time.sleep(2)

            elif option_select == 12:
                aim_delay = int(input("[DEAGLE] Aim Delay: "))
                deserteagle[0]['aim_delay'] = aim_delay
                print("[DEAGLE] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)

            elif option_select == 13:
                aim_time = int(input("[DEAGLE] Aim Time: "))
                deserteagle[0]['aim_time'] = aim_time
                print("[DEAGLE] Aim Time set to: " + str(aim_time))
                time.sleep(2)

            elif option_select == 14:
                aim_thru_walls = int(input("[DEAGLE] Aim Through Walls: "))
                deserteagle[0]['aim_thru_walls'] = aim_thru_walls
                print("[DEAGLE] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)

            elif option_select == 15:
                trigger_key = int(input("[DEAGLE] Trigger Key: "))
                deserteagle[0]['trigger_key'] = trigger_key
                print("[DEAGLE] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)

            elif option_select == 16:
                trigger_delay = int(input("[DEAGLE] Trigger Delay: "))
                deserteagle[0]['trigger_delay'] = trigger_delay
                print("[DEAGLE] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)

            elif option_select == 17:
                trigger_pause = int(input("[DEAGLE] Trigger Pause: "))
                deserteagle[0]['trigger_pause'] = trigger_pause
                print("[DEAGLE] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)

            elif option_select == 18:
                trigger_after_shot = int(input("[DEAGLE] Trigger After Shot: "))
                deserteagle[0]['trigger_after_shot'] = trigger_after_shot
                print("[DEAGLE] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)

            elif option_select == 19:
                horizontal_rcs = float(input("[DEAGLE] Horizontal RCS: "))
                deserteagle[0]['horizontal_rcs'] = horizontal_rcs
                print("[DEAGLE] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)

            elif option_select == 20:
                vertical_rcs = float(input("[DEAGLE] Vertical RCS: "))
                deserteagle[0]['vertical_rcs'] = vertical_rcs
                print("[DEAGLE] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
            else:
                print("[DEAGLE] Invalid Option")
                time.sleep(2)

    elif weapon_id == 2: # dual berettas
        while True:
            cls()
            print("[DUAL BERETTAS] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[DUAL BERETTAS] Aim Key: "))
                dualberettas[0]['aim_key'] = aim_key
                print("[DUAL BERETTAS] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[DUAL BERETTAS] Aim Rotation: "))
                dualberettas[0]['aim_rotation'] = aim_rotation
                print("[DUAL BERETTAS] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[DUAL BERETTAS] Sticky Aim: "))
                dualberettas[0]['aim_stick'] = aim_stick
                print("[DUAL BERETTAS] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")
            elif option_select == 5:
                aim_fov = float(input("[DUAL BERETTAS] Aim FOV: "))
                dualberettas[0]['aim_fov'] = aim_fov
                print("[DUAL BERETTAS] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[DUAL BERETTAS] Bone Selection: "))
                dualberettas[0]['bone_selection'] = bone_selection
                print("[DUAL BERETTAS] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)

            elif option_select == 7:
                bone_3 = int(input("[DUAL BERETTAS] Bone 3: "))
                dualberettas[0]['bone_3'] = bone_3
                print("[DUAL BERETTAS] Bone 3 set to: " + str(bone_3))
                time.sleep(2)

            elif option_select == 8:
                bone_2 = int(input("[DUAL BERETTAS] Bone 2: "))
                dualberettas[0]['bone_2'] = bone_2
                print("[DUAL BERETTAS] Bone 2 set to: " + str(bone_2))
                time.sleep(2)

            elif option_select == 9:
                bone_1 = int(input("[DUAL BERETTAS] Bone 1: "))
                dualberettas[0]['bone_1'] = bone_1
                print("[DUAL BERETTAS] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[DUAL BERETTAS] Bone 0: "))
                dualberettas[0]['bone_0'] = bone_0
                print("[DUAL BERETTAS] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[DUAL BERETTAS] Smooth: "))
                dualberettas[0]['smooth'] = smooth
                print("[DUAL BERETTAS] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[DUAL BERETTAS] Aim Delay: "))
                dualberettas[0]['aim_delay'] = aim_delay
                print("[DUAL BERETTAS] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[DUAL BERETTAS] Aim Time: "))
                dualberettas[0]['aim_time'] = aim_time
                print("[DUAL BERETTAS] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[DUAL BERETTAS] Aim Through Walls: "))
                dualberettas[0]['aim_thru_walls'] = aim_thru_walls
                print("[DUAL BERETTAS] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[DUAL BERETTAS] Trigger Key: "))
                dualberettas[0]['trigger_key'] = trigger_key
                print("[DUAL BERETTAS] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[DUAL BERETTAS] Trigger Delay: "))
                dualberettas[0]['trigger_delay'] = trigger_delay
                print("[DUAL BERETTAS] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[DUAL BERETTAS] Trigger Pause: "))
                dualberettas[0]['trigger_pause'] = trigger_pause
                print("[DUAL BERETTAS] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[DUAL BERETTAS] Trigger After Shot: "))
                dualberettas[0]['trigger_after_shot'] = trigger_after_shot
                print("[DUAL BERETTAS] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[DUAL BERETTAS] Horizontal RCS: "))
                dualberettas[0]['horizontal_rcs'] = horizontal_rcs
                print("[DUAL BERETTAS] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:
                vertical_rcs = float(input("[DUAL BERETTAS] Vertical RCS: "))
                dualberettas[0]['vertical_rcs'] = vertical_rcs
                print("[DUAL BERETTAS] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)
            
            elif option_select == 0:
                break
            else:
                print("[DUAL BERETTAS] Invalid Option")
                time.sleep(2)

    elif weapon_id == 3: #five seven
        while True:
            cls()
            print("[FIVE SEVEN] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[FIVE SEVEN] Aim Key: "))
                fiveseven[0]['aim_key'] = aim_key
                print("[FIVE SEVEN] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[FIVE SEVEN] Aim Rotation: "))
                fiveseven[0]['aim_rotation'] = aim_rotation
                print("[FIVE SEVEN] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[FIVE SEVEN] Sticky Aim: "))
                fiveseven[0]['aim_stick'] = aim_stick
                print("[FIVE SEVEN] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[FIVE SEVEN] Aim FOV: "))
                fiveseven[0]['aim_fov'] = aim_fov
                print("[FIVE SEVEN] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[FIVE SEVEN] Bone Selection: "))
                fiveseven[0]['bone_selection'] = bone_selection
                print("[FIVE SEVEN] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[FIVE SEVEN] Bone 3: "))
                fiveseven[0]['bone_3'] = bone_3
                print("[FIVE SEVEN] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[FIVE SEVEN] Bone 2: "))
                fiveseven[0]['bone_2'] = bone_2
                print("[FIVE SEVEN] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[FIVE SEVEN] Bone 1: "))
                fiveseven[0]['bone_1'] = bone_1
                print("[FIVE SEVEN] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[FIVE SEVEN] Bone 0: "))
                fiveseven[0]['bone_0'] = bone_0
                print("[FIVE SEVEN] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[FIVE SEVEN] Smooth: "))
                fiveseven[0]['smooth'] = smooth
                print("[FIVE SEVEN] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[FIVE SEVEN] Aim Delay: "))
                fiveseven[0]['aim_delay'] = aim_delay
                print("[FIVE SEVEN] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[FIVE SEVEN] Aim Time: "))
                fiveseven[0]['aim_time'] = aim_time
                print("[FIVE SEVEN] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[FIVE SEVEN] Aim Through Walls: "))
                fiveseven[0]['aim_thru_walls'] = aim_thru_walls
                print("[FIVE SEVEN] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[FIVE SEVEN] Trigger Key: "))
                fiveseven[0]['trigger_key'] = trigger_key
                print("[FIVE SEVEN] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[FIVE SEVEN] Trigger Delay: "))
                fiveseven[0]['trigger_delay'] = trigger_delay
                print("[FIVE SEVEN] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[FIVE SEVEN] Trigger Pause: "))
                fiveseven[0]['trigger_pause'] = trigger_pause
                print("[FIVE SEVEN] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[FIVE SEVEN] Trigger After Shot: "))
                fiveseven[0]['trigger_after_shot'] = trigger_after_shot
                print("[FIVE SEVEN] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[FIVE SEVEN] Horizontal RCS: "))
                fiveseven[0]['horizontal_rcs'] = horizontal_rcs
                print("[FIVE SEVEN] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[FIVE SEVEN] Vertical RCS: "))
                fiveseven[0]['vertical_rcs'] = vertical_rcs
                print("[FIVE SEVEN] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[FIVE SEVEN] Invalid Option")
                time.sleep(2)
            
    elif weapon_id == 4: #glock
        while True:
            cls()
            print("[GLOCK] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[GLOCK] Aim Key: "))
                glock[0]['aim_key'] = aim_key
                print("[GLOCK] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[GLOCK] Aim Rotation: "))
                glock[0]['aim_rotation'] = aim_rotation
                print("[GLOCK] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[GLOCK] Sticky Aim: "))
                glock[0]['aim_stick'] = aim_stick
                print("[GLOCK] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[GLOCK] Aim FOV: "))
                glock[0]['aim_fov'] = aim_fov
                print("[GLOCK] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[GLOCK] Bone Selection: "))
                glock[0]['bone_selection'] = bone_selection
                print("[GLOCK] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[GLOCK] Bone 3: "))
                glock[0]['bone_3'] = bone_3
                print("[GLOCK] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[GLOCK] Bone 2: "))
                glock[0]['bone_2'] = bone_2
                print("[GLOCK] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[GLOCK] Bone 1: "))
                glock[0]['bone_1'] = bone_1
                print("[GLOCK] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[GLOCK] Bone 0: "))
                glock[0]['bone_0'] = bone_0
                print("[GLOCK] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[GLOCK] Smooth: "))
                glock[0]['smooth'] = smooth
                print("[GLOCK] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[GLOCK] Aim Delay: "))
                glock[0]['aim_delay'] = aim_delay
                print("[GLOCK] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[GLOCK] Aim Time: "))
                glock[0]['aim_time'] = aim_time
                print("[GLOCK] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[GLOCK] Aim Through Walls: "))
                glock[0]['aim_thru_walls'] = aim_thru_walls
                print("[GLOCK] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[GLOCK] Trigger Key: "))
                glock[0]['trigger_key'] = trigger_key
                print("[GLOCK] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[GLOCK] Trigger Delay: "))
                glock[0]['trigger_delay'] = trigger_delay
                print("[GLOCK] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[GLOCK] Trigger Pause: "))
                glock[0]['trigger_pause'] = trigger_pause
                print("[GLOCK] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[GLOCK] Trigger After Shot: "))
                glock[0]['trigger_after_shot'] = trigger_after_shot
                print("[GLOCK] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[GLOCK] Horizontal RCS: "))
                glock[0]['horizontal_rcs'] = horizontal_rcs
                print("[GLOCK] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[GLOCK] Vertical RCS: "))
                glock[0]['vertical_rcs'] = vertical_rcs
                print("[GLOCK] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[GLOCK] Invalid Option")
                time.sleep(2)

    elif weapon_id == 5: #tec9
        while True:
            cls()
            print("[TEC9] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[TEC9] Aim Key: "))
                tec9[0]['aim_key'] = aim_key
                print("[TEC9] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[TEC9] Aim Rotation: "))
                tec9[0]['aim_rotation'] = aim_rotation
                print("[TEC9] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[TEC9] Sticky Aim: "))
                tec9[0]['aim_stick'] = aim_stick
                print("[TEC9] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[TEC9] Aim FOV: "))
                tec9[0]['aim_fov'] = aim_fov
                print("[TEC9] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[TEC9] Bone Selection: "))
                tec9[0]['bone_selection'] = bone_selection
                print("[TEC9] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[TEC9] Bone 3: "))
                tec9[0]['bone_3'] = bone_3
                print("[TEC9] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[TEC9] Bone 2: "))
                tec9[0]['bone_2'] = bone_2
                print("[TEC9] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[TEC9] Bone 1: "))
                tec9[0]['bone_1'] = bone_1
                print("[TEC9] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[TEC9] Bone 0: "))
                tec9[0]['bone_0'] = bone_0
                print("[TEC9] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[TEC9] Smooth: "))
                tec9[0]['smooth'] = smooth
                print("[TEC9] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[TEC9] Aim Delay: "))
                tec9[0]['aim_delay'] = aim_delay
                print("[TEC9] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[TEC9] Aim Time: "))
                tec9[0]['aim_time'] = aim_time
                print("[TEC9] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[TEC9] Aim Through Walls: "))
                tec9[0]['aim_thru_walls'] = aim_thru_walls
                print("[TEC9] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[TEC9] Trigger Key: "))
                tec9[0]['trigger_key'] = trigger_key
                print("[TEC9] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[TEC9] Trigger Delay: "))
                tec9[0]['trigger_delay'] = trigger_delay
                print("[TEC9] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[TEC9] Trigger Pause: "))
                tec9[0]['trigger_pause'] = trigger_pause
                print("[TEC9] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[TEC9] Trigger After Shot: "))
                tec9[0]['trigger_after_shot'] = trigger_after_shot
                print("[TEC9] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[TEC9] Horizontal RCS: "))
                tec9[0]['horizontal_rcs'] = horizontal_rcs
                print("[TEC9] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[TEC9] Vertical RCS: "))
                tec9[0]['vertical_rcs'] = vertical_rcs
                print("[TEC9] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[TEC9] Invalid Option")
                time.sleep(2)

    elif weapon_id == 6: #p2000
        while True:
            cls()
            print("[P2000] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[P2000] Aim Key: "))
                p2000[0]['aim_key'] = aim_key
                print("[P2000] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[P2000] Aim Rotation: "))
                p2000[0]['aim_rotation'] = aim_rotation
                print("[P2000] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[P2000] Sticky Aim: "))
                p2000[0]['aim_stick'] = aim_stick
                print("[P2000] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[P2000] Aim FOV: "))
                p2000[0]['aim_fov'] = aim_fov
                print("[P2000] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[P2000] Bone Selection: "))
                p2000[0]['bone_selection'] = bone_selection
                print("[P2000] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[P2000] Bone 3: "))
                p2000[0]['bone_3'] = bone_3
                print("[P2000] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[P2000] Bone 2: "))
                p2000[0]['bone_2'] = bone_2
                print("[P2000] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[P2000] Bone 1: "))
                p2000[0]['bone_1'] = bone_1
                print("[P2000] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[P2000] Bone 0: "))
                p2000[0]['bone_0'] = bone_0
                print("[P2000] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[P2000] Smooth: "))
                p2000[0]['smooth'] = smooth
                print("[P2000] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[P2000] Aim Delay: "))
                p2000[0]['aim_delay'] = aim_delay
                print("[P2000] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[P2000] Aim Time: "))
                p2000[0]['aim_time'] = aim_time
                print("[P2000] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[P2000] Aim Through Walls: "))
                p2000[0]['aim_thru_walls'] = aim_thru_walls
                print("[P2000] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[P2000] Trigger Key: "))
                p2000[0]['trigger_key'] = trigger_key
                print("[P2000] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[P2000] Trigger Delay: "))
                p2000[0]['trigger_delay'] = trigger_delay
                print("[P2000] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[P2000] Trigger Pause: "))
                p2000[0]['trigger_pause'] = trigger_pause
                print("[P2000] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[P2000] Trigger After Shot: "))
                p2000[0]['trigger_after_shot'] = trigger_after_shot
                print("[P2000] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[P2000] Horizontal RCS: "))
                p2000[0]['horizontal_rcs'] = horizontal_rcs
                print("[P2000] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[P2000] Vertical RCS: "))
                p2000[0]['vertical_rcs'] = vertical_rcs
                print("[P2000] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[P2000] Invalid Option")
                time.sleep(2)

    elif weapon_id == 7: #p250
        while True:
            cls()
            print("[P250] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[P250] Aim Key: "))
                p250[0]['aim_key'] = aim_key
                print("[P250] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[P250] Aim Rotation: "))
                p250[0]['aim_rotation'] = aim_rotation
                print("[P250] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[P250] Sticky Aim: "))
                p250[0]['aim_stick'] = aim_stick
                print("[P250] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[P250] Aim FOV: "))
                p250[0]['aim_fov'] = aim_fov
                print("[P250] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[P250] Bone Selection: "))
                p250[0]['bone_selection'] = bone_selection
                print("[P250] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[P250] Bone 3: "))
                p250[0]['bone_3'] = bone_3
                print("[P250] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[P250] Bone 2: "))
                p250[0]['bone_2'] = bone_2
                print("[P250] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[P250] Bone 1: "))
                p250[0]['bone_1'] = bone_1
                print("[P250] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[P250] Bone 0: "))
                p250[0]['bone_0'] = bone_0
                print("[P250] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[P250] Smooth: "))
                p250[0]['smooth'] = smooth
                print("[P250] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[P250] Aim Delay: "))
                p250[0]['aim_delay'] = aim_delay
                print("[P250] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[P250] Aim Time: "))
                p250[0]['aim_time'] = aim_time
                print("[P250] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[P250] Aim Through Walls: "))
                p250[0]['aim_thru_walls'] = aim_thru_walls
                print("[P250] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[P250] Trigger Key: "))
                p250[0]['trigger_key'] = trigger_key
                print("[P250] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[P250] Trigger Delay: "))
                p250[0]['trigger_delay'] = trigger_delay
                print("[P250] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[P250] Trigger Pause: "))
                p250[0]['trigger_pause'] = trigger_pause
                print("[P250] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[P250] Trigger After Shot: "))
                p250[0]['trigger_after_shot'] = trigger_after_shot
                print("[P250] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[P250] Horizontal RCS: "))
                p250[0]['horizontal_rcs'] = horizontal_rcs
                print("[P250] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[P250] Vertical RCS: "))
                p250[0]['vertical_rcs'] = vertical_rcs
                print("[P250] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[P250] Invalid Option")
                time.sleep(2)

    elif weapon_id == 8: #usps
        while True:
            cls()
            print("[USP-S] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[USP-S] Aim Key: "))
                usp[0]['aim_key'] = aim_key
                print("[USP-S] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[USP-S] Aim Rotation: "))
                usp[0]['aim_rotation'] = aim_rotation
                print("[USP-S] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[USP-S] Sticky Aim: "))
                usp[0]['aim_stick'] = aim_stick
                print("[USP-S] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[USP-S] Aim FOV: "))
                usp[0]['aim_fov'] = aim_fov
                print("[USP-S] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[USP-S] Bone Selection: "))
                usp[0]['bone_selection'] = bone_selection
                print("[USP-S] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[USP-S] Bone 3: "))
                usp[0]['bone_3'] = bone_3
                print("[USP-S] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[USP-S] Bone 2: "))
                usp[0]['bone_2'] = bone_2
                print("[USP-S] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[USP-S] Bone 1: "))
                usp[0]['bone_1'] = bone_1
                print("[USP-S] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[USP-S] Bone 0: "))
                usp[0]['bone_0'] = bone_0
                print("[USP-S] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[USP-S] Smooth: "))
                usp[0]['smooth'] = smooth
                print("[USP-S] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[USP-S] Aim Delay: "))
                usp[0]['aim_delay'] = aim_delay
                print("[USP-S] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[USP-S] Aim Time: "))
                usp[0]['aim_time'] = aim_time
                print("[USP-S] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[USP-S] Aim Through Walls: "))
                usp[0]['aim_thru_walls'] = aim_thru_walls
                print("[USP-S] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[USP-S] Trigger Key: "))
                usp[0]['trigger_key'] = trigger_key
                print("[USP-S] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[USP-S] Trigger Delay: "))
                usp[0]['trigger_delay'] = trigger_delay
                print("[USP-S] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[USP-S] Trigger Pause: "))
                usp[0]['trigger_pause'] = trigger_pause
                print("[USP-S] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[USP-S] Trigger After Shot: "))
                usp[0]['trigger_after_shot'] = trigger_after_shot
                print("[USP-S] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[USP-S] Horizontal RCS: "))
                usp[0]['horizontal_rcs'] = horizontal_rcs
                print("[USP-S] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[USP-S] Vertical RCS: "))
                usp[0]['vertical_rcs'] = vertical_rcs
                print("[USP-S] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[USP-S] Invalid Option")
                time.sleep(2)

    elif weapon_id == 9: #cz75
        while True:
            cls()
            print("[CZ75] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[CZ75] Aim Key: "))
                cz[0]['aim_key'] = aim_key
                print("[CZ75] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[CZ75] Aim Rotation: "))
                cz[0]['aim_rotation'] = aim_rotation
                print("[CZ75] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[CZ75] Sticky Aim: "))
                cz[0]['aim_stick'] = aim_stick
                print("[CZ75] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[CZ75] Aim FOV: "))
                cz[0]['aim_fov'] = aim_fov
                print("[CZ75] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[CZ75] Bone Selection: "))
                cz[0]['bone_selection'] = bone_selection
                print("[CZ75] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[CZ75] Bone 3: "))
                cz[0]['bone_3'] = bone_3
                print("[CZ75] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[CZ75] Bone 2: "))
                cz[0]['bone_2'] = bone_2
                print("[CZ75] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[CZ75] Bone 1: "))
                cz[0]['bone_1'] = bone_1
                print("[CZ75] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[CZ75] Bone 0: "))
                cz[0]['bone_0'] = bone_0
                print("[CZ75] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[CZ75] Smooth: "))
                cz[0]['smooth'] = smooth
                print("[CZ75] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[CZ75] Aim Delay: "))
                cz[0]['aim_delay'] = aim_delay
                print("[CZ75] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[CZ75] Aim Time: "))
                cz[0]['aim_time'] = aim_time
                print("[CZ75] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[CZ75] Aim Through Walls: "))
                cz[0]['aim_thru_walls'] = aim_thru_walls
                print("[CZ75] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[CZ75] Trigger Key: "))
                cz[0]['trigger_key'] = trigger_key
                print("[CZ75] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[CZ75] Trigger Delay: "))
                cz[0]['trigger_delay'] = trigger_delay
                print("[CZ75] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[CZ75] Trigger Pause: "))
                cz[0]['trigger_pause'] = trigger_pause
                print("[CZ75] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[CZ75] Trigger After Shot: "))
                cz[0]['trigger_after_shot'] = trigger_after_shot
                print("[CZ75] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[CZ75] Horizontal RCS: "))
                cz[0]['horizontal_rcs'] = horizontal_rcs
                print("[CZ75] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[CZ75] Vertical RCS: "))
                cz[0]['vertical_rcs'] = vertical_rcs
                print("[CZ75] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[CZ75] Invalid Option")
                time.sleep(2)
    
    elif weapon_id == 10: #revolver
        while True:
            cls()
            print("[R8 REVOLVER] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[R8 REVOLVER] Aim Key: "))
                revolver[0]['aim_key'] = aim_key
                print("[R8 REVOLVER] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[R8 REVOLVER] Aim Rotation: "))
                revolver[0]['aim_rotation'] = aim_rotation
                print("[R8 REVOLVER] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[R8 REVOLVER] Sticky Aim: "))
                revolver[0]['aim_stick'] = aim_stick
                print("[R8 REVOLVER] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[R8 REVOLVER] Aim FOV: "))
                revolver[0]['aim_fov'] = aim_fov
                print("[R8 REVOLVER] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[R8 REVOLVER] Bone Selection: "))
                revolver[0]['bone_selection'] = bone_selection
                print("[R8 REVOLVER] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[R8 REVOLVER] Bone 3: "))
                revolver[0]['bone_3'] = bone_3
                print("[R8 REVOLVER] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[R8 REVOLVER] Bone 2: "))
                revolver[0]['bone_2'] = bone_2
                print("[R8 REVOLVER] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[R8 REVOLVER] Bone 1: "))
                revolver[0]['bone_1'] = bone_1
                print("[R8 REVOLVER] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[R8 REVOLVER] Bone 0: "))
                revolver[0]['bone_0'] = bone_0
                print("[R8 REVOLVER] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[R8 REVOLVER] Smooth: "))
                revolver[0]['smooth'] = smooth
                print("[R8 REVOLVER] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[R8 REVOLVER] Aim Delay: "))
                revolver[0]['aim_delay'] = aim_delay
                print("[R8 REVOLVER] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[R8 REVOLVER] Aim Time: "))
                revolver[0]['aim_time'] = aim_time
                print("[R8 REVOLVER] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[R8 REVOLVER] Aim Through Walls: "))
                revolver[0]['aim_thru_walls'] = aim_thru_walls
                print("[R8 REVOLVER] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[R8 REVOLVER] Trigger Key: "))
                revolver[0]['trigger_key'] = trigger_key
                print("[R8 REVOLVER] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[R8 REVOLVER] Trigger Delay: "))
                revolver[0]['trigger_delay'] = trigger_delay
                print("[R8 REVOLVER] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[R8 REVOLVER] Trigger Pause: "))
                revolver[0]['trigger_pause'] = trigger_pause
                print("[R8 REVOLVER] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[R8 REVOLVER] Trigger After Shot: "))
                revolver[0]['trigger_after_shot'] = trigger_after_shot
                print("[R8 REVOLVER] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[R8 REVOLVER] Horizontal RCS: "))
                revolver[0]['horizontal_rcs'] = horizontal_rcs
                print("[R8 REVOLVER] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[R8 REVOLVER] Vertical RCS: "))
                revolver[0]['vertical_rcs'] = vertical_rcs
                print("[R8 REVOLVER] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[R8 REVOLVER] Invalid Option")
                time.sleep(2)
    
    elif weapon_id == 11: #ak47
        while True:
            cls()
            print("[AK-47] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[AK-47] Aim Key: "))
                ak47[0]['aim_key'] = aim_key
                print("[AK-47] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[AK-47] Aim Rotation: "))
                ak47[0]['aim_rotation'] = aim_rotation
                print("[AK-47] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[AK-47] Sticky Aim: "))
                ak47[0]['aim_stick'] = aim_stick
                print("[AK-47] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[AK-47] Aim FOV: "))
                ak47[0]['aim_fov'] = aim_fov
                print("[AK-47] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[AK-47] Bone Selection: "))
                ak47[0]['bone_selection'] = bone_selection
                print("[AK-47] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[AK-47] Bone 3: "))
                ak47[0]['bone_3'] = bone_3
                print("[AK-47] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[AK-47] Bone 2: "))
                ak47[0]['bone_2'] = bone_2
                print("[AK-47] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[AK-47] Bone 1: "))
                ak47[0]['bone_1'] = bone_1
                print("[AK-47] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[AK-47] Bone 0: "))
                ak47[0]['bone_0'] = bone_0
                print("[AK-47] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[AK-47] Smooth: "))
                ak47[0]['smooth'] = smooth
                print("[AK-47] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[AK-47] Aim Delay: "))
                ak47[0]['aim_delay'] = aim_delay
                print("[AK-47] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[AK-47] Aim Time: "))
                ak47[0]['aim_time'] = aim_time
                print("[AK-47] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[AK-47] Aim Through Walls: "))
                ak47[0]['aim_thru_walls'] = aim_thru_walls
                print("[AK-47] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[AK-47] Trigger Key: "))
                ak47[0]['trigger_key'] = trigger_key
                print("[AK-47] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[AK-47] Trigger Delay: "))
                ak47[0]['trigger_delay'] = trigger_delay
                print("[AK-47] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[AK-47] Trigger Pause: "))
                ak47[0]['trigger_pause'] = trigger_pause
                print("[AK-47] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[AK-47] Trigger After Shot: "))
                ak47[0]['trigger_after_shot'] = trigger_after_shot
                print("[AK-47] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[AK-47] Horizontal RCS: "))
                ak47[0]['horizontal_rcs'] = horizontal_rcs
                print("[AK-47] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[AK-47] Vertical RCS: "))
                ak47[0]['vertical_rcs'] = vertical_rcs
                print("[AK-47] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[AK-47] Invalid Option")
                time.sleep(2)
    
    elif weapon_id == 12: #aug
        while True:
            cls()
            print("[AUG] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[AUG] Aim Key: "))
                aug[0]['aim_key'] = aim_key
                print("[AUG] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[AUG] Aim Rotation: "))
                aug[0]['aim_rotation'] = aim_rotation
                print("[AUG] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[AUG] Sticky Aim: "))
                aug[0]['aim_stick'] = aim_stick
                print("[AUG] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[AUG] Aim FOV: "))
                aug[0]['aim_fov'] = aim_fov
                print("[AUG] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[AUG] Bone Selection: "))
                aug[0]['bone_selection'] = bone_selection
                print("[AUG] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[AUG] Bone 3: "))
                aug[0]['bone_3'] = bone_3
                print("[AUG] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[AUG] Bone 2: "))
                aug[0]['bone_2'] = bone_2
                print("[AUG] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[AUG] Bone 1: "))
                aug[0]['bone_1'] = bone_1
                print("[AUG] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[AUG] Bone 0: "))
                aug[0]['bone_0'] = bone_0
                print("[AUG] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[AUG] Smooth: "))
                aug[0]['smooth'] = smooth
                print("[AUG] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[AUG] Aim Delay: "))
                aug[0]['aim_delay'] = aim_delay
                print("[AUG] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[AUG] Aim Time: "))
                aug[0]['aim_time'] = aim_time
                print("[AUG] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[AUG] Aim Through Walls: "))
                aug[0]['aim_thru_walls'] = aim_thru_walls
                print("[AUG] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[AUG] Trigger Key: "))
                aug[0]['trigger_key'] = trigger_key
                print("[AUG] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[AUG] Trigger Delay: "))
                aug[0]['trigger_delay'] = trigger_delay
                print("[AUG] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[AUG] Trigger Pause: "))
                aug[0]['trigger_pause'] = trigger_pause
                print("[AUG] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[AUG] Trigger After Shot: "))
                aug[0]['trigger_after_shot'] = trigger_after_shot
                print("[AUG] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[AUG] Horizontal RCS: "))
                aug[0]['horizontal_rcs'] = horizontal_rcs
                print("[AUG] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[AUG] Vertical RCS: "))
                aug[0]['vertical_rcs'] = vertical_rcs
                print("[AUG] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[AUG] Invalid Option")
                time.sleep(2)
    
    elif weapon_id == 13: #famas
        while True:
            cls()
            print("[FAMAS] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[FAMAS] Aim Key: "))
                famas[0]['aim_key'] = aim_key
                print("[FAMAS] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[FAMAS] Aim Rotation: "))
                famas[0]['aim_rotation'] = aim_rotation
                print("[FAMAS] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[FAMAS] Sticky Aim: "))
                famas[0]['aim_stick'] = aim_stick
                print("[FAMAS] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[FAMAS] Aim FOV: "))
                famas[0]['aim_fov'] = aim_fov
                print("[FAMAS] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[FAMAS] Bone Selection: "))
                famas[0]['bone_selection'] = bone_selection
                print("[FAMAS] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[FAMAS] Bone 3: "))
                famas[0]['bone_3'] = bone_3
                print("[FAMAS] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[FAMAS] Bone 2: "))
                famas[0]['bone_2'] = bone_2
                print("[FAMAS] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[FAMAS] Bone 1: "))
                famas[0]['bone_1'] = bone_1
                print("[FAMAS] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[FAMAS] Bone 0: "))
                famas[0]['bone_0'] = bone_0
                print("[FAMAS] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[FAMAS] Smooth: "))
                famas[0]['smooth'] = smooth
                print("[FAMAS] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[FAMAS] Aim Delay: "))
                famas[0]['aim_delay'] = aim_delay
                print("[FAMAS] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[FAMAS] Aim Time: "))
                famas[0]['aim_time'] = aim_time
                print("[FAMAS] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[FAMAS] Aim Through Walls: "))
                famas[0]['aim_thru_walls'] = aim_thru_walls
                print("[FAMAS] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[FAMAS] Trigger Key: "))
                famas[0]['trigger_key'] = trigger_key
                print("[FAMAS] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[FAMAS] Trigger Delay: "))
                famas[0]['trigger_delay'] = trigger_delay
                print("[FAMAS] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[FAMAS] Trigger Pause: "))
                famas[0]['trigger_pause'] = trigger_pause
                print("[FAMAS] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[FAMAS] Trigger After Shot: "))
                famas[0]['trigger_after_shot'] = trigger_after_shot
                print("[FAMAS] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[FAMAS] Horizontal RCS: "))
                famas[0]['horizontal_rcs'] = horizontal_rcs
                print("[FAMAS] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[FAMAS] Vertical RCS: "))
                famas[0]['vertical_rcs'] = vertical_rcs
                print("[FAMAS] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[FAMAS] Invalid Option")
                time.sleep(2)
    
    elif weapon_id == 14: #galil
        while True:
            cls()
            print("[GALIL] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[GALIL] Aim Key: "))
                galil[0]['aim_key'] = aim_key
                print("[GALIL] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[GALIL] Aim Rotation: "))
                galil[0]['aim_rotation'] = aim_rotation
                print("[GALIL] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[GALIL] Sticky Aim: "))
                galil[0]['aim_stick'] = aim_stick
                print("[GALIL] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[GALIL] Aim FOV: "))
                galil[0]['aim_fov'] = aim_fov
                print("[GALIL] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[GALIL] Bone Selection: "))
                galil[0]['bone_selection'] = bone_selection
                print("[GALIL] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[GALIL] Bone 3: "))
                galil[0]['bone_3'] = bone_3
                print("[GALIL] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[GALIL] Bone 2: "))
                galil[0]['bone_2'] = bone_2
                print("[GALIL] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[GALIL] Bone 1: "))
                galil[0]['bone_1'] = bone_1
                print("[GALIL] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[GALIL] Bone 0: "))
                galil[0]['bone_0'] = bone_0
                print("[GALIL] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[GALIL] Smooth: "))
                galil[0]['smooth'] = smooth
                print("[GALIL] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[GALIL] Aim Delay: "))
                galil[0]['aim_delay'] = aim_delay
                print("[GALIL] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[GALIL] Aim Time: "))
                galil[0]['aim_time'] = aim_time
                print("[GALIL] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[GALIL] Aim Through Walls: "))
                galil[0]['aim_thru_walls'] = aim_thru_walls
                print("[GALIL] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[GALIL] Trigger Key: "))
                galil[0]['trigger_key'] = trigger_key
                print("[GALIL] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[GALIL] Trigger Delay: "))
                galil[0]['trigger_delay'] = trigger_delay
                print("[GALIL] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[GALIL] Trigger Pause: "))
                galil[0]['trigger_pause'] = trigger_pause
                print("[GALIL] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[GALIL] Trigger After Shot: "))
                galil[0]['trigger_after_shot'] = trigger_after_shot
                print("[GALIL] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[GALIL] Horizontal RCS: "))
                galil[0]['horizontal_rcs'] = horizontal_rcs
                print("[GALIL] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[GALIL] Vertical RCS: "))
                galil[0]['vertical_rcs'] = vertical_rcs
                print("[GALIL] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[GALIL] Invalid Option")
                time.sleep(2)
    
    elif weapon_id == 15: #m4a1-s
        while True:
            cls()
            print("[M4A1-S] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[M4A1-S] Aim Key: "))
                m4a1silencer[0]['aim_key'] = aim_key
                print("[M4A1-S] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[M4A1-S] Aim Rotation: "))
                m4a1silencer[0]['aim_rotation'] = aim_rotation
                print("[M4A1-S] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[M4A1-S] Sticky Aim: "))
                m4a1silencer[0]['aim_stick'] = aim_stick
                print("[M4A1-S] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[M4A1-S] Aim FOV: "))
                m4a1silencer[0]['aim_fov'] = aim_fov
                print("[M4A1-S] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[M4A1-S] Bone Selection: "))
                m4a1silencer[0]['bone_selection'] = bone_selection
                print("[M4A1-S] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[M4A1-S] Bone 3: "))
                m4a1silencer[0]['bone_3'] = bone_3
                print("[M4A1-S] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[M4A1-S] Bone 2: "))
                m4a1silencer[0]['bone_2'] = bone_2
                print("[M4A1-S] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[M4A1-S] Bone 1: "))
                m4a1silencer[0]['bone_1'] = bone_1
                print("[M4A1-S] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[M4A1-S] Bone 0: "))
                m4a1silencer[0]['bone_0'] = bone_0
                print("[M4A1-S] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[M4A1-S] Smooth: "))
                m4a1silencer[0]['smooth'] = smooth
                print("[M4A1-S] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[M4A1-S] Aim Delay: "))
                m4a1silencer[0]['aim_delay'] = aim_delay
                print("[M4A1-S] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[M4A1-S] Aim Time: "))
                m4a1silencer[0]['aim_time'] = aim_time
                print("[M4A1-S] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[M4A1-S] Aim Through Walls: "))
                m4a1silencer[0]['aim_thru_walls'] = aim_thru_walls
                print("[M4A1-S] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[M4A1-S] Trigger Key: "))
                m4a1silencer[0]['trigger_key'] = trigger_key
                print("[M4A1-S] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[M4A1-S] Trigger Delay: "))
                m4a1silencer[0]['trigger_delay'] = trigger_delay
                print("[M4A1-S] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[M4A1-S] Trigger Pause: "))
                m4a1silencer[0]['trigger_pause'] = trigger_pause
                print("[M4A1-S] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[M4A1-S] Trigger After Shot: "))
                m4a1silencer[0]['trigger_after_shot'] = trigger_after_shot
                print("[M4A1-S] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[M4A1-S] Horizontal RCS: "))
                m4a1silencer[0]['horizontal_rcs'] = horizontal_rcs
                print("[M4A1-S] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[M4A1-S] Vertical RCS: "))
                m4a1silencer[0]['vertical_rcs'] = vertical_rcs
                print("[M4A1-S] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[M4A1-S] Invalid Option")
                time.sleep(2)

    elif weapon_id == 16: #m4a4
        while True:
            cls()
            print("[M4A4] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[M4A4] Aim Key: "))
                m4a4[0]['aim_key'] = aim_key
                print("[M4A4] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[M4A4] Aim Rotation: "))
                m4a4[0]['aim_rotation'] = aim_rotation
                print("[M4A4] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[M4A4] Sticky Aim: "))
                m4a4[0]['aim_stick'] = aim_stick
                print("[M4A4] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[M4A4] Aim FOV: "))
                m4a4[0]['aim_fov'] = aim_fov
                print("[M4A4] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[M4A4] Bone Selection: "))
                m4a4[0]['bone_selection'] = bone_selection
                print("[M4A4] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[M4A4] Bone 3: "))
                m4a4[0]['bone_3'] = bone_3
                print("[M4A4] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[M4A4] Bone 2: "))
                m4a4[0]['bone_2'] = bone_2
                print("[M4A4] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[M4A4] Bone 1: "))
                m4a4[0]['bone_1'] = bone_1
                print("[M4A4] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[M4A4] Bone 0: "))
                m4a4[0]['bone_0'] = bone_0
                print("[M4A4] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[M4A4] Smooth: "))
                m4a4[0]['smooth'] = smooth
                print("[M4A4] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[M4A4] Aim Delay: "))
                m4a4[0]['aim_delay'] = aim_delay
                print("[M4A4] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[M4A4] Aim Time: "))
                m4a4[0]['aim_time'] = aim_time
                print("[M4A4] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[M4A4] Aim Through Walls: "))
                m4a4[0]['aim_thru_walls'] = aim_thru_walls
                print("[M4A4] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[M4A4] Trigger Key: "))
                m4a4[0]['trigger_key'] = trigger_key
                print("[M4A4] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[M4A4] Trigger Delay: "))
                m4a4[0]['trigger_delay'] = trigger_delay
                print("[M4A4] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[M4A4] Trigger Pause: "))
                m4a4[0]['trigger_pause'] = trigger_pause
                print("[M4A4] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[M4A4] Trigger After Shot: "))
                m4a4[0]['trigger_after_shot'] = trigger_after_shot
                print("[M4A4] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[M4A4] Horizontal RCS: "))
                m4a4[0]['horizontal_rcs'] = horizontal_rcs
                print("[M4A4] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[M4A4] Vertical RCS: "))
                m4a4[0]['vertical_rcs'] = vertical_rcs
                print("[M4A4] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[M4A4] Invalid Option")
                time.sleep(2)
    
    elif weapon_id == 17: #sg553
        while True:
            cls()
            print("[SG553] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[SG553] Aim Key: "))
                sg553[0]['aim_key'] = aim_key
                print("[SG553] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[SG553] Aim Rotation: "))
                sg553[0]['aim_rotation'] = aim_rotation
                print("[SG553] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[SG553] Sticky Aim: "))
                sg553[0]['aim_stick'] = aim_stick
                print("[SG553] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[SG553] Aim FOV: "))
                sg553[0]['aim_fov'] = aim_fov
                print("[SG553] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[SG553] Bone Selection: "))
                sg553[0]['bone_selection'] = bone_selection
                print("[SG553] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[SG553] Bone 3: "))
                sg553[0]['bone_3'] = bone_3
                print("[SG553] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[SG553] Bone 2: "))
                sg553[0]['bone_2'] = bone_2
                print("[SG553] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[SG553] Bone 1: "))
                sg553[0]['bone_1'] = bone_1
                print("[SG553] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[SG553] Bone 0: "))
                sg553[0]['bone_0'] = bone_0
                print("[SG553] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[SG553] Smooth: "))
                sg553[0]['smooth'] = smooth
                print("[SG553] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[SG553] Aim Delay: "))
                sg553[0]['aim_delay'] = aim_delay
                print("[SG553] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[SG553] Aim Time: "))
                sg553[0]['aim_time'] = aim_time
                print("[SG553] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[SG553] Aim Through Walls: "))
                sg553[0]['aim_thru_walls'] = aim_thru_walls
                print("[SG553] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[SG553] Trigger Key: "))
                sg553[0]['trigger_key'] = trigger_key
                print("[SG553] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[SG553] Trigger Delay: "))
                sg553[0]['trigger_delay'] = trigger_delay
                print("[SG553] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[SG553] Trigger Pause: "))
                sg553[0]['trigger_pause'] = trigger_pause
                print("[SG553] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[SG553] Trigger After Shot: "))
                sg553[0]['trigger_after_shot'] = trigger_after_shot
                print("[SG553] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[SG553] Horizontal RCS: "))
                sg553[0]['horizontal_rcs'] = horizontal_rcs
                print("[SG553] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[SG553] Vertical RCS: "))
                sg553[0]['vertical_rcs'] = vertical_rcs
                print("[SG553] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[SG553] Invalid Option")
                time.sleep(2)

    elif weapon_id == 18: #awp 
        while True:
            cls()
            print("[AWP] Options")
            print(Options)
            option_select = int(input("Option: "))
            if option_select == 1:
                aim_key = int(input("[AWP] Aim Key: "))
                awp[0]['aim_key'] = aim_key
                print("[AWP] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[AWP] Aim Rotation: "))
                awp[0]['aim_rotation'] = aim_rotation
                print("[AWP] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[AWP] Sticky Aim: "))
                awp[0]['aim_stick'] = aim_stick
                print("[AWP] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[AWP] Aim FOV: "))
                awp[0]['aim_fov'] = aim_fov
                print("[AWP] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[AWP] Bone Selection: "))
                awp[0]['bone_selection'] = bone_selection
                print("[AWP] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[AWP] Bone 3: "))
                awp[0]['bone_3'] = bone_3
                print("[AWP] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[AWP] Bone 2: "))
                awp[0]['bone_2'] = bone_2
                print("[AWP] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[AWP] Bone 1: "))
                awp[0]['bone_1'] = bone_1
                print("[AWP] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[AWP] Bone 0: "))
                awp[0]['bone_0'] = bone_0
                print("[AWP] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[AWP] Smooth: "))
                awp[0]['smooth'] = smooth
                print("[AWP] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[AWP] Aim Delay: "))
                awp[0]['aim_delay'] = aim_delay
                print("[AWP] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[AWP] Aim Time: "))
                awp[0]['aim_time'] = aim_time
                print("[AWP] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[AWP] Aim Through Walls: "))
                awp[0]['aim_thru_walls'] = aim_thru_walls
                print("[AWP] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[AWP] Trigger Key: "))
                awp[0]['trigger_key'] = trigger_key
                print("[AWP] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[AWP] Trigger Delay: "))
                awp[0]['trigger_delay'] = trigger_delay
                print("[AWP] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[AWP] Trigger Pause: "))
                awp[0]['trigger_pause'] = trigger_pause
                print("[AWP] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[AWP] Trigger After Shot: "))
                awp[0]['trigger_after_shot'] = trigger_after_shot
                print("[AWP] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[AWP] Horizontal RCS: "))
                awp[0]['horizontal_rcs'] = horizontal_rcs
                print("[AWP] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[AWP] Vertical RCS: "))
                awp[0]['vertical_rcs'] = vertical_rcs
                print("[AWP] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[AWP] Invalid Option")
                time.sleep(2)
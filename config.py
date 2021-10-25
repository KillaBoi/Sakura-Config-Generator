
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
                galil[0]['aim_key'] = aim_key
                print("[FIVE SEVEN] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[FIVE SEVEN] Aim Rotation: "))
                galil[0]['aim_rotation'] = aim_rotation
                print("[FIVE SEVEN] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[FIVE SEVEN] Sticky Aim: "))
                galil[0]['aim_stick'] = aim_stick
                print("[FIVE SEVEN] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[FIVE SEVEN] Aim FOV: "))
                galil[0]['aim_fov'] = aim_fov
                print("[FIVE SEVEN] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[FIVE SEVEN] Bone Selection: "))
                galil[0]['bone_selection'] = bone_selection
                print("[FIVE SEVEN] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[FIVE SEVEN] Bone 3: "))
                galil[0]['bone_3'] = bone_3
                print("[FIVE SEVEN] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[FIVE SEVEN] Bone 2: "))
                galil[0]['bone_2'] = bone_2
                print("[FIVE SEVEN] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[FIVE SEVEN] Bone 1: "))
                galil[0]['bone_1'] = bone_1
                print("[FIVE SEVEN] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[FIVE SEVEN] Bone 0: "))
                galil[0]['bone_0'] = bone_0
                print("[FIVE SEVEN] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[FIVE SEVEN] Smooth: "))
                galil[0]['smooth'] = smooth
                print("[FIVE SEVEN] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[FIVE SEVEN] Aim Delay: "))
                galil[0]['aim_delay'] = aim_delay
                print("[FIVE SEVEN] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[FIVE SEVEN] Aim Time: "))
                galil[0]['aim_time'] = aim_time
                print("[FIVE SEVEN] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[FIVE SEVEN] Aim Through Walls: "))
                galil[0]['aim_thru_walls'] = aim_thru_walls
                print("[FIVE SEVEN] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[FIVE SEVEN] Trigger Key: "))
                galil[0]['trigger_key'] = trigger_key
                print("[FIVE SEVEN] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[FIVE SEVEN] Trigger Delay: "))
                galil[0]['trigger_delay'] = trigger_delay
                print("[FIVE SEVEN] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[FIVE SEVEN] Trigger Pause: "))
                galil[0]['trigger_pause'] = trigger_pause
                print("[FIVE SEVEN] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[FIVE SEVEN] Trigger After Shot: "))
                galil[0]['trigger_after_shot'] = trigger_after_shot
                print("[FIVE SEVEN] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[FIVE SEVEN] Horizontal RCS: "))
                galil[0]['horizontal_rcs'] = horizontal_rcs
                print("[FIVE SEVEN] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[FIVE SEVEN] Vertical RCS: "))
                galil[0]['vertical_rcs'] = vertical_rcs
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
                galil[0]['aim_key'] = aim_key
                print("[GLOCK] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[GLOCK] Aim Rotation: "))
                galil[0]['aim_rotation'] = aim_rotation
                print("[GLOCK] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[GLOCK] Sticky Aim: "))
                galil[0]['aim_stick'] = aim_stick
                print("[GLOCK] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[GLOCK] Aim FOV: "))
                galil[0]['aim_fov'] = aim_fov
                print("[GLOCK] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[GLOCK] Bone Selection: "))
                galil[0]['bone_selection'] = bone_selection
                print("[GLOCK] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[GLOCK] Bone 3: "))
                galil[0]['bone_3'] = bone_3
                print("[GLOCK] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[GLOCK] Bone 2: "))
                galil[0]['bone_2'] = bone_2
                print("[GLOCK] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[GLOCK] Bone 1: "))
                galil[0]['bone_1'] = bone_1
                print("[GLOCK] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[GLOCK] Bone 0: "))
                galil[0]['bone_0'] = bone_0
                print("[GLOCK] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[GLOCK] Smooth: "))
                galil[0]['smooth'] = smooth
                print("[GLOCK] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[GLOCK] Aim Delay: "))
                galil[0]['aim_delay'] = aim_delay
                print("[GLOCK] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[GLOCK] Aim Time: "))
                galil[0]['aim_time'] = aim_time
                print("[GLOCK] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[GLOCK] Aim Through Walls: "))
                galil[0]['aim_thru_walls'] = aim_thru_walls
                print("[GLOCK] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[GLOCK] Trigger Key: "))
                galil[0]['trigger_key'] = trigger_key
                print("[GLOCK] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[GLOCK] Trigger Delay: "))
                galil[0]['trigger_delay'] = trigger_delay
                print("[GLOCK] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[GLOCK] Trigger Pause: "))
                galil[0]['trigger_pause'] = trigger_pause
                print("[GLOCK] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[GLOCK] Trigger After Shot: "))
                galil[0]['trigger_after_shot'] = trigger_after_shot
                print("[GLOCK] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[GLOCK] Horizontal RCS: "))
                galil[0]['horizontal_rcs'] = horizontal_rcs
                print("[GLOCK] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[GLOCK] Vertical RCS: "))
                galil[0]['vertical_rcs'] = vertical_rcs
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
                galil[0]['aim_key'] = aim_key
                print("[TEC9] Aim Key set to: " + str(aim_key))
                time.sleep(2)
            elif option_select == 2:
                aim_rotation = int(input("[TEC9] Aim Rotation: "))
                galil[0]['aim_rotation'] = aim_rotation
                print("[TEC9] Aim Rotation set to: " + str(aim_rotation))
                time.sleep(2)

            elif option_select == 3:
                aim_stick = int(input("[TEC9] Sticky Aim: "))
                galil[0]['aim_stick'] = aim_stick
                print("[TEC9] Sticky Aim set to: " + str(aim_stick))
                time.sleep(2)

            elif option_select == 4:
                print("unknown value, not changing")

            elif option_select == 5:
                aim_fov = float(input("[TEC9] Aim FOV: "))
                galil[0]['aim_fov'] = aim_fov
                print("[TEC9] Aim FOV set to: " + str(aim_fov))
                time.sleep(2)
            
            elif option_select == 6:
                bone_selection = int(input("[TEC9] Bone Selection: "))
                galil[0]['bone_selection'] = bone_selection
                print("[TEC9] Bone Selection set to: " + str(bone_selection))
                time.sleep(2)
            
            elif option_select == 7:
                bone_3 = int(input("[TEC9] Bone 3: "))
                galil[0]['bone_3'] = bone_3
                print("[TEC9] Bone 3 set to: " + str(bone_3))
                time.sleep(2)
            
            elif option_select == 8:
                bone_2 = int(input("[TEC9] Bone 2: "))
                galil[0]['bone_2'] = bone_2
                print("[TEC9] Bone 2 set to: " + str(bone_2))
                time.sleep(2)
            
            elif option_select == 9:
                bone_1 = int(input("[TEC9] Bone 1: "))
                galil[0]['bone_1'] = bone_1
                print("[TEC9] Bone 1 set to: " + str(bone_1))
                time.sleep(2)
            
            elif option_select == 10:
                bone_0 = int(input("[TEC9] Bone 0: "))
                galil[0]['bone_0'] = bone_0
                print("[TEC9] Bone 0 set to: " + str(bone_0))
                time.sleep(2)
            
            elif option_select == 11:
                smooth = float(input("[TEC9] Smooth: "))
                galil[0]['smooth'] = smooth
                print("[TEC9] Smooth set to: " + str(smooth))
                time.sleep(2)
            
            elif option_select == 12:
                aim_delay = int(input("[TEC9] Aim Delay: "))
                galil[0]['aim_delay'] = aim_delay
                print("[TEC9] Aim Delay set to: " + str(aim_delay))
                time.sleep(2)
            
            elif option_select == 13:
                aim_time = int(input("[TEC9] Aim Time: "))
                galil[0]['aim_time'] = aim_time
                print("[TEC9] Aim Time set to: " + str(aim_time))
                time.sleep(2)
            
            elif option_select == 14:
                aim_thru_walls = int(input("[TEC9] Aim Through Walls: "))
                galil[0]['aim_thru_walls'] = aim_thru_walls
                print("[TEC9] Aim Through Walls set to: " + str(aim_thru_walls))
                time.sleep(2)
            
            elif option_select == 15:
                trigger_key = int(input("[TEC9] Trigger Key: "))
                galil[0]['trigger_key'] = trigger_key
                print("[TEC9] Trigger Key set to: " + str(trigger_key))
                time.sleep(2)
            
            elif option_select == 16:
                trigger_delay = int(input("[TEC9] Trigger Delay: "))
                galil[0]['trigger_delay'] = trigger_delay
                print("[TEC9] Trigger Delay set to: " + str(trigger_delay))
                time.sleep(2)
            
            elif option_select == 17:
                trigger_pause = int(input("[TEC9] Trigger Pause: "))
                galil[0]['trigger_pause'] = trigger_pause
                print("[TEC9] Trigger Pause set to: " + str(trigger_pause))
                time.sleep(2)
            
            elif option_select == 18:
                trigger_after_shot = int(input("[TEC9] Trigger After Shot: "))
                galil[0]['trigger_after_shot'] = trigger_after_shot
                print("[TEC9] Trigger After Shot set to: " + str(trigger_after_shot))
                time.sleep(2)
            
            elif option_select == 19:
                horizontal_rcs = float(input("[TEC9] Horizontal RCS: "))
                galil[0]['horizontal_rcs'] = horizontal_rcs
                print("[TEC9] Horizontal RCS set to: " + str(horizontal_rcs))
                time.sleep(2)
            
            elif option_select == 20:

                vertical_rcs = float(input("[TEC9] Vertical RCS: "))
                galil[0]['vertical_rcs'] = vertical_rcs
                print("[TEC9] Vertical RCS set to: " + str(vertical_rcs))
                time.sleep(2)

            elif option_select == 0:
                break
        
            else:
                print("[TEC9] Invalid Option")
                time.sleep(2)
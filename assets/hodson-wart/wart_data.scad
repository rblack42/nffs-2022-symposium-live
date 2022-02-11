//######################################
// A6 - class rule constraints

max_wing_area = 30;		// square inches
spar_size = 1/16;
min_rib_thickness = 1/32;
min_rib_height = 1/16;
max_motor_stick_length = 6;
max_prop_diameter = 6;
prop_blade_thickness = 1/32;	// flat
min_weight = 1.2;			        // grams

//##################################################
// paper tubes
pt_t = 1/64;
pt_id = 1/16;
pt_r = 1/32;
pt_h = 0.25;

//######################################
wing_center_chord = 2;
wing_center_span = 8;
wing_tip_chord = 1.75;
wing_tip_span = 3.75;
wing_rib_camber = 4;
wing_tip_dihedral = 7/16;
winglet_chord = 1.75;
winglet_span = 1.25;

//######################################
stab_center_chord = 1.75;
stab_tip_chord = 1;
stab_span = 10 + 14/16;
stab_camber = 2;
stab_tip_dihedral = 7/8;

//######################################
fin_radius = 2;

//######################################
ms_length = max_motor_stick_length;
ms_front_height = 0.160;
ms_height = 0.190;
ms_rear_height = 0.160;
ms_front_post = 1.25;
ms_thickness = 0.070;
wing_post_height = 7/8;

// motor stick polygon
ms_x0 = 0.0;
ms_x1 = ms_length;
ms_x2 = ms_length;
ms_x3 = ms_front_post + wing_center_chord + 2 * (pt_r + pt_t);
ms_x4 = ms_front_post + pt_r + pt_t;
ms_x5 = 0.25;
ms_x6 = 0.0;

ms_y = ms_thickness;

ms_z0 = 0.0;
ms_z1 = 0.0;
ms_z2 = ms_rear_height;
ms_z3 = ms_height;
ms_z4 = ms_height;
ms_z5 = 0.18;
ms_z6 = ms_front_height;

ms_poly = [
    [ms_x0, ms_z0],
    [ms_x1, ms_z1],
    [ms_x2, ms_z2],
    [ms_x3, ms_z3],
    [ms_x4, ms_z4],
    [ms_x5, ms_z5],
    [ms_x6, ms_z6],
];

//######################################
tail_boom_length = 8.5;
tail_boom_front_height = 1/8;
tail_boom_thickness = 1/16;
tail_boom_rear_height = 1/16;
tail_boom_overlap = 0.5;
tail_boom_elevation = ms_rear_height + 3/16;
tb_overlap = 0.25;



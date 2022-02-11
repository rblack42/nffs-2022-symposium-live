include <../wart_data.scad>
include <MMlib/colors.scad>
use <./prop_blade.scad>

$fn=50;
prop_spar_l = 3;
prop_spar_center_r = 1/16;
prop_spar_tip_r = 1/16;
prop_pitch_angle = 45;

module prop_spar() {
    color(WOOD_Balsa) {
        cylinder(
            h=prop_spar_l/2,
            r1=prop_spar_center_r,
            r2=prop_spar_tip_r);
        rotate([180,0,0])
            cylinder(
            h=prop_spar_l/2,
            r1=prop_spar_center_r,
            r2=prop_spar_tip_r);
    }
}

module prop_wire() {
    color(METAL_Aluminium)
    rotate([90,90,0]) cylinder(h=1, r=1/64);
}

module propeller() {
        prop_spar();
        rotate([0,0,90]) {
            prop_wire();
            rotate([0,0,180+prop_pitch_angle])
          translate([0,0,0.5])
            prop_blade();
          rotate([0,180,-180-prop_pitch_angle])
            translate([0,0,0.5])
            prop_blade();
    }
}

//

propeller();

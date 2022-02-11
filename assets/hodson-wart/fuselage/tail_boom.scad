// tail_boom.scad
$fn=100;

use <MMlib/single_taper_spar.scad>
include <../wart_data.scad>
include <MMlib/colors.scad>

module tail_boom() {
  color(WOOD_Balsa) {
    translate([0,tail_boom_thickness/2,0])
      rotate([180,0,0])   // top surface is level
        single_taper_spar(
          l = tail_boom_length,
          z1 = tail_boom_front_height,
          z2 = tail_boom_rear_height,
          t = tail_boom_thickness
        );
    translate([-0.25,0,-tail_boom_thickness/2])
      rotate([0,90,0])
        cylinder(h=0.25, r=1/32);
  }
}

tail_boom();


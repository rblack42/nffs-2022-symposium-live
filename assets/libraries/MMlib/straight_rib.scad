//#####################################
// straight_rib
// (c) 2021 - Roie R. Black
//=====================================
$fn = 100;

use <MMlib/rib_strip.scad>

module straight_rib(r=3, w=4, t=0.5, h=0.5) {
  translate([0,t/2,0])
    rotate([90,0,0])
      linear_extrude(height = t)
        rib_strip(r,w,h);
}


straight_rib();

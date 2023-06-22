//#####################################
// rib_strip
// (c) 2021 - Roie R. Black
//=====================================
$fn = 100;
use <MMlib/circle_strip.scad>

module rib_strip(r=3, w=4, t=0.5) {
  dy = sqrt((r-t)*(r-t) - (w/2)*(w/2));
    translate([0,-dy])
      intersection() {
        circle_strip(r,t);
        translate([-w/2,0])
          square([w,2*r]);
      }
}

rib_strip();

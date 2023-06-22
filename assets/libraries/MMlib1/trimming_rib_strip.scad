//#####################################
// trimming_rib_strip
// (c) 2021 - Roie R. Black
//=====================================
$fn = 100;
use <MMlib/circle_strip.scad>


module trimming_rib_strip(r=3, w=4, t=0.5) {
  wt = 1.1*w;
  dy = sqrt((r-t)*(r-t) - (w/2)*(w/2));
  dyt = sqrt((r-t)*(r-t) - (wt/2)*(wt/2));
    translate([0,-dy])
      intersection() {
        circle_strip(r,t);
        translate([-wt/2,0])
          square([wt,2*r]);
      }
}

trimming_rib_strip();

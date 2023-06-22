//#####################################
// circular_arc_spar
// (c) 2021 - Roie R. Black
//=====================================
$fn = 100;

use <MMlib/circular_arc_strip.scad>


module circular_arc_spar(
    r=3,
    start_angle=0, end_angle=270,
    t=0.5,
    h=0.5
  ) {
  linear_extrude(height=h)
    circular_arc_strip(r,start_angle, end_angle, t);
}

circular_arc_spar();
